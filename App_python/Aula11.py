
lista = [1, 10]

try:
    divisao = 10/5
    numero = lista[1]
    #x = a
except ZeroDivisionError:
    print('Não é possível divasão por zero')
except IndexError:
    print('Erro ao acessar um índice na tabela')
except BaseException as ex:
    print('Erro Desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não a excessão')
finally:
    print('Sempre exevutar sempre, independente do que aconteça')