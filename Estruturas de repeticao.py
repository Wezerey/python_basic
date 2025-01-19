# 1. Números entre dois inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    num1, num2 = num2, num1  # Garantir que num1 seja menor

for i in range(num1 + 1, num2):
    print(i)

# 2. Crescimento das bactérias
a = 4
b = 10
dias = 0

while a < b:
    a += a * 0.03
    b += b * 0.015
    dias += 1

print(f"A colônia A levará {dias} dias para ultrapassar ou igualar a colônia B.")

# 3. Verificação de notas válidas
avaliacoes = []

while len(avaliacoes) < 15:
    nota = float(input(f"Digite a {len(avaliacoes) + 1}ª nota (0 a 5): "))
    if 0 <= nota <= 5:
        avaliacoes.append(nota)
    else:
        print("Nota inválida. Digite um valor entre 0 e 5.")

print("Notas válidas registradas:", avaliacoes)

# 4. Média de temperaturas
temperaturas = []
while True:
    temp = float(input("Digite a temperatura em Celsius (-273 para encerrar): "))
    if temp == -273:
        break
    temperaturas.append(temp)

if temperaturas:
    media = sum(temperaturas) / len(temperaturas)
    print(f"A média das temperaturas é: {media:.2f}°C")
else:
    print("Nenhuma temperatura foi informada.")

# 5. Fatorial de um número
num = int(input("Digite um número inteiro: "))
fatorial = 1

if num < 0:
    print("Fatorial não definido para números negativos.")
else:
    for i in range(1, num + 1):
        fatorial *= i
    print(f"O fatorial de {num} é {fatorial}.")

# 6. Tabuada de um número
num = int(input("Digite um número inteiro para ver a tabuada: "))
print(f"Tabuada do {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 7. Verificação de número primo
num = int(input("Digite um número inteiro: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} não é um número primo.")
            break
    else:
        print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")

# 8. Distribuição de idades
intervalos = [0, 0, 0, 0]

while True:
    idade = int(input("Digite a idade (número negativo para encerrar): "))
    if idade < 0:
        break
    elif 0 <= idade <= 25:
        intervalos[0] += 1
    elif 26 <= idade <= 50:
        intervalos[1] += 1
    elif 51 <= idade <= 75:
        intervalos[2] += 1
    elif 76 <= idade <= 100:
        intervalos[3] += 1

print(f"Distribuição de idades:")
print(f"[0-25]: {intervalos[0]}")
print(f"[26-50]: {intervalos[1]}")
print(f"[51-75]: {intervalos[2]}")
print(f"[76-100]: {intervalos[3]}")

# 9. Votação para gerência
votos = [0] * 7

for i in range(1, 21):
    voto = int(input(f"Colaborador {i}, vote no candidato (1-4), nulo (5) ou branco (6): "))
    if 1 <= voto <= 6:
        votos[voto] += 1
    else:
        print("Voto inválido. Tente novamente.")
        i -= 1

print("Resultado da votação:")
for i in range(1, 5):
    print(f"Candidato {i}: {votos[i]} votos")
print(f"Votos nulos: {votos[5]}")
print(f"Votos em branco: {votos[6]}")

vencedor = votos.index(max(votos[1:5]))
print(f"O vencedor é o candidato {vencedor} com {votos[vencedor]} votos.")
