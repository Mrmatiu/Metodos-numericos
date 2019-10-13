### Metodo modificado de Aitken

import scipy.integrate as spi
import numpy as np
import math
from numpy import ndarray

def funcion_1(x): return math.sqrt(10/(x+4));
def funcion_2(x): return (2-math.exp(x) + x**2)/3;
def funcion_3(x): return (math.sin(x)+math.cos(x))/2;

def main():
  po = 0.5;
  p1 = 0.0;
  p2 = 0.0;
  pñ = 0.0;
  tol = 1e-9;
  i = 1;
  condicion = 1;
  print(" Metodo modificado de Aitken");
  print(" | n |    Pn    |   f(Pn)  |");
  while True:
    p1 = funcion_2(po);
    p2 = funcion_2(p1);
    pñ = po - ((p1 - po)**2)/( po -2*p1 +p2 );
    q = funcion_2(pñ);
    valor_absoluto = abs(pñ - q);
    z = ' | ' + str(i) + ' | ' + str('%.6f'%pñ) +' | ' +str('%.6f'%q)+ ' | ';
    print(z);
    if valor_absoluto < tol:
      condicion == 0;
      print('La raiz es '+str(pñ));
      break
    po = p1;
    p1 = p2;
    i = i+1;


if __name__ == "__main__":

    main()
