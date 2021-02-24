#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:04:13 2021

@author: pi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:54:42 2021

@author: pi
"""
import random
import numpy as np
import sympy as sp
    

def serie_potencias_graficar(fn, a, ns, f0):

    #funcion, variable, suma
    f,x,g=sp.symbols('f,x,g')
    
    f=fn


    L=sp.plot(f,(x,-1,1),ylim=(0.5,-6),show=False,legend=True)
    L.label='$f$'
    
    for n in ns:
        g=sp.diff(f,x,0).subs(x,a)/sp.factorial(0)*((x-a)**0)
        conTerminos=0
        i=1
        #sumatoria en for dependiendo del número de terminos
        #Se itera en base al número de términos que sean VALIDOS
        while(conTerminos <= n-1):
            termino_nuevo=sp.diff(f,x,i).subs(x,a)/sp.factorial(i)*((x-a)**i)
            termino_nuevo_ev=termino_nuevo.evalf(subs= {x:f0})
            #print(termino_nuevo_ev)
            if(termino_nuevo_ev != 0):
                conTerminos+=1
                g+=termino_nuevo 
            i+=1
    
        
    
        M=sp.plot(g,(x,-1,1),ylim=(0.5,-6),show=False,legend=True)
        M[0].label='n={}'.format(n)
        ##color random
        r=lambda: random.randint(0,255)
        color='#%02X%02X%02X'%(r(),r(),r())
        M[0].line_color=color
        
        L.append(M[0])
        
    L.show()

#Ejercicio 6
x = symbols('x')
serie_potencias_graficar((1/((x-1)*(x+1))),0,[20],1)



    