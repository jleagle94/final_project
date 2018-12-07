import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import special
from scipy.integrate import odeint


def rho(w):
    if w >= 0:
        return np.exp(w)*scipy.special.erf(np.sqrt(w))-np.sqrt((4*w)/(np.pi))*(1+(2*w)/3)
    else:
        return 0.

def king(y,x):
    w, z = y
    if x==0:
        d0=0
    else:
        d0=-2*x/z
    dydx = [z, d0 - rho(w)]
    return dydx

def main():

    x = np.linspace(0, float(sys.argv[1]), 100)   # Use rappture to input second number
    y_init=[float(sys.argv[2]), 0]      # Use rappture to input first number

    sol=odeint(king, y_init, x)

    plt.plot(x, sol[:,0])

    plt.show()

if __name__ == "__main__":
    main()

#plt.plot(rho(y),r,label='rho(y) vs. r')
#plt.xlabel('radius')
#plt.ylabel('rho(y)')
#plt.legend()
#plt.show()
