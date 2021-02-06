# -*- coding: utf-8 -*-
"""
Spyder Editor

Adrián Homero Moreno García

Coded in Raspberry PI 4
"""

from sympy import *
import numpy as np

#Permite utilizar formulas

#Simbolos para las formulas
#usalas como variables simbolicas

def rapshon(fn,x0,precision):

        
    #f(x)
    f=fn
    
    #f'(X)
    fd=f.diff(x,1) #sobre que variable, respecto a x .. primera derivada con respecto a
    #derivative.evalf(subs= {x:0})

    #Contador de iteraciones
    i=0
    
    
    error=10000
    
    while abs(error) > precision:
        i+=1
        y=f.subs(x,x0)#substituyeme x por 3
        yd=fd.subs(x,x0)
        
        #Calcular nueva X
        new_val = x0-y.evalf()/yd.evalf()
        x0=new_val
        
        error=np.float(f.evalf(subs= {x:x0}))
        
        print(f'The {i} iteration x0 is {x0:.10} and f(xn) is {np.float(error):.2}')

x=symbols('x')

print('Rapshon for ((x**3)-(2*(x**2))-5)=0')
rapshon(((x**3)-(2*(x**2))-5),2,10 ** (-4))

print('\n Rapshon for cos(x)-x=0')
rapshon(cos(x)-x,-2,10 ** (-4))

print('\n Rapshon for 0.2*sen(x)-x+0.8=0')
rapshon(0.2*sin(x)-x+0.8,-1,10 ** (-4))

print('\n Rapshon for ln(x-1)+cos(x-1)=0')
rapshon(ln(x-1)+cos(x-1),1.02,10 ** (-4))

print('\n Rapshon for (3*(x^2)-exp(x))=0 ,, Primera solución')
rapshon((3*(x**2)-exp(x)),-4,10 ** (-4))
print('\n Rapshon for (3*(x^2)-exp(x))=0 ,, Segunda solución')
rapshon((3*(x**2)-exp(x)),3,10 ** (-4))
print('\n Rapshon for (3*(x^2)-exp(x))=0 ,, Tercera solución')
rapshon((3*(x**2)-exp(x)),0.5,10 ** (-4))


print('\n Rapshon for (x^2)-5=0 ..this for sqrt(5) ,, Primera solución')
rapshon((x**2)-5,2,10 ** (-4))
print('\n Rapshon for (x^2)-5=0 ..this for sqrt(5) ,, Segunda solución')
rapshon((x**2)-5,-3,10 ** (-4))

print('\n Rapshon for ln((x^2)+1)-(e^(0.4*x))*cos(pi*x)=0')
rapshon(ln((x**2)+1)-(exp(0.4*x))*cos(pi*x),1,10 ** (-6))




