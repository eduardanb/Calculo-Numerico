import math

def calcular_seno(x, preman=1e-10):
    i = 3  
    fact = 1  
    seno = x 
    sinal = -1  
    termo = x  

    # O loop continua enquanto o termo for maior que o valor de preman
    while abs(termo) > preman:
        fact *= i * (i - 1)  # Calcula o fatorial de forma acumulada
        termo = sinal * (x**i) / fact  # Calcula o próximo termo da série
        seno += termo  # Adiciona o termo ao valor de seno
        sinal = -sinal  # Alterna o sinal para o próximo termo
        i += 2  # Aumenta i para os próximos termos da série (potências ímpares)

    return seno  

x = math.radians(30)  # Converte 30 graus para radianos
resultado = calcular_seno(x)
print("Seno aproximado:", resultado)
print("Seno real:", math.sin(x))  # Seno real com math.sin
