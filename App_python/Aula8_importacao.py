from Aula7_televisao import Televisao
from Aula7_Calc1 import Calculadora
from Aula8_ContadorLetras import contador_letras, teste

if __name__ == '__main__':
    calculadora = Calculadora(5, 10)
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    print(calculadora.soma())
    lista = ('cachorro', 'gato', 'elefante')
    print(contador_letras(lista))
    total_letras = contador_letras(lista)
    print('Total de letras por palavra = {}'.format(total_letras))
    print(teste())