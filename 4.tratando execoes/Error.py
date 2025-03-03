""" 
    é possivel usar "Exception" para tratar qualquer tipo de erro

try:
    # código a ser executado. Caso uma exceção seja lançada, pare imediatamente
except:
    # Se uma exceção for lançada no try, rode esse código, senão pule esta etapa
else:
    # Se não houver uma exceção lançada pelo try, rode essa parte
finally:
    # Rode essa parte (com ou sem exceção)
raise:
    # Caso queira lançar uma exceção personalizada
"""
def estudante():
    notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}
    try:
        nome = input("Digite o nome do(a) estudante: ").capitalize()
        resultado = notas[nome]
        if nome.isnumeric():
            raise ValueError("Nome não pode ser um número") 
    except Exception as e :
        print(type(e),f"Erro: {e}")
        print("Nome não encontrado")
    else:
        print(resultado)
    finally:
        print("Fim do programa")

def media(lista: list=[0]) -> float:
    ''' Função para calcular a média de notas passadas por uma lista

    lista: list, default[0]
        Lista com as notas para calcular a média
        return calculo: float
        Média calculada
    '''

    calculo = sum(lista) / len(lista)
    if len(lista) >4:
        raise ValueError("Número de notas maior que o solicitado")
    return calculo
try:   
    notas = [8, 9, 10,4]
    resultado = media(notas)
except TypeError:
    print("Erro: Só é permitido números")
except ValueError as e:
    print(type(e),f"Erro: {e}")
else:
    print(resultado)
finally:("A cunsulta foi encerrada")
