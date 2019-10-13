### Metodo de la biseccion.

import scipy.integrate as spi
import numpy as np
import math

def funcion(x): return np.log(x-1) + math.cos(x-1);


def main():
  a = 1.3;
  b = 2;
  tol = 1e-4;
  po = 0.00000;
  fp = 0;
  i = 1;
  print(" Metodo de la bisección ");
  print(" | n |    Pn    |   f(Pn)   |  [f(Pn)] |");
  while True:
    po = (a+b)/2;
    fp = funcion(po);
    valor_absoluto = abs(fp)
    s = ' | ' + str(i) + ' | ' + str('%.6f'%po) + ' | ' + str('%.6f'%fp) + ' | ' + str('%.6f'%valor_absoluto) + ' | ';
    print (s);
    if abs(fp) <= tol:
      print("\nLa raiz de la funcion es " + repr(po));
      break
    else:
      if (funcion(po)*funcion(a)) < 0:
        b = po;
      if (funcion(po)*funcion(b)) < 0:
        a = po;
    i = i +1


if __name__ == "__main__":

    main()
