#	Metodo de interpolacion de Hermite.

import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt

def H(x,xj,L,x0,x1,x2):
	K = Lp(xj,x0,x1,x2)
	return (1 - 2*(x - xj)*K)*L**2

def Hp(x,xj,L):
	return (x - xj)*L**2

def L(x,x0,x1,x2,):
	return (x - x1)*(x - x2)/((x0 - x1)*(x0 - x2))

def Lp(x,x0,x1,x2):
	return (2*x - x2 - x1)/((x0 - x1)*(x0 - x2))

def main():
	# Definimos valores iniciales
	x = 1.5
	x0,x1,x2 = 1.3, 1.6, 1.9
	f1,f2,f3 = 0.6200860, 0.4554022, 0.2818186
	fp1,fp2,fp3 = -0.5220232, -0.5698959, -0.5811571
	
	L20 = L(x,x0,x1,x2);
	L21 = L(x,x1,x0,x2); 
	L22 = L(x,x2,x0,x1); 

	H20 = H(x,x0,L20,x0,x1,x2); 
	H21 = H(x,x1,L21,x1,x0,x2); 
	H22 = H(x,x2,L22,x2,x0,x1);

	Hp20 = Hp(x,x0,L20); 
	Hp21 = Hp(x,x1,L21); 
	Hp22 = Hp(x,x2,L22); 

	Hr = f1*H20 + f2*H21 + f3*H22 + fp1*Hp20 + fp2*Hp21 + fp3*Hp22

	print("el valor: " + str(Hr))

if __name__ == "__main__":
    main()

