import numpy as np
from collections import Counter
def srednia(x):
    return sum(x)/len(x)

def mediana(y):
    y.sort()
    if len(y)%2 == 0:
        Med= (y[int((len(y)/2)-1)]+y[(int(len(y)/2))])/2
    else:
        Med= y[(int((len(y)+1)/2)-1)]
    return Med
    
def dominanta(x):
   c=Counter(x)
   return c.most_common(1)[0][0]
    

def sos(x):
    """suma odchylen sekwencji"""
    c = srednia(x)
    ss = sum((x-c)**2 for x in x)
    return ss

def odch(x, ddof=0):
    """Oblicza odchylenie standardowe populacji
     domyślnie; podaj ddof = 1, aby obliczyć próbkę
     odchylenie standardowe."""
    n = len(x)
    if n < 2:
        raise ValueError('odchylenie standardowe potrzebuje conajmniej dwoch wartosci')
    pvar = sos(x)/(n-ddof)
    return pvar**0.5

def wariancja(x, y=0):
    n = len(x)
    pvar = sos(x)/(n-y)
    return pvar

def skosnosc(x, y=0):
    n = len(x)
    pvar = sos(x)/(n-y)
    return(1/odch(x)**3)*(pvar**2)
    
def kurtoza(x,y=0):
    n = len(x)
    pvar = sos(x)/(n-y)
    return(1/odch(x)**4)*(pvar**4)-3
    

    