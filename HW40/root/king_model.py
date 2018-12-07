import Rappture
import numpy as np
import sys
import math
from math import *
from scipy.integrate import odeint
from scipy import optimize
import scipy
from scipy import special

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

    # Get arguments
    io = Rappture.library(sys.argv[1])
    a = float(io.get('input.number(sys.argv[1]).current'))
    b = float(io.get('input.number(sys.argv[2]).current'))
    x = np.linspace(0, a, 100)   # Use rappture to input second number
    y_init=[b, 0]      # Use rappture to input first number
    #formula = io.get('input.string(formula).current')

    sol=odeint(king, y_init, x)
    
    io.put('output.curve(result1).about.label','density vs. r',append=0)
    io.put('output.curve(result1).yaxis.label','density')
    io.put('output.curve(result1).xaxis.label','radius')

    for i in range(5):
        io.put(
               'output.curve(result1).component.xy',
               '%g %g\n' % (x[i],sol[i][0]), append=1
              )


    # Get base string

    my_str_base = 'int_0^root (' + king(y,x) + ') dydx - ' + str(y)

    # Get compute root of \int_0^x f(x') dx' - a

    #root = optimize.brentq(
    #           calc, xmin, xmax, args=(a, formula
    #        )

    #plt.plot(x, sol[:,0])
    #plt.show()
    #my_str = 'Root of f(x) in the range ' + str(xmin) + ' to ' + \
    #         str(xmax) + ' is ' + str(root)
    #io.put('output.string(result1).about.label', 'Root')
    #io.put('output.string(result1).current', my_str)

    Rappture.result(io)


    # Check

    #check = calc(root, a, formula)

    #my_str2 = '\nCheck: ' + my_str_base + ' = ' + str(check[0])

    #print(my_str2 + '\n')

if __name__ == "__main__":
    main()
