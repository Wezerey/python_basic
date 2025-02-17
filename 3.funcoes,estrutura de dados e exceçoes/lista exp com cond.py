''' 
    [exp[indice] for item in lista]
    [exp[indice] for item in lista if item[indice] => 8.0]
    
'''
nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]
nomes = [nome[0] for nome in nomes]
estudantes = list(zip(nomes, medias))
print(estudantes)
candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]
print(candidatos)