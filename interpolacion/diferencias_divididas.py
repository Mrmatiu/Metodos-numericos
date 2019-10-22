#Metodo de diferencias divididas.

import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt

def dif_divididas(x1,x2,fx1,fx2):
	return (fx2-fx1)/(x2-x1)

def newton(p0,p1,p2,p3,p4):
	x0 = 1.0; x1 = 1.3; x2 = 1.6; x3 = 1.9;
	x = 1.5
	return p0 + p1*(x-x0) + p2*(x-x0)*(x-x1) + p3*(x-x0)*(x-x1)*(x-x2) + p4*(x-x0)*(x-x1)*(x-x2)*(x-x3)

def main():
	x0 = 1.0; x1 = 1.3; x2 = 1.6; x3 = 1.9; x4 = 2.2;
	fx0 = 0.7651977; fx1 = 0.6200860; fx2 = 0.4554022;
	fx3 = 0.2818186; fx4 = 0.1103623;
	# primer ronda
	fx0x1 = dif_divididas(x0,x1,fx0,fx1)
	fx1x2 = dif_divididas(x1,x2,fx1,fx2)
	fx2x3 = dif_divididas(x2,x3,fx2,fx3)
	fx3x4 = dif_divididas(x3,x4,fx3,fx4)
	# segunda ronda
	fx0x1x2 = dif_divididas(x0,x2,fx0x1,fx1x2)
	fx1x2x3 = dif_divididas(x1,x3,fx1x2,fx2x3)
	fx2x3x4 = dif_divididas(x2,x4,fx2x3,fx3x4)
	# tercer ronda
	fx0x1x2x3 = dif_divididas(x0,x3,fx0x1x2,fx1x2x3)
	fx1x2x3x4 = dif_divididas(x1,x4,fx1x2x3,fx2x3x4)
	# Ultima ronda, valor deseado
	fx0x1x2x3x4 = dif_divididas(x0,x4,fx0x1x2x3,fx1x2x3x4)
	# Metodo prgresivo de newton
	valor = newton(fx0,fx0x1,fx0x1x2,fx0x1x2x3,fx0x1x2x3x4)
	print("El valor de aproimacion es: "+str(valor))

if __name__ == "__main__":

    main()


