# 1) Maior entre dois números
print("1) Maior entre dois números")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é {num1}")
elif num2 > num1:
    print(f"O maior número é {num2}")
else:
    print("Os números são iguais.")
print("-" * 40)

# 2) Crescimento ou decrescimento
print("2) Crescimento ou decrescimento")
percentual = float(input("Digite o percentual de crescimento da produção: "))

if percentual > 0:
    print("Houve crescimento.")
elif percentual < 0:
    print("Houve decrescimento.")
else:
    print("A produção permaneceu constante.")
print("-" * 40)

# 3) Vogal ou consoante
print("3) Vogal ou consoante")
letra = input("Digite uma letra: ").lower()

if letra in "aeiou":
    print("A letra é uma vogal.")
elif letra.isalpha():
    print("A letra é uma consoante.")
else:
    print("Caractere inválido.")
print("-" * 40)

# 4) Valor mais alto e mais baixo entre três anos
print("4) Valor mais alto e mais baixo entre três anos")
preco1 = float(input("Digite o preço do carro no ano 1: "))
preco2 = float(input("Digite o preço do carro no ano 2: "))
preco3 = float(input("Digite o preço do carro no ano 3: "))

maior_preco = max(preco1, preco2, preco3)
menor_preco = min(preco1, preco2, preco3)

print(f"Maior preço: {maior_preco}")
print(f"Menor preço: {menor_preco}")
print("-" * 40)

# 5) Produto mais barato
print("5) Produto mais barato")
produto1 = float(input("Digite o preço do produto 1: "))
produto2 = float(input("Digite o preço do produto 2: "))
produto3 = float(input("Digite o preço do produto 3: "))

if produto1 < produto2 and produto1 < produto3:
    print("Compre o produto 1.")
elif produto2 < produto3:
    print("Compre o produto 2.")
else:
    print("Compre o produto 3.")
print("-" * 40)

# 6) Números em ordem decrescente
print("6) Números em ordem decrescente")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

numeros = [n1, n2, n3]
numeros.sort(reverse=True)

print(f"Números em ordem decrescente: {numeros}")
print("-" * 40)

# 7) Turno de estudo
print("7) Turno de estudo")
turno = input("Em qual turno você estuda? (manhã, tarde ou noite): ").lower()

if turno == "manhã":
    print("Bom Dia!")
elif turno == "tarde":
    print("Boa Tarde!")
elif turno == "noite":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
print("-" * 40)

# 8) Par ou ímpar
print("8) Par ou ímpar")
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
print("-" * 40)

# 9) Inteiro ou decimal
print("9) Inteiro ou decimal")
numero = float(input("Digite um número: "))

if numero == int(numero):
    print("O número é inteiro.")
else:
    print("O número é decimal.")
print("-" * 40)

# 10) Operação e características do número
print("10) Operação e características do número")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha uma operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Divisão por zero não é permitida.")
        resultado = None
else:
    print("Operação inválida.")
    resultado = None

if resultado is not None:
    print(f"Resultado: {resultado}")
    if resultado % 2 == 0:
        print("O resultado é par.")
    else:
        print("O resultado é ímpar.")

    if resultado > 0:
        print("O resultado é positivo.")
    elif resultado < 0:
        print("O resultado é negativo.")

    if resultado == int(resultado):
        print("O resultado é inteiro.")
    else:
        print("O resultado é decimal.")
print("-" * 40)

# 11) Tipos de triângulo
print("11) Tipos de triângulo")
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles.")
    else:
        print("Triângulo Escaleno.")
else:
    print("Os valores fornecidos não formam um triângulo.")
print("-" * 40)

# 12) Combustíveis e descontos
print("12) Combustíveis e descontos")
combustivel = input("Digite o tipo de combustível (E para etanol, D para diesel): ").upper()
litros = float(input("Digite a quantidade de litros: "))

if combustivel == "E":
    preco = 1.70
    desconto = 0.02 if litros <= 15 else 0.04
elif combustivel == "D":
    preco = 2.00
    desconto = 0.03 if litros <= 15 else 0.05
else:
    print("Tipo de combustível inválido.")
    preco = 0
    desconto = 0

valor_desconto = preco * litros * desconto
valor_total = (preco * litros) - valor_desconto

print(f"Valor a pagar: R${valor_total:.2f}")
print("-" * 40)

# 13) Análise de vendas
print("13) Análise de vendas")
vendas_2022 = int(input("Digite a quantidade de vendas em 2022: "))
vendas_2023 = int(input("Digite a quantidade de vendas em 2023: "))

variacao = ((vendas_2023 - vendas_2022) / vendas_2022) * 100

print(f"Variação percentual: {variacao:.2f}%")
if variacao > 20:
    print("Bonificação para o time de vendas.")
elif 2 < variacao <= 20:
    print("Pequena bonificação para o time de vendas.")
elif -10 <= variacao <= 2:
    print("Planejamento de políticas de incentivo às vendas.")
else:
    print("Corte de gastos.")
print("-" * 40)
