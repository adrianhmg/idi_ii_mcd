#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:21:14 2021

@author: pi
"""

import numpy as np
import sympy as sp
from numpy import linalg as LA
from sympy import *

def rapshon(variables,funciones,vectorinicial,precision):

    n= len(variables)    

    #Matriz en formato lista, para que encuentres Jaccobiano etc
    #Vector A
    A=sp.Matrix(funciones)
    V=sp.Matrix(variables)
    
    
    #Jaccobiano, hoy la compu del profe amaneció lenta
    J=A.jacobian(V)

    J_inv=J.inv()

    multiplyJinv_A= J_inv*A
    
    
    i=0
    #Es solo un número para inicializar la variable, siempre esperamos números pequeños , por eso puse un número grande
    error=10000
    
    while abs(error) > precision:
        pairssymbols =[(variables[i],vectorinicial[i]) for i in range(n)]
        
        i+=1
        
        N=V.subs(pairssymbols)
        
        #print(N)
        
        #Calculamos delta xi
        delta_xi=N-multiplyJinv_A.subs(pairssymbols)
        #print(delta_xi)
        delta_xi=[np.float(elem.evalf()) for elem in delta_xi]
         
        
        #Aux dict    
        pairssymbols_delta_xi= {variables[i]:delta_xi[i] for i in range(n)}
        error =[np.float(fn.evalf(subs=pairssymbols_delta_xi)) for fn in funciones]
            
        error=abs(LA.norm(error,np.inf))
            
        formatted_list=['%.5f' % elem for elem in delta_xi]
        
        #Aux dict for print    
        print(f'The {i} iteration delta_xi is {formatted_list} and f(xn) is {np.float(error):.2}')
            
        vectorinicial=delta_xi


x,y=sp.symbols('x,y')


print('\n Rapshon for x²+y=1,x-2y²=0 ,, Primera solución')
rapshon([x,y],[((x**2)+y-1),(x-2*(y**2))],[2,2],10 ** (-4))
print('\n Rapshon for x²+y=1,x-2y²=0 ,, Segunda solución')
rapshon([x,y],[((x**2)+y-1),(x-2*(y**2))],[2,-2],10 ** (-4))

print('\n Rapshon for x²-10x+y²=-5,xy²+x-10y=-8 ,, Primera solución')
rapshon([x,y],[((x**2)-10*x+(y**2)+5),((x*(y**2))+x-10*y+8)],[2,2],10 ** (-4))
print('\n Rapshon for x²-10x+y²=-5,xy²+x-10y=-8 ,, Segunda solución')
rapshon([x,y],[((x**2)-10*x+(y**2)+5),((x*(y**2))+x-10*y+8)],[0.5,0.5],10 ** (-4))

print('\n Rapshon for x*sin(y)=1,x²+y²=4 ,, Primera solución')
rapshon([x,y],[(x*(sin(y))-1),((x**2)+(y**2)-4)],[1,2],10 ** (-4))
print('\n Rapshon for x*sin(y)=1,x²+y²=4 ,, Segunda solución')
rapshon([x,y],[(x*(sin(y))-1),((x**2)+(y**2)-4)],[2,1],10 ** (-4))
print('\n Rapshon for x*sin(y)=1,x²+y²=4 ,, Tercera solución')
rapshon([x,y],[(x*(sin(y))-1),((x**2)+(y**2)-4)],[1,-2],10 ** (-4))
print('\n Rapshon for x*sin(y)=1,x²+y²=4 ,, Cuarta solución')
rapshon([x,y],[(x*(sin(y))-1),((x**2)+(y**2)-4)],[-2,1],10 ** (-4))

print('\n Rapshon for y²*ln(x)=3,y=x² ,, Primera solución')
rapshon([x,y],[((y**2)*ln(x)-3),(y-(x**2))],[2,2],10 ** (-4))


x,y,z=sp.symbols('x,y,z')

print('\n Rapshon for x+y-z=-2,x²+y=0,z-y²=1 ,, Primera solución')
rapshon([x,y,z],[(x+y-z+2),((x**2)+y),(z-(y**2))],[2,-2,-2],10 ** (-4))
print('\n Rapshon for x+y-z=-2,x²+y=0,z-y²=1 ,, Segunda solución')
rapshon([x,y,z],[(x+y-z+2),((x**2)+y),(z-(y**2))],[-2,-2,2],10 ** (-4))
