#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:54:42 2021

@author: pi
"""
import numpy as np
import sympy as sp
from sympy import symbols


def serie_potencias_calcular_error_absoluto(fn, a, n, f0):
    # funcion, variable, suma
    f, x, g = sp.symbols('f,x,g')

    f = fn

    g = (sp.diff(f, x, 0).subs(x, a) / sp.factorial(0)) * ((x - a) ** 0)

    conTerminos = 0
    i = 1

    # sumatoria en for dependiendo del número de terminos
    # Se itera en base al número de términos que sean VALIDOS
    while (conTerminos <= n - 1):
        termino_nuevo = (sp.diff(f, x, i).subs(x, a) / sp.factorial(i)) * ((x - a) ** i)
        termino_nuevo_ev = termino_nuevo.evalf(subs={x: f0})
        if (termino_nuevo_ev != 0):
            conTerminos += 1
            g += termino_nuevo

        i += 1

    # y=symbols('y')
    # print(sp.integrate(y**2,(y,0,1)))
    f = sp.integrate(f)
    g = sp.integrate(g)
    val_estimado = g.evalf(subs={x: f0})
    val_real = f.evalf(subs={x: f0})

    error_absoluto = np.abs(val_real - val_estimado)

    print(f'El valor real es igual =  {val_real:.8}')
    print(f'El valor estimado da igual por la serie para x={f0} es igual =  {1 - val_estimado:.8}')
    print(
        f'The absolute error for function {f}, Taylor Serie around a={a}, evaluating x={f0:.5}, with {n} terms is {np.float(error_absoluto):.8}')


# Ejercicio 3
x = symbols('x')
serie_potencias_calcular_error_absoluto(x * sp.cos(x ** 3), 0.4, 10, 1.0)
