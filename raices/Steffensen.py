### Metodo de Stefrensen

import scipy.integrate as spi
import numpy as np
import math
from numpy import ndarray

def fx1(x): return (2-math.exp(x)+x**2)/3;
def fx2(x): return sqrt(10/(x+4));

def main():
  tol = 1e-10;
  i = 0;
  po = 0.5;
  p1 = fx1(po);
  p2 = fx1(p1);
  q = po -(((p1-po)*(p1-po))/(p2-2*p1+po));
  qe = fx1(q);
  print("    Metodo de Steffensen    \n");
  print(" | n |      qn     |     g(qn)   |");
  z = ' | '+str(i)+' | '+str('%.9f'%q)+' | '+str('%.9f'%qe)+' | ';
  print(z);
  q = 0.0
  while True:
    po = q;
    p1 = fx1(po);
    p2 = fx1(p1);
    q = po -(((p1-po)*(p1-po))/(p2-2*p1+po));
    valor = abs(q - fx1(q));
    qe = fx1(q);
    s = ' | '+str(i+1)+' | '+str('%.9f'%q)+' | '+str('%.9f'%qe)+' | ';
    print(s);
    if valor < tol:
      print("\n El valor de la raiz es " +str(q));
      break
    i = i+1;



if __name__ == "__main__":

    main()

