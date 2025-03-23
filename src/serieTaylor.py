import math

def calcular_seno(x, preman=1e-10):
    i = 3
    fact = 1
    seno = x  # O primeiro termo da série é x
    sinal = -1  
    termo = x  

    while abs(termo) > preman:  
        fact *= i * (i - 1)  
        termo = sinal * (x**i) / fact  
        seno += termo  
        sinal = -sinal  
        i += 2  

    return seno

# Teste com um valor de x
x = math.radians(30)  # Converte graus para radianos
resultado = calcular_seno(x)
print("Seno aproximado:", resultado)
print("Seno real:", math.sin(x))
