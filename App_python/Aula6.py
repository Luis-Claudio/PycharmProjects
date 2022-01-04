conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto1.union(conjunto2)
conjunto_interseccao = conjunto1.intersection(conjunto2)
conjunto_diferenca1 = conjunto1.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto1)
conjunto_dif_simetr = conjunto1.symmetric_difference(conjunto2)
print('União -> {uni} \n'
      'Intersecção ->  {intersec} \n'
      'Diferença 1 e 2 -> {dif_1_2} \n'
      'Diferença 2 e 1 -> {dif_2_1} \n'
      'Diferença Simetrica -> {dif_simetr}' .format (uni = conjunto_uniao,
                                           intersec = conjunto_interseccao,
                                           dif_1_2 = conjunto_diferenca1,
                                           dif_2_1 = conjunto_diferenca2,
                                           dif_simetr = conjunto_dif_simetr))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
eh_subconjunto = conjunto_a.issubset(conjunto_b)
print('A esta contido em B? {}'.format(eh_subconjunto))
eh_superconjunto = conjunto_b.issuperset(conjunto_a)
print('B contem A? {}'.format(eh_superconjunto))

lista_animais_1 = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista_animais_1)
lista_animais_2 = list(conjunto_animais)
print(lista_animais_1)
print(conjunto_animais)
print(lista_animais_2)
