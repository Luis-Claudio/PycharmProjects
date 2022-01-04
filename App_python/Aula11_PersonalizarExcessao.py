
class Error (Exception):
    pass

class ImputError(Error):
    def __init__(self,mensagem):
        self.mensagem = mensagem

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise ImputError('Erro - Nota não pode ser maior que 10')
        elif x < 0:
            raise ImputError('Erro - Nota não pode ser menor que o')
        break
    except ValueError:
        print('Erro - Digite apenas número!')
    except ImputError as ex:
        print(ex)
