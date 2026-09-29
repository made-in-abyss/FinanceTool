import matplotlib.pyplot as plt
import numpy
import json
##   _____ . _____    |                        ______  ._____
##   |     | |    \   |       /\     |\    |  /        |
##   |____ | | __ /   |      /  \    | \   | |         |
##   |     | |   \    |     /____\   |  \  | |         |_____
##   |     | |    \   |    /      \  |   \ | |         |
##   |     | |     \  |__ /        \ |    \|  \______  |_____
##   github.com/made-in-abyss
TITLE = "Geometric Brownian Simulation (Student-t)"
mu = 0.1 / 252
std = 0.45 / numpy.sqrt(252)
dt = 1
df = 4.0
def _gen_ret():
  return numpy.exp(
      (mu - (std**2) / 2) * dt + std * numpy.sqrt(dt) * numpy.random.standard_t(df=df)
  )
def run_simulation(n=1000, base=10):
  ly = [base]
  for _ in range(2, n + 3):
    base *= _gen_ret()
    ly.append(base)
  return ly


if __name__ == "__main__":
  prices = run_simulation()
  print(json.dumps({"prices": prices}))