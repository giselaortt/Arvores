# -*- coding: utf-8 -*-

#definirei altura de um no como a maior altura dentre seus filhos, mais 1.
#o fator de balanceamento de um nó é a diferenca entre sua altura esquerda e direita. Hesq - Hdir


class Node:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.dir = None
        self.esq = None
        self.pai = None
        self.h = 1 #definirei a altura de uma folha como 1
        
    def fator(self): #o fator é a altura do lado esquerdo menos a altura do lado direito
        if self.dir is None and self.esq is None:
            return 0
        if self.esq is None:
            return -1 * self.dir.h
        if self.dir is None:
            return self.esq.h
        else:
            return self.esq.h - self.dir.h
    

'''
         y                               x
        / \     Right Rotation          /  \
       x   T3   - - - - - - - >        T1   y
      / \       < - - - - - - -            / \
     T1  T2     Left Rotation            T2  T3
'''
#Arvores 2: arvores binarias balanceadas
class AVL:
    def __init__(self):
        self.raiz = None


    def inserir(self, id, nome):
        novo = Node(id, nome)
        if self.raiz is None:
            self.raiz = novo
        else:
            self.inserir_recursao( self.raiz, novo )


    def inserir_recursao( self, node, novo_no):
        if node.id == novo_no.id:
            print("não foi possivel inserir o novo nó, pois não são aceitas repetições.")
            return
        if node.id < novo_no.id:
            if node.dir is None:
                node.dir = novo_no
                novo_no.pai = node
                self.atualizar_altura(novo_no)
                self._balancear_apos_inserir(node)
            else:
                self.inserir_recursao(node.dir, novo_no)
        else:
            if(node.esq is None):
                node.esq = novo_no
                novo_no.pai = node
                self.atualizar_altura(novo_no)
                self._balancear_apos_inserir(node)
            else:
                self.inserir_recursao(node.esq, novo_no)


    #atualiza a altura apos uma inserir
    def atualizar_altura(self, node ):
        while( node != None and node.pai != None ):
            if( node.pai.h == node.h ):
                node.pai.h = node.pai.h + 1
                node = node.pai
            else:
                break


    def rotacionar_direita( self, node ):
        #o filho esquerdo se torna o novo pai
        novo_pai = node.esq
        if( node.pai.id > node.id ):
            node.pai.esq = novo_pai
        else:
            node.pai.dir = novo_pai
        novo_pai.pai = node.pai
        node.pai = novo_pai
        #o antigo pai se torna o novo filho DIREITO, e assume o filho direito do outro como seu filho ESQUERDO.
        node.esq = novo_pai.dir
        novo_pai.dir.pai = node
        novo_pai.dir = node
        atualizar_altura( node )
        
        
    def rotacionar_esquerda( self, node ):
        novo_pai = node.dir
        novo_pai.pai = node.pai
        if( node.pai.id > node.id ):
            node.pai.esq = novo_pai
        else:
            node.pai.dir = novo_pai
        node.pai = novo_pai
        #o antigo pai se torna o novo filho ESQUERDO e assume o filho esquerdo do outro como seu filho DIREITO
        novo_pai.esq.pai = node
        node.dir = novo_pai.esq
        novo_pai.esq = node
        atualizar_altura( node )

    def atualizar_altura( self, node ):
        node.h = max(node.dir.h, node.esq.h) + 1
        atualizar_altura(node.pai)

   #função para balancear a arvore apos uma INSERÇÃO
    def _balancear_apos_inserir( self, no ):
        #find first unbalanced node
        while( node != None ):
            if( node.esq.h - node.dir.h >= 2):
                if( node.esq.esq.h - node.esq.dir.h == 1 ):
                    #left left case. perform simple right rotation.
                    self.rotacionar_direita( node )
                    #node.h = node.h - 2

                else: #left right case.
                    rotacionar_esquerda( node.esq )
                    rotacionar_direita( node )

                break;
            elif ( node.esq.h - node.dir.h <= -2 ):
                if( node.dir.esq - node.dir.dir == -1 ):
                    #right right case. perform simple right rotation.
                    self.rotacionar_esquerda( node )
                    #node.h = node.h - 2

                else: #right left case.
                    rotacionar_direita(node.dir)
                    rotacionar_esquerda(node)

                break;
            node = node.pai


    def remocao(self, id):
        self.remocao( self.raiz, id )


    def _remocao( self, id ):
        node = self.busca( id )
        if node is None:
            print("id não encontrado")
            return
            
        #a primeira parte é fazer uma remoção comum.
        
        # se o nó for um nó folha:
        if node.esq is None and node.dir is None:
            if node.pai is not None:
                if node.pai.dir == node:
                    node.pai.dir = None
                else:
                    node.pai.esq = None
            return

        # se o nó possui apenas 1 filho, e esse filho está a esquerda
        if node.dir is None:
            node.esq.pai = node.pai
            if node.pai is not None and node.pai.esq == node:
                node.pai.esq = node.esq
            elif node.pai is not None and node.pai.dir == node:

                node.pai.dir = node.esq
        return

        # se o nó possui apenas um filho, que está a direita
        if node.esq is None:
            node.dir.pai = node.pai
            if node.pai is not None and node.pai.esq == node:
                node.pai.esq = node.dir
            elif node.pai is not None and node.pai.dir == node:

                node.pai.dir = node.dir
        return
            
        # se o nó possui dois filhos
        # podemos pegar o nó mais esquerdo do ramo direito, ou o nó mais direito do ramo esquerdo.
        #ou podemos escolher o que tiver o valor mais próximo, ou o que estiver no ramo mais longo.
        substituto_direito = node.dir
        dist_direita = 1
        while substituto_direito.esq is not None:
            substituto_direito = substituto_direito.esq
            dist_direita += 1
            
        substituto_esquerdo = node.esq
        dist_esquerda = 1
        while substituto_esquerdo.dir is not None:
            substituto_esquerdo = substituto_esquerdo.dir
            dist_esquerda += 1
        
        #escolhendo o no que esta mais longe
        if( dist_direita > dist_esquerda ):
            substituto = substituto_direito
            
        else:
            substituto = substituto_esquerdo

        auxiliar = substituto.pai # vamos guardar uma referencia para esse nó pois é a partir daqui que será necessário rebalancear.

        # fazer o pai do substituto apontar para o null
        if substituto.pai.id > substituto.id:
            substituto.pai.esq = None
        else:
            substituto.pai.dir = None

        # fazer o substituto apontar pras ligações do nó a ser removido
        substituto.pai = node.pai
        substituto.esq = node.esq
        substituto.dir = node.dir

        # fazer as ligações do nó a ser removido apontarem pro substituto
        node.esq.pai = substituto
        node.dir.pai = substituto
        if node.pai is not None and node.pai.esq == node:
            node.pai.esq = substituto
        elif node.pai is not None and node.pai.dir == node:
            node.pai.dir = substituto

        #agora vamos atualizar a altura após a remoção ( para poder calcular os fatores de cada nó )
        node = auxiliar
        if node.dir is None and node.esq is None:
            node.h = 0
        elif node.dir is None:
            node.h = node.esq.h+1
        elif node.esq is None:
            node.h = node.dir.h+1
            
        while( node.pai != None ):
            node = node.pai
            if( node.dir.h < node.h-1 and node.esq.h < node.h-1 ):
                node.h -= 1
            else:
                break
    
        #agora balancear a arvore. primeiro vamos procurar o primeiro nó desbalanceado.
        node = auxiliar
        while( node != None ):
            if abs(node.fator()) <= 1:
                node = node.pai
            else:
                node_z = node
                if( node_z.dir.h > node_z.esq.h ):
                    node_y = node_z.dir
                else:
                    node_y = node_z.esq
                if( node_y.dir.h > node_y.esq.h ):
                    node_x = node_y.dir
                else:
                    node_x = node_y.esq
                    
                ##Left-left case
                if( node_z.esq is node_y and node_y.esq is node_x ):
                    rotacionar_direita(node_z)

                #Left-right case
                if( node_z.esq is node_y and node_y.dir is node_x ):
                    rotacionar_esquerda( node_y )
                    rotacionar_direita( node_z )

                #right-left case
                if( node_z.dir is node_y and node_y.esq is node_x ):
                    rotacionar_direita( node_y )
                    rotacionar_esquerda( node_z )
                
                #right-right case
                if( node_z.dir is node_y and node_y.dir is node_x ):
                    rotacionar_esquerda( node_z )


    def busca(self, id):
        node = self._busca(self.raiz, id)
        if node:
            return node.nome
        return 'id {id} não encontrado'


    def _busca(self, node, id):
        if node is None:
            return node
        if node.id == id:
            return node
        if id > node.id:
            return self._busca(node.dir, id)
        return self._busca(node.esq, id)
        
        
    def altura( self ):
        return _altura( self.raiz )
    
    
    def _altura( self, node ):
        if node is None:
            return 0
        return max( self._altura(node.dir), self._altura(node.esq) ) + 1
