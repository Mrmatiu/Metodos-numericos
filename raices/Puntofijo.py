### Metodo de iteracion punto fijo.


import scipy.integrate as spi
import numpy as np
import math
from numpy import ndarray

def funcion_1(x): return x - (x**3) - 4*(x**2) +10;
def funcion_2(x): return math.sqrt((10/x)-4*x);
def funcion_3(x): return 0.5*math.sqrt(10-(x**3));
def funcion_4(x): return math.sqrt(10/(4+x));
def funcion_5(x): return x - ((x**3) + 4*(x**2) - 10)/(3*(x**2)+8*x);


def main():
  po = 1.1;
  p = 0;
  err = 1;
  tol = 1e-10;
  i = 1;
  print(" Metodo de iteracion de punto fijo");
  print(" | n |    Pn    |   Pn-1   | [Pn-Pn-1] |");
  s = ' | 0 | ' + str('%.6f'%p) + ' |  -----   | ' + '  ------  | ';
  print (s);
  p = funcion_5(po);
  while err > tol:
    err = abs(p - po);
    po = p;
    p = funcion_5(po);
    z = ' | ' + str(i) + ' | ' + str('%.6f'%p) +' | ' +str('%.6f'%po)+ ' | ' +str('%.7f'%err)+ ' | ';
    print(z);
    i = i+1;
  segundo_main();

def segundo_main():
  po = 1.1;
  p = 0;
  err = 1;
  tol = 1e-10;
  i = 1;
  print("\n Metodo de iteracion de punto fijo");
  print("  Segunda funcion");
  print(" | n |    Pn    |   Pn-1   | [Pn-Pn-1] |");
  s = ' | 0 | ' + str('%.6f'%p) + ' |  -----   | ' + '  ------  | ';
  print (s);
  p = funcion_4(po);
  while err > tol:
    err = abs(p - po);
    po = p;
    p = funcion_4(po);
    z = ' | ' + str(i) + ' | ' + str('%.6f'%p) +' | ' +str('%.6f'%po)+ ' | ' +str('%.7f'%err)+ ' | ';
    print(z);
    i = i+1;
  tercer_main();

def tercer_main():
  po = 1.1;
  p = 0;
  err = 1;
  tol = 1e-10;
  i = 1;
  print("\n Metodo de iteracion de punto fijo");
  print("  Tercer funcion");
  print(" | n |    Pn    |   Pn-1   | [Pn-Pn-1] |");
  s = ' | 0 | ' + str('%.6f'%p) + ' |  -----   | ' + '  ------  | ';
  print (s);
  p = funcion_3(po);
  while err > tol:
    err = abs(p - po);
    po = p;
    p = funcion_3(po);
    z = ' | ' + str(i) + ' | ' + str('%.6f'%p) +' | ' +str('%.6f'%po)+ ' | ' +str('%.7f'%err)+ ' | ';
    print(z);
    i = i+1;

if __name__ == "__main__":

    main()
