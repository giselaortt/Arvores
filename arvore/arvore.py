# -*- coding: utf-8 -*-

class Node:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.dir = None
        self.esq = None
        self.pai = None


# arvores não balanceadas
class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, id, nome):
        novo = Node(id, nome)
        if(self.raiz is None):
            self.raiz = novo
        else:
            self._inserir_recursao(self.raiz, novo)

    def _inserir_recursao(self, node, novo_no):
        if node.id == novo_no.id:
            print("não foi possivel inserir o novo nó, pois não são aceitas repetições.")
            return
        if node.id < novo_no.id:
            if node.dir is None:
                node.dir = novo_no
                novo_no.pai = node
            else:
                self._inserir_recursao(node.dir, novo_no)
        else:
            if(node.esq is None):
                node.esq = novo_no
                novo_no.pai = node
            else:
                self._inserir_recursao(node.esq, novo_no)

    def buscar(self, id):
        node = self._tras_ai(self.raiz, id)
        if node:
            return node.nome
        return 'id {id} não encontrado'

    def _tras_ai(self, node, id):
        if node is None:
            return False
        if node.id == id:
            return node
        if id > node.id:
            return self._tras_ai(node.dir, id)
        return self._tras_ai(node.esq, id)

    def remover(self, id):
        node = self._tras_ai(self.raiz, id)
        if node is False:
            print("nó não encontrado na arvore. tente novamente.")
            return
        
        # se o nó for um nó folha:
        if( node.esq is None and node.dir is None ):
            if node is self.raiz :
                self.raiz = None
            else:
                if node.pai.dir == node:
                    node.pai.dir = None
                else:
                    node.pai.esq = None
            return

        
        # se o nó possui apenas 1 filho, e esse filho está a esquerda
        if( node.dir is None ):
            node.esq.pai = node.pai
            if node is self.raiz:
                self.raiz = node.esq
            elif node.pai.esq == node:
                node.pai.esq = node.esq
            elif node.pai.dir == node:
                node.pai.dir = node.esq
            return

        
        # se o nó possui apenas um filho, que está a direita
        if node.esq is None:
            node.dir.pai = node.pai
            if node is self.raiz:
                self.raiz = node.dir
            elif node.pai.esq == node:
                node.pai.esq = node.dir
            elif node.pai.dir == node:
                node.pai.dir = node.dir
            return

        # se o nó possui dois filhos
        # podemos pegar o nó mais esquerdo do ramo direito, ou o nó mais direito do ramo esquerdo.
        # implemeitarei a primeira opção, a outra é analoga.
        substituto = node.dir
        while substituto.esq is not None:
            substituto = substituto.esq

        
        if( node.dir is substituto ):
            substituto.esq = node.esq
            node.esq.pai = substituto

        elif( node.esq is substituto ):
            substituto.dir = node.dir
            node.dir.pai = substituto
        
        else:
            #caso geral
            if substituto.pai.id > substituto.id:
                substituto.pai.esq = None
            else:
                substituto.pai.dir = None
            substituto.esq = node.esq
            substituto.dir = node.dir
            # fazer as ligações do nó a ser removido apontarem pro substituto
            node.esq.pai = substituto
            node.dir.pai = substituto
       
        substituto.pai = node.pai
        if node is self.raiz:
            self.raiz = substituto
        elif node.pai.esq == node:
            node.pai.esq = substituto
        elif node.pai.dir == node:
            node.pai.dir = substituto


    def altura( self ):
        return _altura( self.raiz )
    
    
    def _altura( self, node ):
        if node is None:
            return 0
        return max( self._altura(node.dir), self._altura(node.esq) ) + 1
