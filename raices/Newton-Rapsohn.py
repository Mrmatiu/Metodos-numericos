import scipy.integrate as spi
import numpy as np
from numpy import ndarray


#El metodos mas eficaz cuando la funcion es facil de derivar.

def fx(x): return np.log(x-1) + np.cos(x-1);
def dx(x): return 1/(x-1) - np.sin(x-1);

def main():
  i = 1;
  po = 1.5;
  p = 0.0;
  tol = 1e-5;
  print(" Metodo de Newton - Raphson ");
  print(" | n |    Pn    |   f(Pn)   |  |f(Pn)| |");
  while True:
    p = po -(fx(po)/(dx(po)));
    #fixed point
    fp = fx(p);
    valor_absoluto = abs(fp);
    if fp < 0:
      valor_absoluto = fp*(-1);
    z = ' | '+str(i)+' | '+str('%.6f'%p)+' | '+str('%.6f'%fp)+' | '+str('%.6f'%valor_absoluto)+' | ';  
    print(z);
    if valor_absoluto < tol:
      print("La raiz de la funcion es: "+ str(p));
      break
    i = i+1;
    po = p;

if __name__ == "__main__":
   
    main()