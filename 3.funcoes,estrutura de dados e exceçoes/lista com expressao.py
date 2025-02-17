'''[{expressao} for {item} in {lista}]'''
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
def media(lista: list=[0]) -> float:
    return sum(lista) / len(lista)
medias=[round(media(nota),1) for nota in notas]
print(medias)
