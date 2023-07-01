from pulp import *

# Crear el problema de minimización
problema = LpProblem("Problema de optimización", LpMinimize)

# Definir las variables de decisión
X = LpVariable("X", lowBound=0)
Y = LpVariable("Y", lowBound=0)

# Definir la función objetivo
problema += 6*X + 2*Y

# Definir las restricciones
restriccion1 = 0.5*X + 0.2*Y <= 4
restriccion2 = 2*X + 3*Y >= 20
restriccion3 = 1*X + 1*Y == 10

problema += restriccion1
problema += restriccion2
problema += restriccion3

# Resolver el problema
problema.solve()

# Imprimir el resultado
print("Estado de la solución:", LpStatus[problema.status])
print("Valor óptimo de Z:", value(problema.objective))
print("Valor óptimo de X:", value(X))
print("Valor óptimo de Y:", value(Y))
