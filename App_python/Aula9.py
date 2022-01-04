import shutil

import shutil

def escrver_arquivo(texto):
    arquivo = open('teste.txt','w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_ar1uivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print (texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        #print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(arq_ori):
    shutil.copy(arq_ori, 'c:/TestePiton/')

def move_arquivo(arq_ori):
    shutil.move(arq_ori, 'c:/TestePiton/')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    #ista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrver_arquivo('Primeira Linha. \n')
    #aluno = 'Fernanda, 09, 10, 10,08\n'
    #atualizar_arquivo('notas.txt', aluno)
    #atualizar_arquivo('Terceira Linha. \n')
    #ler_ar1uivo('teste.txt')