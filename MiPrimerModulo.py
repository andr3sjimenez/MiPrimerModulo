import math

# Función para sumar 5 registros
def sum_5(a, b, c, d, e):
    return a + b + c + d + e

# Función que recibe 5 números y los eleva al cuadrado
def power_5(a, b, c, d, e):
    return (a ** 2, b ** 2, c ** 2, d ** 2, e ** 2)

# Función que recibe 5 números y obtiene la raíz cuadrada de cada uno
def square_5(a, b, c, d, e):
    return (math.sqrt(a), math.sqrt(b), math.sqrt(c), math.sqrt(d), math.sqrt(e))

# Función que recibe 5 números y se obtiene la varianza muestral
def var_5(a, b, c, d, e):
    mean = (a + b + c + d + e) / 5
    variance = ((a - mean) ** 2 + (b - mean) ** 2 + (c - mean) ** 2 + (d - mean) ** 2 + (e - mean) ** 2) / 4
    return variance

# Función que recibe 5 números y se obtiene el coeficiente de asimetría y curtosis
def curto_5(a, b, c, d, e):
    mean = (a + b + c + d + e) / 5
    variance = ((a - mean) ** 2 + (b - mean) ** 2 + (c - mean) ** 2 + (d - mean) ** 2 + (e - mean) ** 2) / 4
    skewness = ((a - mean) ** 3 + (b - mean) ** 3 + (c - mean) ** 3 + (d - mean) ** 3 + (e - mean) ** 3) / (5 * variance ** 1.5)
    kurtosis = ((a - mean) ** 4 + (b - mean) ** 4 + (c - mean) ** 4 + (d - mean) ** 4 + (e - mean) ** 4) / (5 * variance ** 2)
    return skewness, kurtosis

