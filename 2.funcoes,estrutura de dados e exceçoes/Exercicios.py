def ponderada():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    media_ponderavel = lambda x, y, z:(x*3+y*2+z*5)/10
    media_estudante = media_ponderavel(n1, n2, n3)
    print(f'A média do aluno foi: {media_estudante:.1f}\n')


def qualitativo():
    notas = [6.0, 7.0, 8.0, 9.0]
    qualitativo = 0.5
    notas_atualizadas = list(map(lambda x: x + qualitativo, notas))
    print(notas_atualizadas)

def Aquecimento ():
    lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
    soma = sum(lista)
    for i in range(len(lista)):
        if i == 0:
            menor = lista[i]
            maior = lista[i]
        elif lista[i] < menor:
            menor = lista[i]
        elif lista[i] > maior:
            maior = lista[i]
    print(f'O menor número da lista é: {menor}\nO maior número da lista é: {maior}\nA soma de todos os números da lista é: {soma}\nA lista tem {len(lista)} elementos\n')            
def lambda1 ():
    '''lambda usado para exibir o cubo dos numeros presentes na lista.
    '''
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lambda2 = list(map(lambda x: x ** 2, numeros))
    print(lambda2)
def nota ():
    ''' Min e Max para identificar qual a madia maior e menor de uma lista
    '''
    notas = [5.0, 6.0, 7.0, 8.0, 9.0]
    notas.remove(min(notas))
    notas.remove(max(notas))
    media = sum(notas) / len(notas)
    print(f'Nota da manobra{media:.1f}')
def media_notas ():
    ''' Min e Max para identificar qual a madia maior e menor de uma lista
        If colocado direto no print
    '''
    notas = [6.0, 7.0, 8.0, 9.0]
    maior = max(notas)
    menor = min(notas)
    media = sum(notas)/len(notas)
    print(f'Maior nota: {maior}\nMenor nota: {menor}\nMédia: {media:.1f}, Situação: {"Aprovado" if media >= 7 else "Reprovado"}')
def nome_sobrenome():
    nomes = ["joão", "MaRia", "JOSÉ"]
    sobrenomes = ["SILVA", "souza", "Tavares"]
    nome_completo = list(map(lambda x, y: x.capitalize() + " " + y.capitalize(), nomes, sobrenomes))
    print(nome_completo)
def gols():
    gols_marcados = [2, 1, 3, 1, 0]
    gols_sofridos = [1, 2, 2, 1, 3]
    gols_total = list(map(lambda x, y: x - y, gols_marcados, gols_sofridos))
    pontos = 0
    for x,y in enumerate(gols_total):
        if y == 0:
            pontos += 1
        elif y > 0:
            pontos += 3
        else:
            pontos += 0
        print(f'Rodada {x+1}: {y} gols, {pontos} pontos')
def viagem():
    dias = int(input("Quantas diárias? "))
cidade = input("Qual a cidade? [Salvador, Fortaleza, Natal ou Aracaju]: ")
distancias = [850, 800, 300, 550]
passeio = [200, 400, 250, 300]
km_l = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gasto_gasolina(cidade):
    if cidade == "Salvador":
        return (2 * distancias[0] * gasolina) / km_l 
    elif cidade == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l 
    elif cidade == "Natal":
        return (2 * distancias[2] * gasolina) / km_l 
    elif cidade == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l 

def gasto_passeio(cidade, dias):
    if cidade=="Salvador":
        return passeio[0] * dias
    elif cidade=="Fortaleza":
        return passeio[1] * dias
    elif cidade=="Natal":
        return passeio[2] * dias 
    elif cidade=="Aracaju":
        return passeio[3] * dias 

    gastos = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)
    print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {round(gastos, 2)} reais")
def viagem_2():
    print('Informe qual a cidade deseja ir:\n[1]Salvador\n[2]Fortaleza\n[3]Natal\n[4]Aracaju')
    escolha_cidade = int(input('Digite o número da cidade: '))
    nomes_cidades = ["Salvador","Fortaleza","Aracaju","Natal"]
    escolha_dias= int(input("Digite a quantidade de dias, de 1 a 4: "))
    dias = [200, 400, 250, 300]
    distancia = [850,800,300,550]
    gasto_alimentacao = sum(dias[:escolha_dias])
    gasto_gasolina = round((distancia[escolha_cidade-1]/ 14)*5)
    gasto_hotel = 150*escolha_dias
    gastos = gasto_alimentacao+gasto_gasolina+gasto_hotel
    print(f"Com base nos gastos definidos, uma viagem de {escolha_dias} dias para {nomes_cidades[escolha_cidade-1]} saindo de Recife custaria {gastos} reais")
def filtro():
    frase = "Aprender Python aqui na Alura é muito bom"
    palavras = frase.split()
    filtro = list(filter(lambda x: len(x) >= 5, palavras))
    print(filtro)