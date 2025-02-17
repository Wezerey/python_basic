'''
    a tupla serve para trabalhar com dados sensiveis, que nao podem ser modificados.
'''
from random import randint
estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]
def gera_codigo():
    return f"{randint(0, 999)}"
codigo_estudante = []
for i in range(len(estudantes)):
    codigo_estudante.append([estudantes[i], estudantes[i][0] + gera_codigo()])
print(codigo_estudante)