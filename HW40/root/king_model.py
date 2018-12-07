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
    
    x = 0.0001
    dx = 0.0001
    psi0 = float(io.get('input.number(psi0).current'))
    y_init =[psi0,0]

    r = []
    psi = []
    dens = []
    yy = 1
    while yy >= 1.e-8:
        sol=odeint(king, y_init, [0,x])
        yy = sol[1,0]
        r.append(x)
        psi.append(yy)
        dens.append(rho(yy))
        dx = min(2. * dx, 0.02 * sol[1,0] / abs(sol[1,1]))
        x += dx

        v_max = np.sqrt(2.) * np.sqrt(psi)

    
    for i in range(len(r)):
        io.put(
                'output.curve(result1).component.xy',
                '%g %g\n'%(r[i],dens[i]), append=1
                )
        
    io.put('output.curve(result1).about.label','density vs. r',append=0)
    io.put('output.curve(result1).yaxis.label','density')
    io.put('output.curve(result1).xaxis.label','radius')
        
        
    for i in range(len(r)):
        io.put(
                'output.curve(result2).component.xy',
                '%g %g\n'%(r[i],v_max[i]), append=1
              )
        
    io.put('output.curve(result2).about.label','v_max vs. r',append=0)
    io.put('output.curve(result2).yaxis.label','v_max')
    io.put('output.curve(result2).xaxis.label','radius')
        
    for i in range(len(r)):
        io.put(
                'output.curve(result3).component.xy',
                '%g %g\n'%(r[i],psi[i]), append=1
        )

    io.put('output.curve(result3).about.label','psi vs. r',append=0)
    io.put('output.curve(result3).yaxis.label','psi')
    io.put('output.curve(result3).xaxis.label','radius')


    Rappture.result(io)

if __name__ == "__main__":
    main()
