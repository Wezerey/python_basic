''' 
    [exp[indice] for item in lista]
    [exp[indice] for item in lista if item[indice] => 8.0]
    {chave: valor for item in lista}
    
    
'''
def cond_1():
    nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
    medias = [9.0, 7.3, 5.8, 6.7, 8.5]
    nomes = [nome[0] for nome in nomes]
    estudantes = list(zip(nomes, medias))
    print(estudantes)
    candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]
    print(candidatos)
def nota_alunos():
    nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
    notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
    medias = [9.0, 7.3, 5.8, 6.7, 8.5]
    situacao = ["aprovado" if media >= 6 else "reprovado" for media in medias]
    lista_completa = list(zip([nome[0] for nome in nomes], medias, situacao))
    lista_completa1 = (nomes, medias, situacao)
    print(situacao)
    print(lista_completa)
    print(lista_completa1)
def estudantes_dict():
    lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                    [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                    [9.0, 7.3, 5.8, 6.7, 8.5],
                    ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]
    coluna = ["Notas", "Médias", "Situação"]
    cadastro = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))}
    print(cadastro)
    cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]
    print(cadastro["Estudante"])
def media_estudantes():
    nomes_estudantes = [ "Enrico Monteiro", "Luna Pereira", "Anthony Silveira", "Letícia Fernandes", 
                    "João Vitor Nascimento", "Maysa Caldeira", "Diana Carvalho", "Mariane da Rosa",
                    "Camila Fernandes", "Levi Alves", "Nicolas da Rocha", "Amanda Novaes", 
                    "Laís Moraes", "Letícia Oliveira", "Lucca Novaes", "Lara Cunha", 
                    "Beatriz Martins", "João Vitor Azevedo", "Stephany Rosa", "Gustavo Henrique Lima" ]
    medias_estudantes = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 10.0, 5.0, 8.2, 5.5,8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1, 5.6, 6.7, 8.2]
    bolsistas = {nome: media for nome, media in zip(nomes_estudantes, medias_estudantes) if media >= 9.0}
    print(bolsistas)
media_estudantes()