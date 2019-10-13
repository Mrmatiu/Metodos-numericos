
#Interpolacion de polinomios de Lagrange.

# Los polinomios lagrange lo que haces es usar un polinomio de X grado que pase por siertos puntos 
# en forma de cruva. Normalmente estos puntos son (grado x -1).
import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray

#def Interpolacion(x1,x2.x3): return (((x-x2)*(x-x3))/((x1-x2)*(x1-x3)))*fx(x0) + (((x-x1)*(x-x3))/((x2-x1)*(x2-x3)))*fx(x0) + (((x-x1)*(x-x3))/((x3-x1)*(x3-x1)))*fx(x0);

# En la siguiente funcion se ve el calculo para el polinmio de Lagrange
# de segundo orden. Esto es porque tenemos tres puntos.
def fx(x): return 1/x

def calculo(x):
	x1 = 2; x2 = 2.5; x3 = 4;
	fx0 = 0.5; fx1 = 0.4; fx2 = 0.25;
	return (((x-x2)*(x-x3))/((x1-x2)*(x1-x3)))*fx0 + (((x-x1)*(x-x3))/((x2-x1)*(x2-x3)))*fx1 + (((x-x1)*(x-x3))/((x3-x1)*(x3-x1)))*fx2

# Vectorizamos la funcion.
vec_calculo = np.vectorize(calculo);
vec_fx = np.vectorize(fx);
		
# Dado que el problema tiene un intervalo en xE[1,5]
rango = np.arange(1.0,5.0,0.05,float);

# Insertamos nuestro rango de valores dentro de la funcion.
calculos = vec_calculo(rango);
funcion = vec_fx(rango);

# Graficamos las funciones.
plt.plot(rango,calculos,'b', label = 'P2(x)')
plt.plot(rango,funcion,'k', label = 'f(x)')
# Graficamos los puntos.
plt.plot([2], [0.5], marker='o', markersize=5, color="red", label='P2(x) vs f(x)')
plt.plot([2.5], [0.4], marker='o', markersize=5, color="red")
plt.plot([4], [0.25], marker='o', markersize=5, color="red")

plt.ylabel(' X')
plt.legend()
plt.grid(True)
plt.show()

