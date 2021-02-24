#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:54:42 2021

@author: pi
"""
import numpy as np
import sympy as sp
from sympy import solveset, symbols, Interval

def get_m(function, lower_bound, upper_bound):
    #Reference https://stackoverflow.com/questions/39192643/finding-the-minimum-of-a-function-on-a-closed-interval-with-python
    # Lo cambié por Max, había generado un código anterior a este, pero este cubre casos en que M pudiera no estar en los limites del rango
    zeros = solveset(function, x, domain=Interval(lower_bound, upper_bound))
    assert zeros.is_FiniteSet # If there are infinite solutions the next line will hang.
    ans = [np.abs(np.float(function.evalf(subs= {x:lower_bound}))), np.abs(np.float(function.evalf(subs= {x:upper_bound}))), *[function.evalf(subs= {x:i}) for i in zeros]]
    ans= np.max(ans)
    return(ans)


def serie_potencias_calcular_estimar(fn, a, n, f0):

    #funcion, variable, suma
    f,x,g=sp.symbols('f,x,g')
    
    f=fn
  
    L=sp.plot(sp.integrate(f),(x,-1,1),show=False,legend=True)
    L.label='$f$'
    
    error=10000

    while abs(error) > (10 ** (-4)):
        g=(sp.diff(f,x,0).subs(x,a)/sp.factorial(0))*((x-a)**0)
        conTerminos=0
        i=1
        #sumatoria en for dependiendo del número de terminos
        #Se itera en base al número de términos que sean VALIDOS
        while(conTerminos <= n-1):
            termino_nuevo=sp.diff(f,x,i).subs(x,a)/sp.factorial(i)*((x-a)**i)
            termino_nuevo_ev=termino_nuevo.evalf(subs= {x:f0})
            if(termino_nuevo_ev != 0):
                conTerminos+=1
                g+=termino_nuevo 
            i+=1
        
        g_next_diff = sp.diff(f,x,n+1) 
        
        M=sp.plot(sp.integrate(g),(x,-1,1),show=False,legend=True)
        M[0].label='n={}'.format(n)
        ##color random
        r=lambda: random.randint(0,255)
        color='#%02X%02X%02X'%(r(),r(),r())
        M[0].line_color=color
        L.append(M[0])
        
        g=sp.integrate(g)
        #obtenemos M
        m = get_m(g_next_diff,f0,a)
        #print(m)
        #Calculamos el error absoluto
        error= np.float(((np.float(m))*((np.abs(f0-a))**(n+1)))/np.math.factorial(n+1))
        
        #print(g)
        val_estimado = g.evalf(subs= {x:1.0})
        print(f'El valor estimado da igual por la serie para x=pi/60 es igual =  {val_estimado:.8}')
        print(f'The absolute error for function {f}, Maclaurin Serie around a={a}, evaluating x={f0:.5}, with {n} terms is {np.float(error):.8}')
        print('\n')
        n+=1 
    L.show()            

#Ejercicio 8
x = symbols('x')
serie_potencias_calcular_estimar(x*sp.cos(x**3),0.4,10,1.0)