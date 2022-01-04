A = int(input('Informe o 1º valor: '))
B = int(input('Informe o 2º valor: '))
SOMA = A + B
SUBTRACAO = A - B
MULTIPLICACAO = A * B
DIVISAO = A / B
RESTO = (A % (B+1))
X ='1'
print('Soma de '+str(A)+' + '+str(B)+' = {}'.format(SOMA))
print('Subtraçâo de '+str(A)+' - '+str(B)+ ' = '+str(SUBTRACAO))
print('Multiplicaçâo de '+str(A)+' x '+str(B)+ ' = '+str(MULTIPLICACAO))
print('Divisão de '+str(A)+' / '+str(B)+ ' = '+str(int(DIVISAO)))
print('Resto da divisão de '+str(A)+' / '+str(B+int(X))+ ' = '+str(RESTO))
resultado = ('Soma = {soma} . \nSubtração = {sub}'
      '\nMultiplicação = {multi}'
      '\nDivisão = {div} '
      '\nResto = {rest}'.format(soma=SOMA,
                                sub=SUBTRACAO,
                                multi=MULTIPLICACAO,
                                div=DIVISAO,
                                rest=RESTO))
print(resultado)
# utilize o rastag para comentários
# outra opção é utilizar o comando .format()
# \n equivale ao enter, muda de linha