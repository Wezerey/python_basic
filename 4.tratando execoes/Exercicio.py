#1.
def floate():
    '''
    A função floate() recebe dois números e retorna a divisão do primeiro pelo segundo.
    Caso o segundo número seja 0, a função deve retornar um erro ZeroDivisionError.
    Caso o usuário digite um valor que não seja um número, a função deve retornar um erro ValueError.
    '''
    try:
        num1 = float(input('Digite dois números: '))
        num2 = float(input('Digite dois números: '))
        resultado = num1 / num2
        print (resultado)
    except Exception as e:
        print('Erro: não foi possível realizar a divisão')
        print(type(e))
#2.
def nome():
    '''
    A função nome() recebe um dicionário com os nomes e idades de alunos e retorna a idade do aluno.
    Caso o nome não seja encontrado no dicionário, a função deve retornar um erro KeyError.
    Caso o nome seja um número, a função deve retornar um erro ValueError.
    '''
    try:
        idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
        nome = input('Digite o nome do(a) aluno: ').capitalize()
        resultado = idades[nome]
        if nome.isnumeric():
            raise ValueError("Nome não pode ser um número")
        elif nome not in idades:
            raise KeyError(f"Nome {nome} não encontrado")
    except Exception as e:
        print(type(e), f"Erro: {e}")
    else:
        print(resultado)
    finally:
        print('Fim do programa')
#3.
def notas(lista: list) -> float:
    '''
    A função notas() recebe uma lista de números e retorna a média dos elementos.
    Caso a lista seja vazia, a função deve retornar um erro ZeroDivisionError.
    O print deve retornar a média dos elementos da lista.
    O print do finally deve retornar 'Fim do programa'.
    '''
    try:
        # Tenta calcular a média da lista
        calculo = sum(lista) / len(lista)
        print(calculo)
        return calculo
    except Exception as e:
        print(type(e), f"Erro: {e}")
    finally:
        print('Fim do programa')
# notas([5,5,8,])
#4.
def media():
    '''
    A função media() recebe duas listas de números e retorna a média das somas de cada par de elementos.
    Caso as listas não tenham o mesmo tamanho ou uma string, a função deve retornar um erro ValueError.
    O print deve retornar uma lista com os elementos das duas listas e a soma de cada par de elementos.
    '''
    lista1 = [4,6,7,9,10]
    lista2 = [-4,6,8,7,9]
    media = list(zip(lista1,lista2,[(x + y)for x, y in zip(lista1,lista2)]))
    try:
        
        if len(lista1) != len(lista2):
            raise ValueError("Listas devem ter o mesmo tamanho")
    except Exception as e:
        print(type(e), f"Erro: {e}")
    else:
        
        print(media)
    finally:
        print('Fim do programa')
# 5.
def correcao():
    '''
    A função correcao() recebe uma lista de testes de múltipla escolha, 
    onde cada teste é uma lista de 5 alternativas (A, B, C, D) e 
    retorna a quantidade de testes corretos e quais são eles.
    Caso a alternativa não seja uma das opções válidas,
    a função deve retornar um erro ValueError.
    '''
    try:
        gabarito = ['D', 'A', 'B', 'C', 'A']
        testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
        testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
        # mudar o testes_sem_ex para testes_com_ex para testar o erro
        fora_padrao = [i for itens in testes_sem_ex for i in itens if i not in {'A', 'B', 'C', 'D'}]
        if fora_padrao:
            raise ValueError(f"A alternativa {fora_padrao} não é uma opção de alternativa válida")
        else:
            corrigir = [testes_com_ex[i] for i in range(len(testes_com_ex)) if testes_com_ex[i] == gabarito]
        print(f"Quantidade de testes corretos: {len(corrigir)}")
        print(corrigir)
    except Exception as e:
        print(type(e), f"Erro: {e}")
    finally:
        print('Fim do programa')
def tratar_lista():
    lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                    'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                    'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']
    for palavra in lista_nao_tratada:
        for letra in palavra:
            if letra in ',.!':
                raise ValueError(f"O texto apresenta pontuações na palavra '{palavra}'.")
def divider_colunas():
    '''
    A função divider_colunas() recebe duas listas e retona a divisao entre elas,
    Se uma das colunas possui um valor igual a zero, a função deve retornar um erro ZeroDivisionError.
    Caso as listas não tenham o mesmo tamanho, a função deve retornar um erro ValueError.
    '''
    pressoes = [100, 120, 140, 160,150]
    temperaturas = [20, 25, 30, 35, 40]
    try:
        media = [round(pressoes[i] / temperaturas[i], 1) for i in range(len(pressoes))]
        if len(temperaturas) != len(pressoes):
            raise ValueError("Listas devem ter o mesmo tamanho")
    except ZeroDivisionError:
        print("Erro: divisão por zero")
    else:
        print(media)
    finally:
        print("Fim do programa")

