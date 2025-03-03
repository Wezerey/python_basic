# 1. soma de uma lista dentro de uma lista
def soma_listas():
    lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
    soma = [sum(lista) for lista in lista_de_listas]
    print(soma)
# 2. criar uma lista que contem o terceiro elemento de cada tupla
def terceiro_elemento():
    lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
    nome=[lista_de_tuplas[i][0] for i in range(len(lista_de_tuplas))]
    print(nome)
# 3. criar uma lista numerada com os elementos da lista
    lista_numerada = []
    for i in range(len(nome)):
        lista_numerada.append([i+1,nome[i]])
    print(lista_numerada)
# 4. criar uma lista que armazena somente o valor numero se for apartamento
def aluguel():
    aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
    valor = [aluguel[i][1] for i in range(len(aluguel)) if aluguel[i][0] == 'Apartamento']
    print(valor)
# 5. criar uma lista que armazena o valor da despesa de cada mês
def despesas(): 
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
    cadastro = {ano: gasto for ano, gasto in zip(meses, despesa)}
    print(cadastro)
# 6. Filtrar as vendas de 2022 que foram maiores ou iguais a 6000
def vendas():
    vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
    vendas_2022 = [vendas[i] for i in range(len(vendas)) if vendas[i][0] == '2022' and vendas[i][1] >= 6000]
    print(vendas_2022)
# 7. analize de dados de hipoglicemia
def glicemia():
    glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
    situacao = [
        "Hipoglicemia" if hipo <= 70 else 
        "Normal" if 71 <= hipo <= 99 else 
        "Alterada" if 100 <= hipo <= 125 else 
        "Diabetes" 
        for hipo in glicemia
    ]
    situacao_final = list(zip( situacao,glicemia))
    print(situacao_final)
# 8. caclulo total de produtos
def ecomerce():
    id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
    preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]
    tabela = [('id', 'quantidade', 'preco', 'total')]
    tabela += [(id[i], quantidade[i], preco[i], quantidade[i]*preco[i]) for i in range(len(id))]
    print(tabela)
# 9. contagem de estados unicos
def estados():
    estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
    estados_unicos = list(set(estados))
    lista_de_listas = []
    for estado in estados_unicos:
        lista = [uf for uf in estados if uf == estado]
        lista_de_listas.append(lista)
    print(lista_de_listas)
    contagem_valores = {estados_unicos[i]: len(lista_de_listas[i]) for i in range(len(estados_unicos))}
    print(contagem_valores)

# 10. agrupamento de funcionarios por estado
def funcionarios():
    funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
    # Armazenando os estados sem repetição de valor
    estados_unicos = list(set([tupla[0] for tupla in funcionarios]))

    # Criando uma lista de listas com valores de funcionários de cada estado
    lista_de_listas = []
    for estado in estados_unicos:
        lista = [tupla[1] for tupla in funcionarios if tupla[0] == estado]
        lista_de_listas.append(lista)
    print(lista_de_listas)

    # Criando um dicionário com dados agrupados de funcionário por estado
    agrupamento_por_estado = {estados_unicos[i]: lista_de_listas[i] for i in range(len(estados_unicos))}
    print(agrupamento_por_estado)

    # Criando um dicionário com a soma de funcionários por estado
    soma_por_estado = {estados_unicos[i]: sum(lista_de_listas[i]) for i in range(len(estados_unicos))}
    print(soma_por_estado)