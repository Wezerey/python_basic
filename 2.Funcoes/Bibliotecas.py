# 1. instalar bilbioteca vercionadas
    #pip install matplotlib==3.7.1
# 2. Importar biblioteca numpy como np
import numpy as np
# 3. Selecionar numero aleatorio dentro de uma lista
from random import choice,randrange
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
num1 = choice(lista)
print(num1)
# 4. Escolha um numero aleatorio menor que 100
from random import randrange
num2 = randrange(100)
print(num2)
# 5. Solicite 2 numeros e exiba a potencia
from math import pow
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
result = pow(num3, num4)
print(f"{result:0.0f}")
# 6. Solicite um numero de participantes, e exiba o numero de sorteio
from random import randrange
participantes = int(input("Digite o número de participantes: "))
print(f"O número sorteado foi {randrange(1, participantes + 1)}.")
# 7. gere um token par de 1000 a 9998
from random import randrange
nome1 = "João"
token = randrange(1000, 9998, 2)
print(f"Olá, {nome1}, o seu token de acesso é {token}! Seja bem-vindo(a)!")
# 8. Selecionar 3 itens aleatorios de uma lista
from random import sample
frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
print(f" sua salada de frutas terá: {sample(frutas, 3)}")
# 9. Raiz quadrada de uma lista
from math import sqrt
numeros = [2, 8, 15, 23, 91, 112, 256]
for numero in numeros:
    raiz = sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz:0.2f}")
    print(f"{raiz} É um numero inteiro"if raiz % 2 == 0 else f"{raiz:0.1f} Nao é um numero inteiro")

# 10. Area de um circulo  
from math import pi, pow
raio = float(input("Digite o raio da área circular em metros: "))
area = pi*pow(raio,2)
valor = area * 25.00
print(f"Você precisará pagar R$ {round(valor,2)} por uma área de {round(area,2)} metros de grama")