### Metodo de la secante

import scipy.integrate as spi
import numpy as np
import math  
from numpy import ndarray

def funcion_1(x): return x**3 + 4*x**2 -10;
def funcion_2(x): return math.log(x-1) + math.cos(x-1);
def funcion_3(x): return np.exp(x) + -x**2 + 2*math.cos(x)-6;

def main():
  pn_inferior = 1.3;
  pn = 1.5;
  pn_superior = 0;
  tol = 1e-3;
  i = 1;
  print(" Metodo de la secante");
  print(" | n |   Pn+1   |    Pn    |   Pn-1   |   f(Pn)   | |f(Pn)|  |");
  while True:
    pn_superior = pn -((pn - pn_inferior)/(funcion_2(pn) - funcion_2(pn_inferior)) )*funcion_2(pn);
    fp = funcion_2(pn_superior);
    fp_absoluto = abs(fp);
    p_abosoluto = abs(pn_superior-pn);
    z = ' | ' + str(i) + ' | ' + str('%.6f'%pn_superior) +' | ' + str('%.6f'%pn) + ' | ' +str('%.6f'%pn_inferior)+ ' | ' +str('%.7f'%fp)+ ' | ' + str('%.7f'%fp_absoluto) + '|';
    print(z);
    if p_abosoluto < tol:
      print(' \n La raiz es ' + str(pn));
      break
    i = i+1;
    pn_inferior = pn;
    pn = pn_superior;
    
    
  
if __name__ == "__main__":
   
    main()