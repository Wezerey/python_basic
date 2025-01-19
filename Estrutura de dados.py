# 1. Cálculo da média de gastos
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
media_gastos = sum(gastos) / len(gastos)
print(f"A média de gastos é: R${media_gastos:.2f}")

# 2. Compras acima de R$3000 e porcentagem
compras_acima_3000 = [gasto for gasto in gastos if gasto > 3000]
porcentagem = (len(compras_acima_3000) / len(gastos)) * 100
print(f"{len(compras_acima_3000)} compras foram acima de R$3000, representando {porcentagem:.2f}% do total.")

# 3. Lista de 5 números inteiros
numeros = [int(input(f"Digite o número {i + 1}: ")) for i in range(5)]
print("Lista de números:", numeros)

# 4. Lista em ordem inversa
numeros = [int(input(f"Digite o número {i + 1}: ")) for i in range(5)]
print("Lista em ordem inversa:", numeros[::-1])

# 5. Lista de números primos até N
n = int(input("Digite um número: "))
primos = []
for i in range(2, n + 1):
    if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
        primos.append(i)
print("Números primos:", primos)

# 6. Validação de data
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
valida = False

if 1 <= mes <= 12:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        valida = 1 <= dia <= 31
    elif mes in [4, 6, 9, 11]:
        valida = 1 <= dia <= 30
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            valida = 1 <= dia <= 29
        else:
            valida = 1 <= dia <= 28

print("Data válida" if valida else "Data inválida")

# 7. Crescimento percentual de bactérias
bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
crescimento = [100 * (bacterias[i] - bacterias[i - 1]) / bacterias[i - 1] for i in range(1, len(bacterias))]
print("Crescimento percentual por dia:", crescimento)

# 8. Separação de produtos doces e amargos
ids = [int(input(f"Digite o ID do produto {i + 1}: ")) for i in range(10)]
doces = len([id for id in ids if id % 2 == 0])
amargos = len(ids) - doces
print(f"Produtos doces: {doces}, Produtos amargos: {amargos}")

# 9. Correção de prova
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
respostas = [input(f"Resposta da questão {i + 1}: ").strip().upper() for i in range(10)]
nota = sum(1 for i in range(10) if respostas[i] == gabarito[i])
print(f"Nota do aluno: {nota}")

# 10. Temperaturas médias do ano
temperaturas = [float(input(f"Digite a temperatura média de {mes}: ")) for mes in ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]]
media_anual = sum(temperaturas) / len(temperaturas)
print(f"Média anual: {media_anual:.2f}°C")
print("Temperaturas acima da média anual:")
for i, temp in enumerate(temperaturas):
    if temp > media_anual:
        print(f"{['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'][i]}: {temp}°C")

# 11. Vendas totais e produto mais vendido
vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
total_vendas = sum(vendas.values())
mais_vendido = max(vendas, key=vendas.get)
print(f"Total de vendas: {total_vendas}")
print(f"Produto mais vendido: {mais_vendido}")

# 12. Design vencedor
votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}
vencedor = max(votos, key=votos.get)
total_votos = sum(votos.values())
print(f"Design vencedor: {vencedor}")
print(f"Porcentagem de votos: {(votos[vencedor] / total_votos) * 100:.2f}%")

# 13. Abono salarial
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = {salario: max(salario * 0.1, 200) for salario in salarios}
total_abonos = sum(abonos.values())
minimos = sum(1 for abono in abonos.values() if abono == 200)
maior_abono = max(abonos.values())
print(f"Total de gastos com abonos: {total_abonos:.2f}")
print(f"Colaboradores com abono mínimo: {minimos}")
print(f"Maior abono: {maior_abono:.2f}")

# 14. Diversidade biológica
areas = {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}
media_especies = {area: sum(valores) / len(valores) for area, valores in areas.items()}
mais_diversa = max(areas, key=lambda x: sum(areas[x]))
print("Média de espécies por área:", media_especies)
print(f"Área com maior diversidade: {mais_diversa}")

# 15. Idades dos colaboradores
setores = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65], 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64], 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56], 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
media_setores = {setor: sum(idades) / len(idades) for setor, idades in setores.items()}
media_geral = sum(sum(idades) for idades in setores.values()) / sum(len(idades) for idades in setores.values())
acima_media = sum(1 for idades in setores.values() for idade in idades if idade > media_geral)
print("Média de idades por setor:", media_setores)
print(f"Média geral de idades: {media_geral:.2f}")
print(f"Colaboradores acima da média geral: {acima_media}")
