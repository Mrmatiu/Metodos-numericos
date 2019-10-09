{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "numericos.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Mrmatiu/Metodos-numericos/blob/master/numericos.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "id": "ryeUly6Z7Pwd",
        "colab": {}
      },
      "source": [
        "### Metodo delta^2 de Aitken\n",
        "\n",
        "import scipy.integrate as spi\n",
        "import numpy as np\n",
        "import math  \n",
        "from numpy import ndarray\n",
        "from __future__ import division\n",
        "\n",
        "def fx(x): return math.cos(1/x);\n",
        "def fu(x): return fx(x)-((fx(x+1)-fx(x))*(fx(x+1)-fx(x)))/(fx(x+2)-2*fx(x+1)+fx(x));\n",
        "\n",
        "def main():\n",
        "  i = 1;\n",
        "  p = 0.0;\n",
        "  q = 0.0;\n",
        "  print(\" Metodo delta^2 de Aitken\");\n",
        "  print(\" | n |    Pn    |   ~Pn  |\");\n",
        "  while i<=20:\n",
        "    p = fx(i);\n",
        "    q = fu(i);\n",
        "    z = ' | '+str(i)+ ' | '+str('%.6f'%p)+' | '+str('%.6f'%q)+' | ';\n",
        "    print(z);\n",
        "    i = i+1;\n",
        "    \n",
        "if __name__ == \"__main__\":\n",
        "   \n",
        "    main()\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "id": "nZ-qqJrE7PMa",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 173
        },
        "outputId": "ebeabbd9-53f2-4033-ad66-988c0f52276b"
      },
      "source": [
        "### Metodo delta^2 de Aitken\n",
        "\n",
        "import scipy.integrate as spi\n",
        "import numpy as np\n",
        "import math  \n",
        "from numpy import ndarray\n",
        "from __future__ import division\n",
        "\n",
        "def fx1(x): return (2-math.exp(x)+x**2)/3;\n",
        "def fx2(x): return sqrt(10/(x+4));\n",
        "\n",
        "def main():\n",
        "  tol = 1e-10;\n",
        "  i = 0;\n",
        "  po = 0.5;\n",
        "  p1 = fx1(po);\n",
        "  p2 = fx1(p1);\n",
        "  q = po -(((p1-po)*(p1-po))/(p2-2*p1+po));\n",
        "  qe = fx1(q);\n",
        "  print(\"    Metodo de Steffensen    \\n\");\n",
        "  print(\" | n |      qn     |     g(qn)   |\");\n",
        "  z = ' | '+str(i)+' | '+str('%.9f'%q)+' | '+str('%.9f'%qe)+' | ';\n",
        "  print(z);\n",
        "  q = 0.0\n",
        "  while True:\n",
        "    po = q;\n",
        "    p1 = fx1(po);\n",
        "    p2 = fx1(p1);\n",
        "    q = po -(((p1-po)*(p1-po))/(p2-2*p1+po));\n",
        "    valor = abs(q - fx1(q));\n",
        "    qe = fx1(q);\n",
        "    s = ' | '+str(i+1)+' | '+str('%.9f'%q)+' | '+str('%.9f'%qe)+' | ';\n",
        "    print(s);\n",
        "    if valor < tol:\n",
        "      print(\"\\n El valor de la raiz es \" +str(q));\n",
        "      break\n",
        "    i = i+1;\n",
        "\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "   \n",
        "    main()\n",
        "    \n",
        "\n"
      ],
      "execution_count": 92,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "    Metodo de Steffensen    \n",
            "\n",
            " | n |      qn     |     g(qn)   |\n",
            " | 0 | 0.258684428 | 0.257230877 | \n",
            " | 1 | 0.259504081 | 0.257018431 | \n",
            " | 2 | 0.257530380 | 0.257530261 | \n",
            " | 3 | 0.257530285 | 0.257530285 | \n",
            "\n",
            " El valor de la raiz es 0.257530285439861\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "id": "k4JlVSDw7O0C",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 191
        },
        "outputId": "6df53512-5aac-4d48-b1ef-f33949b4ad6a"
      },
      "source": [
        "### Metodo modificado de Aitken\n",
        "\n",
        "import scipy.integrate as spi\n",
        "import numpy as np\n",
        "import math  \n",
        "from numpy import ndarray\n",
        "from __future__ import division\n",
        "\n",
        "def funcion_1(x): return math.sqrt(10/(x+4));\n",
        "def funcion_2(x): return (2-math.exp(x) + x**2)/3;\n",
        "def funcion_3(x): return (math.sin(x)+math.cos(x))/2;\n",
        "\n",
        "def main():\n",
        "  po = 0.5;\n",
        "  p1 = 0.0;\n",
        "  p2 = 0.0;\n",
        "  pñ = 0.0;\n",
        "  tol = 1e-9;\n",
        "  i = 1;\n",
        "  condicion = 1;\n",
        "  print(\" Metodo modificado de Aitken\");\n",
        "  print(\" | n |    Pn    |   f(Pn)  |\");\n",
        "  while True:\n",
        "    p1 = funcion_2(po);\n",
        "    p2 = funcion_2(p1);\n",
        "    pñ = po - ((p1 - po)**2)/( po -2*p1 +p2 );\n",
        "    q = funcion_2(pñ);\n",
        "    valor_absoluto = abs(pñ - q);\n",
        "    z = ' | ' + str(i) + ' | ' + str('%.6f'%pñ) +' | ' +str('%.6f'%q)+ ' | ';\n",
        "    print(z);\n",
        "    if valor_absoluto < tol:\n",
        "      condicion == 0;\n",
        "      print('La raiz es '+str(pñ));\n",
        "      break\n",
        "    po = p1;\n",
        "    p1 = p2;\n",
        "    i = i+1;\n",
        "\n",
        "  \n",
        "if __name__ == \"__main__\":\n",
        "   \n",
        "    main()\n",
        "    \n"
      ],
      "execution_count": 80,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            " Metodo modificado de Aitken\n",
            " | n |    Pn    |   f(Pn)  |\n",
            " | 1 | 0.258684 | 0.257231 | \n",
            " | 2 | 0.257613 | 0.257509 | \n",
            " | 3 | 0.257536 | 0.257529 | \n",
            " | 4 | 0.257531 | 0.257530 | \n",
            " | 5 | 0.257530 | 0.257530 | \n",
            " | 6 | 0.257530 | 0.257530 | \n",
            " | 7 | 0.257530 | 0.257530 | \n",
            "La raiz es 0.2575302855543379\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "id": "VeASeLNe7NJZ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 156
        },
        "outputId": "65180579-e758-4115-c3c5-c3a49c58c39c"
      },
      "source": [
        "### Metodo de la secante\n",
        "\n",
        "\n",
        "import scipy.integrate as spi\n",
        "import numpy as np\n",
        "import math  \n",
        "from numpy import ndarray\n",
        "\n",
        "def funcion_1(x): return x**3 + 4*x**2 -10;\n",
        "def funcion_2(x): return math.log(x-1) + math.cos(x-1);\n",
        "def funcion_3(x): return np.exp(x) + -x**2 + 2*math.cos(x)-6;\n",
        "\n",
        "def main():\n",
        "  pn_inferior = 1.3;\n",
        "  pn = 1.5;\n",
        "  pn_superior = 0;\n",
        "  tol = 1e-3;\n",
        "  i = 1;\n",
        "  print(\" Metodo de la secante\");\n",
        "  print(\" |  n  |       Pn+1       |    Pn    |   Pn-1  |         f(Pn)         |       |f(Pn)|       |\");\n",
        "  while True:\n",
        "    pn_superior = pn -((pn - pn_inferior)/(funcion_2(pn) - funcion_2(pn_inferior)) )*funcion_2(pn);\n",
        "    fp = funcion_2(pn_superior);\n",
        "    fp_absoluto = abs(fp);\n",
        "    p_abosoluto = abs(pn_superior-pn);\n",
        "    z = ' | ' + str(i) + ' | ' + str('%.6f'%pn_superior) +' | ' + str('%.6f'%pn) + ' | ' +str('%.6f'%pn_inferior)+ ' | ' +str('%.7f'%fp)+ ' | ' + str('%.7f'%fp_absoluto) + '|';\n",
        "    print(z);\n",
        "    if p_abosoluto < tol:\n",
        "      print(' \\n La raiz es ' + str(pn));\n",
        "      break\n",
        "    i = i+1;\n",
        "    pn_inferior = pn;\n",
        "    pn = pn_superior;\n",
        "    \n",
        "    \n",
        "  \n",
        "if __name__ == \"__main__\":\n",
        "   \n",
        "    main()\n",
        "    "
      ],
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            " Metodo de la secante\n",
            " |  n  |       Pn+1       |    Pn    |   Pn-1  |         f(Pn)         |       |f(Pn)|       |\n",
            " | 1 | 1.414825 | 1.500000 | 1.300000 | 0.0352874 | 0.0352874|\n",
            " | 2 | 1.394673 | 1.414825 | 1.500000 | -0.0065762 | 0.0065762|\n",
            " | 3 | 1.397838 | 1.394673 | 1.414825 | 0.0001908 | 0.0001908|\n",
            " | 4 | 1.397749 | 1.397838 | 1.394673 | 0.0000010 | 0.0000010|\n",
            " \n",
            " La raiz es 1.3978382013342763\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V3RbyXCnVszn",
        "colab_type": "code",
        "outputId": "086f5a52-b6d7-4a78-ac55-1ae67dd07462",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 243
        }
      },
      "source": [
        "### Metodo de la biseccion.\n",
        "\n",
        "import scipy.integrate as spi\n",
        "import numpy as np\n",
        "\n",
        "def funcion(x):\n",
        "  p = 0;\n",
        "  #p = np.exp(x) - x**2 + 2*np.cos(x) - 6;\n",
        "  #p = np.log(x-1) + cos(x-1);\n",
        "  p = x**3 + 4*(x**2) - 10;\n",
        "  return p;\n",
        "\n",
        "\n",
        "def main():\n",
        "  a = 1;\n",
        "  b = 2;\n",
        "  tol = 1e-4;\n",
        "  po = 0.00000;\n",
        "  fp = 0;\n",
        "  i = 1;\n",
        "  print(\" Metodo de la bisección \");\n",
        "  print(\" | n |    Pn    |   f(Pn)   |  [f(Pn)] |\");\n",
        "  while True:\n",
        "    po = (a+b)/2;\n",
        "    fp = funcion(po);\n",
        "    valor_absoluto = abs(fp)\n",
        "    s = ' | ' + str(i) + ' | ' + str('%.6f'%po) + ' | ' + str('%.6f'%fp) + ' | ' + str('%.6f'%valor_absoluto) + ' | ';\n",
        "    print (s);\n",
        "    if abs(fp) <= tol:\n",
        "      print(\"\\nLa raiz de la funcion es \" + repr(po));\n",
        "      break\n",
        "    else:\n",
        "      if (funcion(po)*funcion(a)) < 0:\n",
        "        b = po;\n",
        "      if (funcion(po)*funcion(b)) < 0:\n",
        "        a = po;\n",
        "    i = i +1\n",
        "    \n",
        "  \n",
        "if __name__ == \"__main__\":\n",
        "   \n",
        "    main()\n",
        "    \n",
        "    \n",
        "    \n",
        "  \n",
        "\n",
        "     "
      ],
      "execution_count": 73,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            " Metodo de la bisección \n",
            " | n |    Pn    |   f(Pn)   |  [f(Pn)] |\n",
            " | 1 | 1.500000 | 2.375000 | 2.375000 | \n",
            " | 2 | 1.250000 | -1.796875 | 1.796875 | \n",
            " | 3 | 1.375000 | 0.162109 | 0.162109 | \n",
            " | 4 | 1.312500 | -0.848389 | 0.848389 | \n",
            " | 5 | 1.343750 | -0.350983 | 0.350983 | \n",
            " | 6 | 1.359375 | -0.096409 | 0.096409 | \n",
            " | 7 | 1.367188 | 0.032356 | 0.032356 | \n",
            " | 8 | 1.363281 | -0.032150 | 0.032150 | \n",
            " | 9 | 1.365234 | 0.000072 | 0.000072 | \n",
            "\n",
            "La raiz de la funcion es 1.365234375\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "outputId": "4163cfa1-8266-4308-bc2b-671af28b22a8",
        "id": "UsYYgny27MSb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 156
        }
      },
      "source": [
        "### Metodo de iteracion punto fijo.\n",
        "\n",
        "\n",
        "import scipy.integrate as spi\n",
        "import numpy as np\n",
        "import math  \n",
        "from numpy import ndarray\n",
        "\n",
        "def funcion_1(x): return x - (x**3) - 4*(x**2) +10;\n",
        "def funcion_2(x): return math.sqrt((10/x)-4*x);\n",
        "def funcion_3(x): return 0.5*math.sqrt(10-(x**3));\n",
        "def funcion_4(x): return sqrt(10/(4+x));\n",
        "def funcion_5(x): return x - ((x**3) + 4*(x**2) - 10)/(3*(x**2)+8*x);\n",
        "\n",
        "\n",
        "\n",
        "def main():\n",
        "  po = 1.1;\n",
        "  p = 0;\n",
        "  err = 1;\n",
        "  tol = 1e-10;\n",
        "  i = 1;\n",
        "  print(\" Metodo de iteracion de punto fijo\");\n",
        "  print(\" | n |    Pn    |   Pn-1   | [Pn-Pn-1] |\");\n",
        "  s = ' | 0 | ' + str('%.6f'%p) + ' |  -----   | ' + '  ------  | ';  \n",
        "  print (s);\n",
        "  p = funcion_5(po);\n",
        "  while err > tol:\n",
        "    err = abs(p - po);\n",
        "    po = p;\n",
        "    p = funcion_5(po);\n",
        "    z = ' | ' + str(i) + ' | ' + str('%.6f'%p) +' | ' +str('%.6f'%po)+ ' | ' +str('%.7f'%err)+ ' | ';\n",
        "    print(z);\n",
        "    i = i+1;\n",
        "    \n",
        "    \n",
        "  \n",
        "if __name__ == \"__main__\":\n",
        "   \n",
        "    main()\n",
        "    \n",
        " \n"
      ],
      "execution_count": 76,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            " Metodo de iteracion de punto fijo\n",
            " | n |    Pn    |   Pn-1   | [Pn-Pn-1] |\n",
            " | 0 | 0.000000 |  -----   |   ------  | \n",
            " | 1 | 1.366101 | 1.408045 | 0.3080451 | \n",
            " | 2 | 1.365230 | 1.366101 | 0.0419437 | \n",
            " | 3 | 1.365230 | 1.365230 | 0.0008710 | \n",
            " | 4 | 1.365230 | 1.365230 | 0.0000004 | \n",
            " | 5 | 1.365230 | 1.365230 | 0.0000000 | \n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "d0TGVu5kQtRX",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "### Metodo de Newton - Raphson\n",
        "\n",
        "### Metodo de Newton - Raphson\n",
        "\n",
        "import scipy.integrate as spi\n",
        "import numpy as np\n",
        "from numpy import ndarray\n",
        "\n",
        "def fx(x): return np.log(x-1) + np.cos(x-1);\n",
        "def dx(x): return 1/(x-1) - np.sin(x-1);\n",
        "\n",
        "def main():\n",
        "  i = 1;\n",
        "  po = 1.5;\n",
        "  p = 0.0;\n",
        "  tol = 1e-5;\n",
        "  print(\" Metodo de Newton - Raphson \");\n",
        "  print(\" | n |   Pn   |    f(Pn)   |   |f(Pn)|    |\");\n",
        "  while True:\n",
        "    p = po -(fx(po)-(fx(po))/(dx(po)));\n",
        "    #fixed point\n",
        "    fp = fx(p);\n",
        "    valor_absoluto = abs(fp);\n",
        "    if fp < 0:\n",
        "      valor_absoluto = fp*(-1);\n",
        "    z = ' | '+str(i)+' | '+str('%.6f'%p)+' | '+str('%.6f'%fp)+' | '+str('%.6f'%valor_absoluto)+' | ';  \n",
        "    print(z);\n",
        "    if valor_absoluto < tol:\n",
        "      print(\"La raiz de la funcion es: \"+ str(p));\n",
        "      break\n",
        "    i = i+1;\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "   \n",
        "    main()\n",
        "     "
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}