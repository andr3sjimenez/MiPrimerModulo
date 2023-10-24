# MiPrimerModulo.py

import statistics
import math

def Suma5(*args):
    if len(args) != 5:
        raise ValueError("Proporcione 5 números")
    return sum(args)

def Potencia5(*args):
    if len(args) != 5:
        raise ValueError("Proporcione 5 números")
    return [x ** 2 for x in args]

def Raiz5(*args):
    if len(args) != 5:
        raise ValueError("Proporcione 5 números")
    return [math.sqrt(x) for x in args]

def Varianza5(*args):
    if len(args) != 5:
        raise ValueError("Proporcione 5 números")
    return statistics.variance(args)

def asimetria_curtosis5(*args):
    if len(args) != 5:
        raise ValueError("Proporcione 5 números")
    
    mean = statistics.mean(args)
    variance = statistics.variance(args)
    
    # Cálculo de la asimetría
    skewness = sum((x - mean) ** 3 for x in args) / (len(args) * variance ** (3/2))
    
    # Cálculo de la curtosis
    kurtosis = sum((x - mean) ** 4 for x in args) / (len(args) * variance ** 2) - 3
    
    return skewness, kurtosis
