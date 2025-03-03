#1.
def floate():
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
    try:
        idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
        nome = input('Digite o nome do(a) aluno: ').capitalize()
        resultado = idades[nome]
        if nome.isnumeric():
            raise ValueError("Nome não pode ser um número")
    except Exception as e:
        print(type(e), f"Erro: {e}")
    else:
        print(resultado)
    finally:
        print('Fim do programa')
#3.
def notas(lista: list) -> float:
    try:
        # Tenta calcular a média da lista
        calculo = sum(lista) / len(lista)
        print(calculo)
        return calculo
    except Exception as e:
        print(type(e), f"Erro: {e}")
    finally:
        print('Fim do programa')
# notas([5,5,8])
#4.
def media():
    lista1 = [4,6,7,9,10]
    lista2 = [-4,6,8,7,9]
    soma = list(zip(lista1,lista2))
    print(soma)
    try:
        media = [sum(nota) for nota in soma]
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
    try:
        gabarito = ['D', 'A', 'B', 'C', 'A']
        testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
        testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
        for i in testes_com_ex:
            if i not in ['A', 'B', 'C', 'D']:
                raise ValueError(f"Resposta inválida {i}")
        corrigir = [testes_com_ex[i] for i in range(len(testes_com_ex)) if testes_com_ex[i] == gabarito]
        print(f"Quantidade de testes corretos: {len(corrigir)}")
        print(corrigir)
    except Exception as e:
        print(type(e), f"Erro: {e}")
    finally:
        print('Fim do programa')