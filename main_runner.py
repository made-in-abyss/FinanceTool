import importlib
import json
import os
import subprocess
import matplotlib.pyplot as plt

##   _____ . _____    |                        ______  ._____
##   |     | |    \   |       /\     |\    |  /        |
##   |____ | | __ /   |      /  \    | \   | |         |
##   |     | |   \    |     /____\   |  \  | |         |_____
##   |     | |    \   |    /      \  |   \ | |         |
##   |     | |     \  |__ /        \ |    \|  \______  |_____
##   github.com/made-in-abyss

ENGINES = {
    "1": ("Geometric Brownian (Student-t) [PREFERRED]", "engines/geobrown2.py"),
    "2": ("Geometric Brownian (Standard)", "engines/geobrown.py"),
    "3": ("Normal Distribution", "engines/normaldis.py"),
}

STRATEGIES = {
    "1": ("Bollinger Bands Mean Reversion", "strategies.bollinger"),
}

def select_menu(options):
    for key, (desc, _) in options.items():
        print(f"[{key}] {desc}")
    choice = input("Select option: ")
    return options.get(choice)[1] if choice in options else None

def __main__():
    balance_start =float(input("Enter starting balance: "))
    risk_pct =float(input("Risk percentage per trade: ")) /100
    engine_choice = select_menu(ENGINES)
    if not engine_choice:
        print("Faied to select engine selection")
        return
        
    strategy_choice = select_menu(STRATEGIES)
    if not strategy_choice:
        print("Failed to select strat")
        return
    
    print(f"\nRunning simulation engine:{engine_choice}")
    result = subprocess.run(["python", engine_choice], capture_output=True, check=True, text=True)
    try:
        data = json.loads(result.stdout)
        prices = data.get("prices", [])
    except json.JSONDecodeError:
        print("Failed to parse json")
        return
    
    print(f"Strategy: {strategy_choice}")
    strat_module = importlib.import_module(strategy_choice)
    final_balance, buys, sells = strat_module.run_strategy(prices, balance_start, risk_pct)
    time_steps = list(range(len(prices)))
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.plot(time_steps, prices, label='Price', linewidth=1.5,color='royalblue',alpha=0.8)
    if buys:
        bx, by = zip(*buys)
        ax.scatter(bx, by, marker='^', color='limegreen', s=100, label='Buy', zorder=5)
    if sells:
        sx,sy =zip(*sells)
        ax.scatter(sx, sy, marker='v',color='crimson', s=100,label='Sell', zorder=5)

    net_pnl = final_balance - balance_start
    roi = (net_pnl /balance_start)*100 if balance_start > 0 else 0
    
    metrics_text = (
        f"Strategy      : {strategy_choice}\n"
        f"Engine        : {engine_choice}\n"
        f"Start Balance : ${balance_start:.2f}\n"
        f"Final Balance : ${final_balance:.2f}\n"
        f"Net PnL       : ${net_pnl:.2f} ({roi:.2f}%)\n"
    )
    props = dict(boxstyle='round', facecolor='white', alpha=0.85, edgecolor='gray', linewidth=1.2)
    ax.text(0.03, 0.95, metrics_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=props, family='monospace')

    plt.style.use('seaborn-v0_8-darkgrid')
    ax.set_xlabel('Time (day)')
    ax.set_ylabel('Price')
    ax.legend(loc='lower right')
    ax.set_title(f"Simulated run: {strategy_choice} on {engine_choice}")
    plt.show()

if __name__ == "__main__":
    __main__()