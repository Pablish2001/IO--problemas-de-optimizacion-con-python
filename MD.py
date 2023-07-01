#importe de librerias 
import matplotlib.pyplot as plt
import numpy as np

#definir las restrinciones y la funcion objetivo
x = np.linspace(0, 100, 1000)
y1 = 20*np.ones(len(x))
y2 = 10*np.ones(len(x))
y3 = (12-3*x)/4

#graficar la regio factible y la funcion objetivo
plt.plot(y1, x, label= 'X <= 20')
plt.plot(x, y2, label= 'Y <= 10')
plt.plot(x, y3, label= '3X + 4Y >= 12')
plt.fill_between(x,y3,y2, where=(x <= 20),color='grey', alpha = 0.3)
plt.xlim((0, 50))
plt.ylim((0, 50))
plt.xlabel('Unidades de X')
plt.ylabel('Unidades de Y')
plt.title('Problema de programación lineal')
plt.legend()

#encontrar el punto factible
x_opt = 20
y_opt = 10
z_opt = 9000*x_opt + 12000*y_opt
plt.scatter(x_opt, y_opt, color = 'r', label = 'punto optimo ({},{})'.format(x_opt, y_opt))                 
plt.annotate('Z= {}'.format(z_opt),xy=(x_opt,y_opt), xytext=(x_opt+15,y_opt+15),
arrowprops =dict(facecolor = 'red', shrink = 0.05))
plt.legend()
plt.show()
