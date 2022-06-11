# -*- coding: utf-8 -*-

from arvore import Arvore

arv = Arvore()

# inserindo usuários
arv.inserir(3, 'Igor')
arv.inserir(6, 'Jurema')
arv.inserir(1, 'Lidia')
arv.inserir(4, 'Carlos')
arv.inserir(24, 'gi')
arv.inserir(2, 'aurora')

# buscando usuários
teste_busca1 = arv.buscar(3)
print(teste_busca1)
teste_busca2 = arv.buscar(4)
print(teste_busca2)
teste_busca3 = arv.buscar(9)
print(teste_busca3)

arv.remover( 6 )
arv.remover( 10 )
arv.remover( 2 )
arv.remover( 4 )
arv.remover( 24 )
arv.remover( 2 )

print( arv.buscar(6) )
