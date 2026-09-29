def run_strategy(prices, initial_balance, risk_per_trade):
    balance = initial_balance
    position = 0
    shares = 0
    window = []
    buy_signals = []
    sell_signals = []
    for current_day, p in enumerate(prices):
        window.append(p)
        if len(window) > 20:
            window.pop(0)

            
        if len(window) == 20:
            sma = sum(window) / 20
            variance = sum((x - sma) ** 2 for x in window) / 20
            std_dev = variance ** 0.5
            lower_band = sma - (2 * std_dev)

            
            if position == 1 and p >= sma:
                balance += shares * p
                position = 0
                shares = 0
                sell_signals.append((current_day, p))
            elif position == 0 and balance > 0 and p <lower_band:
                position = 1
                allocated_cash = balance*risk_per_trade
                shares = allocated_cash / p
                balance -= allocated_cash
                buy_signals.append((current_day, p))


    if position == 1:
        balance += shares * prices[-1]
        sell_signals.append((len(prices)-1, prices[-1]))
        
    return balance, buy_signals, sell_signals