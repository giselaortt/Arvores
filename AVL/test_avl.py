from avl import Arvore

arv = Arvore()

# inserindo usuários
arv.inserir(3, 'Igor')
arv.inserir(6, 'Jurema')
arv.inserir(1, 'Lidia')
arv.inserir(4, 'Carlos')

# buscando usuários
teste_busca1 = arv.buscar(3)
print(teste_busca1)
teste_busca2 = arv.buscar(4)
print(teste_busca2)
# teste_busca1 = arv.buscar(9)
# print(teste_busca2)
