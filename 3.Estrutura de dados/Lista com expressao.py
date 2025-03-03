'''[{expressao} for {item} in {lista}]'''
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
def media(lista: list=[0]) -> float:
    return sum(lista) / len(lista)
medias=[round(media(nota),1) for nota in notas]
print(medias)
def regioes_brasil():    
    id = [1, 2, 3, 4, 5]
    regiao = ["Norte", "Nordeste", "Sudeste", "Centro-Oeste", "Sul"]

    mapa = list(zip(id, regiao))
    print(mapa)
def codigo_fruta():
    codigos = ["1000", "1001", "1002", "1003", "1004", "1005"]
    frutas = ["maçã", "uva", "banana", "laranja"]

    mercadorias = list(zip(codigos, frutas))
    print(mercadorias)
def separar_tuplas():
    tupla_iteravel = [('J392', 'João'), ('M890', 'Maria'), ('J681', 'José'), ('C325', 'Claúdia'), ('A49', 'Ana')]
    ids, nomes  = zip(*tupla_iteravel)

    ids = list(ids)
    nomes = list(nomes)

    print("IDs = ", ids)
    print("Nomes = ", nomes)