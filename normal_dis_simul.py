import matplotlib.pyplot as plt
import numpy

##   _____ . _____                             ______   _____
##   |     | |    \   |       /\     |\    |  -        |
##   |____ | | __ /   |      /  \    | \   | |         |
##   |     | |   \    |     /____\   |  \  | |         |_____
##   |     | |    \   |    /      \  |   \ | |         |
##   |     | |     \  |__ /        \ |    \|  -______  |_____
##   github.com/made-in-abyss


def gen_return(mu, sd):
    sum = 0
    for i in range(1,21):
        sum+=numpy.random.randint(0,101)/100
    sum -= 10
    sum = sum/numpy.sqrt(20/12)
    return mu+sum*sd

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


def __main__():
    n = int(input("Input length: "))
    b = int(input("Base value: "))
    for x in range(0,n):
        lx.append(x)
        rate = gen_return(0.0001,0.01)
        y = b*(1+rate)
        ly.append(y)
        r.append(rate)
        b = y
    print(_gStandardDev())
    plt.plot(lx,ly,label = 'Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
__main__()