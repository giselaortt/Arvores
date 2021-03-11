# -*- coding: utf-8 -*-

from avl import AVL

#um teste muito simples
def teste_inicial():
    arv = AVL()

    # inserindo usuários
    arv.inserir(3, 'Igor')
    arv.inserir(6, 'Jurema')
    arv.inserir(1, 'Lidia')
    arv.inserir(4, 'Carlos')
    arv.inserir(24, 'gi')
    arv.inserir(2, 'aurora')

    # buscando usuários
    teste_busca1 = arv.busca(3)
    print(teste_busca1.nome)
    teste_busca2 = arv.busca(4)
    print(teste_busca2.nome)
    teste_busca3 = arv.busca(9)
    print(teste_busca3)

    arv.remover( 6 )
    arv.remover( 1 )
    arv.remover( 2 )
    arv.remover( 4 )
    arv.remover( 24 )
    arv.remover( 2 )
    arv.remover( 3 )

    print( arv.busca(6) )


def segundo_teste():
    arv = AVL()
    # inserindo usuários
    arv.inserir(3, 'Igor')
    arv.inserir(6, 'Jurema')
    #checando se as alturas estão corretas
    if( arv.raiz.h != arv.altura() ):
        print('não ta ok')
    arv.inserir(1, 'Lidia')
    arv.inserir(4, 'Carlos')
    #checando se as alturas estão corretas
    if( arv.raiz.h != arv.altura() ):
        print('não ta ok')
    arv.inserir(24, 'gi')
    arv.inserir(2, 'aurora')
    arv.inserir(25, 'a')
    #checando se as alturas estão corretas
    if( arv.raiz.h != arv.altura() ):
        print('não ta ok')
    arv.inserir(26, 'b')
    arv.inserir(27, 'c')
    arv.inserir(28, 'd')
    #checando se as alturas estão corretas
    if( arv.raiz.h != arv.altura() ):
        print('não ta ok')
    arv.inserir(29, 'e')
    arv.inserir(30, 'f')
    arv.inserir(-1, 'k')
    #checando se as alturas estão corretas
    if( arv.raiz.h != arv.altura() ):
        print('não ta ok')
    arv.inserir(-10, 'g')
    arv.inserir(-5, 'h')
    #checando se as alturas estão corretas
    if( arv.raiz.h != arv.altura() ):
        print('não ta ok')
    
    if( arv.is_avl( arv.raiz ) ):
        print("okay")
    else:
        print("not_okay")
    
segundo_teste()
