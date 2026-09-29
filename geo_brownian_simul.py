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
TITLE = "Geometric Brownian Simulation"
mu = 0.07/252
std = 0.35/numpy.sqrt(252)
dt = 1


def _var():
    variance = 0
    for i in range(1,21):
        variance+=numpy.random.randint(0,101)/100
    variance -= 10
    variance = variance/numpy.sqrt(20/12)
    return variance

def _genRet():
    return numpy.exp( (mu-(std**2)/2)*dt+std*numpy.sqrt(dt)*_var())

lx = []
ly = []
r  = []

def _gStandardDev() -> float:
    sum = 0
    for i in r:
        sum+=i
    avg = sum/len(r)
    sigma = 0
    for i in r:
        sigma += (i-avg)**2
    sigma/= len(r)
    sigma = numpy.sqrt(sigma)
    return sigma

def _output():
    line1 = plt.plot(lx, ly,label='Price0', linewidth=1.5)
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.xlabel(xlabel= 'Time (day)')
    plt.ylabel(ylabel='Price')
    labels = [l.get_label() for l in line1]
    plt.legend(line1, labels, loc='upper right')
    plt.title(TITLE)
    plt.show()
    data = {"prices: ": ly}
    print(json.dumps(data))



def __main__():
    n = int(input("Input length: "))
    b = int(input("Base value: "))
    lx.append(1)
    ly.append(b)
    for x in range(2,n+3):
        lx.append(x)
        rate = _genRet()
        b*=rate
        ly.append(b)
        r.append(rate)
    ##print(_gStandardDev())
    _output()

__main__()