lista_num = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla_num = (1, 10, 12, 14)
print(len(tupla_num))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla_num)
print(type(lista_numerica))
print(lista_numerica)
lista_numerica[0] = 100
print(lista_numerica)

# print(lista_animal[1])
# nova_lista_animal = lista_animal * 3
# print(nova_lista_animal)
# lista_num.sort()
# lista_animal.sort()
# print(lista_num)
# print(lista_animal)
# # ordena crescentmente a lista
# lista_animal.reverse()
# print('lista_animal')
# # Inverte a ordenação da lista
#
# if 'lobo' in lista_animal:
#     print('Existe um Lobo na lista')
# else:
#     print('Não exite um Lobo na lista, será incluido')
#     lista_animal.append('lobo')
#     print('lista_animal')
