prim_bim = int(input('Informe a nota do 1º Bimestre:-> '))
if prim_bim > 10:
    prim_bim = int(input('*** NOTA DIGITADA ERRADA! Informe novamente a nota do 1º Bimestre :-> '))

seg_bim = int(input('Informe a nota do 2º Bimestre:-> '))
while seg_bim > 10:
    seg_bim = int(input('*** NOTA DIGITADA ERRADA! Informe novamente a nota do 2º Bimestre :-> '))

terc_bim = int(input('Informe a nota do 3º Bimestre:-> '))
while terc_bim > 10:
    terc_bim = int(input('*** NOTA DIGITADA ERRADA! Informe novamente a nota do 3º Bimestre :-> '))

quart_bim = int(input('Informe a nota do 4º Bimestre:-> '))
while quart_bim > 10:
    quart_bim = int(input('*** NOTA DIGITADA ERRADA! Informe novamente a nota do 4º Bimestre :-> '))

media_bin = (prim_bim+seg_bim+terc_bim+quart_bim)/4
print('Média do aluno = {}'.format(media_bin))

# eh_primo = int(input('Informe até que  número devo verificar se é primo: -> '))
#
# for ind_for_2 in range(eh_primo + 1) :
#     cont_rest = 0
#     for ind_for in range(1, ind_for_2+1) :
#         rest_div = ind_for_2 % ind_for
#         print('Resto de: {dividendo} / {divisor} -> {rest}' . format(dividendo=ind_for_2, divisor=ind_for, rest=rest_div))
#         if rest_div == 0:
#             cont_rest = cont_rest + 1
#     if cont_rest == 2 or cont_rest == 1:
#         print('O número {} é primo'.format(ind_for_2))
#     else:
#         print('O número {} não é primo'.format(ind_for_2))

# eh_primo = int(input('Informe um número para verificar se é primo: -> '))
#
# cont_rest = 0
#
# for ind_for in range(1, eh_primo+1) :
#     resto = eh_primo % ind_for
#     print('Resto de: {dividendo} / {divisor} -> {rest}' . format(dividendo=eh_primo, divisor=ind_for, rest=resto))
#     if resto == 0:
#         cont_rest cont_rest + 1
#
# if cont_rest == 2 or cont_rest == 1:
#     print('O número {} é primo'.format(eh_primo))
# else:
#     print('O número {} não é primo'.format(eh_primo))

# for ind in range(1, 101) :
#     print ('Valor de Índice = {} ' .format(ind))