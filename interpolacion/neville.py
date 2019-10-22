#Metodo de aproximacion de Neville.

import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray

def neville(xi,xj,Pij_inferior,Pij_superior):
	x = 1.5;
	return ((x-xj)*Pij_inferior - (x-xi)*Pij_superior)/(xi-xj)

def main():
	x0 = 1.0; x1 = 1.3; x2 = 1.6; x3 = 1.9; x4 = 2.2;
	P00 = 0.7651977; P11 = 0.6200860; P22 = 0.4554022;
	P33 = 0.2818186; P44 = 0.1103623;
	#Corre de 0 hasta 4
	#Primera ronda
	P01 = neville(x0,x1,P00,P11);
	P12 = neville(x1,x2,P11,P22);
	P23 = neville(x2,x3,P22,P33);
	P34 = neville(x3,x4,P33,P44);
	#Segunda ronda
	#En este caso se utilizaran los valores
	#obtenidos en la primer ronda, dado que
	#esto es un metodo de iteracion
	P02 = neville(x0,x2,P01,P12);
	P13 = neville(x1,x3,P12,P23);
	P24 = neville(x2,x4,P23,P34);
	# Tercer ronda
	P03 = neville(x0,x3,P02,P13);
	P14 = neville(x1,x4,P13,P24);
	# Ultima ronda. Este sera el valor deseado.
	P04 = neville(x0,x4,P03,P14);


	print("El valor de la aproximacion es: " +str(P04));

if __name__ == "__main__":

    main()


