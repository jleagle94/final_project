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

    x = 0.0001
    dx = 0.0001
    y_init=[float(sys.argv[1]), 0]      # Use rappture to input first number
    yy = y_init[0]
 
    r = []
    psi = []
    dens = []
    while yy >= 1.e-8:
        sol=odeint(king, y_init, [0,x])
        yy = sol[1,0]
        r.append(x * np.sqrt(float(sys.argv[1])))
        psi.append(yy)
        dens.append(rho(yy))
        dx = min(2. * dx, 0.02 * sol[1,0] / abs(sol[1,1]))
        x += dx

    v_max = np.sqrt(2.) * np.sqrt(psi)

    if sys.argv[2] == 'v_max':
        plt.plot(r, v_max)
        plt.ylabel('${\\rm v_{max}}$')
    elif sys.argv[2] == 'rho':
        plt.plot(r, dens/dens[0])
        plt.ylabel('${\\rm \\rho / \\rho_0}$')
    else:
        plt.plot(r, psi)
        plt.ylabel('${\\rm \\Psi}$')

    #plt.xscale('log')
    #plt.yscale('log')

    #plt.xlim([0.1,200])
    #plt.ylim([1.e-6,10])

    plt.xlabel('${\\rm r / r_0}$')

    plt.show()

if __name__ == "__main__":
    main()

