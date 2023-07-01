#importamos las bibliotecas necesarias
import numpy as np
from scipy.optimize import linprog 

#definir la funcion objetivo y las restrincciones en forma de matrices

c = np.array([110,150])
A = np.array([[4,6],[20,10]])
b = np.array([480,1500])

#resolvemos el problema  utilizando el metodo simplex a travez de la funcion linprog
resultado = linprog(-c, A_ub=A, b_ub=b, method='simplex')

#imprimir el resultado

print("status:", resultado.message)
print("solucion optima:")
print("X =",round(resultado.x[0],2))
print("Y =",round(resultado.x[1],2))
print("valor optimo de la funcion objetivo: Z =", round(-resultado.fun,2))