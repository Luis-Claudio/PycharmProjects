prim_bim = int(input('Informe a nota do 1º Bimestre:-> '))
if prim_bim > 10:
    prim_bim = int(input('*** NOTA DIGITADA ERRADA! Informe novamente a nota do 1º Bimestre :-> '))

seg_bim = int(input('Informe a nota do 2º Bimestre:-> '))
if seg_bim > 10:
    seg_bim = int(input('*** NOTA DIGITADA ERRADA! Informe novamente a nota do 2º Bimestre :-> '))

terc_bim = int(input('Informe a nota do 3º Bimestre:-> '))
if terc_bim > 10:
    terc_bim = int(input('*** NOTA DIGITADA ERRADA! Informe novamente a nota do 3º Bimestre :-> '))

quart_bim = int(input('Informe a nota do 4º Bimestre:-> '))
if quart_bim > 10:
    quart_bim = int(input('*** NOTA DIGITADA ERRADA! Informe novamente a nota do 4º Bimestre :-> '))

media_bin = (prim_bim+seg_bim+terc_bim+quart_bim)/4
print('Média do aluno = {}'.format(media_bin))

# segnum=int(input('Informe 2º número :-> '))
# restprim = primnum%2
# restseg = segnum%2
# if restprim==0 or not restseg>0:
#     print('Um número par foi digitado.')
# else:
#     print('Nunhum número par foi digitado.')

# ehpar=int(input('Informe um número para verificar se ele é ou não par:-> '))
# resto=ehpar%2
# if resto==0:
#     print('O número informado é par.')
# else:
#     print('O número informado é impar.')

# a = int(input('Informe o 1º número -> '))
# b = int(input('Informe o 2º número -> '))
# c = int(input('Informe o 3º número -> '))
#
# if a > b and a > c:
#     print ('O maior número é o 1º -> {}'.format(a))
# elif b > a and b > c:
#     print ('O maior número é o 2º -> {}'.format(b))
# elif c > a and c > b:
#     print ('O maior número é o 3º -> {}'.format(c))
# else:
#     print('Nunhum número é maior que os dois')
#
print('Programa encerrado!')