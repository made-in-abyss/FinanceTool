import matplotlib.pyplot as plt
import numpy
import json

##   _____ . _____                             ______   _____
##   |     | |    \   |       /\     |\    |  -        |
##   |____ | | __ /   |      /  \    | \   | |         |
##   |     | |   \    |     /____\   |  \  | |         |_____
##   |     | |    \   |    /      \  |   \ | |         |
##   |     | |     \  |__ /        \ |    \|  -______  |_____
##   github.com/made-in-abyss
TITLE = "Normal Distribution Simulation"
mu = 0.1/252
std = 0.45/numpy.sqrt(252)
dt = 1
df = 4.0

def _gen_ret():
  return (1+ (mu+std*numpy.random.standard_normal()))

def run_simulation(n=1000, base=10):
  ly = [base]
  for _ in range(2, n + 3):
    base *= _gen_ret()
    ly.append(base)
  return ly


if __name__ == "__main__":
  prices = run_simulation()
  print(json.dumps({"prices": prices}))