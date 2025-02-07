    # Coleta e amostragem de dados
nome = str(input('Digite seu nome:')).strip().title()
print(f'Bem vindo {nome}')
idade = int(input('Digite sua idade:'))
print(f'Você tem {idade} anos')
    #Calculadora com operadores
# Soma de dois valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
print(f"A soma dos dois valores é: {valor1 + valor2}")

# Soma de três valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))
print(f"A soma dos três valores é: {valor1 + valor2 + valor3}")

# Subtração de dois valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
print(f"A subtração do primeiro pelo segundo valor é: {valor1 - valor2}")

# Multiplicação de dois valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
print(f"A multiplicação dos dois valores é: {valor1 * valor2}")

# Divisão de dois valores
valor1 = float(input("Digite o numerador: "))
valor2 = float(input("Digite o denominador (não pode ser 0): "))
if valor2 != 0:
    print(f"A divisão entre os dois valores é: {valor1 / valor2}")
else:
    print("Erro: o denominador não pode ser 0.")

# Exponenciação
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
print(f"O resultado da exponenciação é: {base ** expoente}")

# Divisão inteira
valor1 = float(input("Digite o numerador: "))
valor2 = float(input("Digite o denominador (não pode ser 0): "))
if valor2 != 0:
    print(f"A divisão inteira entre os dois valores é: {valor1 // valor2}")
else:
    print("Erro: o denominador não pode ser 0.")

# Resto da divisão
valor1 = float(input("Digite o numerador: "))
valor2 = float(input("Digite o denominador (não pode ser 0): "))
if valor2 != 0:
    print(f"O resto da divisão entre os dois valores é: {valor1 % valor2}")
else:
    print("Erro: o denominador não pode ser 0.")

# Média de três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media:.2f}")

# Média ponderada
num1, peso1 = 5, 1
num2, peso2 = 12, 2
num3, peso3 = 20, 3
num4, peso4 = 15, 4
media_ponderada = (num1 * peso1 + num2 * peso2 + num3 * peso3 + num4 * peso4) / (peso1 + peso2 + peso3 + peso4)
#ou
media_ponderada = (5*1 + 12*2 + 20*3 + 15*4) / (1+2+3+4)
print(f"A média ponderada dos números é: {media_ponderada:.2f}")

#Editando texto
# Atribuindo uma string a uma variável e imprimindo
frase = "Esta é uma frase de exemplo."
print("# Esta frase demonstra o uso de strings em Python.\n" + frase + "\n")

# Imprimindo uma frase fixa
frase = "Exemplo de frase fixa."
print("# Esta frase demonstra como exibir uma string fixa em Python.\n" + frase + "\n")

# Imprimindo uma frase em letras maiúsculas
frase = "Exemplo de frase fixa."
print("# Esta frase demonstra como converter uma string para letras maiúsculas.\n" + frase.upper() + "\n")

# Imprimindo uma frase em letras minúsculas
frase = "Exemplo de frase fixa."
print("# Esta frase demonstra como converter uma string para letras minúsculas.\n" + frase.lower() + "\n")

# Imprimindo uma frase sem espaços no início e fim
frase = "   Esta é uma frase de exemplo.   "
print("# Esta frase demonstra como remover espaços em branco no início e no fim.\n" + frase.strip() + "\n")

# Imprimindo uma frase fixa sem espaços no início e fim
frase = "   Exemplo de frase fixa.   "
print("# Esta frase demonstra como exibir uma string fixa sem espaços no início e fim.\n" + frase.strip() + "\n")

# Imprimindo uma frase fixa sem espaços no início e fim, em letras minúsculas
frase = "   Exemplo de frase fixa.   "
print("# Esta frase demonstra como remover espaços e converter para letras minúsculas.\n" + frase.strip().lower() + "\n")

# Substituindo todas as vogais "e" por "f"
frase = "Exemplo de frase fixa."
print("# Esta frase demonstra como substituir todas as vogais 'e' por 'f'.\n" + frase.replace("e", "f").replace("E", "F") + "\n")

# Substituindo todas as vogais "a" por "@"
frase = "Exemplo de frase fixa."
print("# Esta frase demonstra como substituir todas as vogais 'a' por '@'.\n" + frase.replace("a", "@").replace("A", "@") + "\n")

# Substituindo todas as consoantes "s" por "$"
frase = "Exemplo de frase fixa."
print("# Esta frase demonstra como substituir todas as consoantes 's' por '$'.\n" + frase.replace("s", chr(36)).replace("S", chr(36)) + "\n")
