
#definirei altura de um no como a maior altura dentre seus filhos, mais 1.
#o fator de balanceamento de um nó é a diferenca entre sua altura esquerda e direita. Aesq - Adir

class Node:
def __init__(self, id, nome):
    self.id = id
    self.nome = nome
    self.dir = None
    self.esq = None
    self.pai = None
    self.h = 0 #definirei a altura de uma folha como 0
    
'''
         y                               x
        / \     Right Rotation          /  \
       x   T3   - - - - - - - >        T1   y
      / \       < - - - - - - -            / \
     T1  T2     Left Rotation            T2  T3
'''
#Arvores 2: arvores binarias balanceadas
class ABB:
    def __init__(self):
        self.raiz = None


    def insercao(self, id, nome):
        novo = Node(id, nome)
        if self.raiz is None:
            self.raiz = novo
        else:
            insercao_recursao( self.raiz, novo )

    def insercao_recursao( no, novo):
        if node.id == novo_no.id:
            print("não foi possivel inserir o novo nó, pois não são aceitas repetições.")
            return
        if node.id < novo_no.id:
            if node.dir is None:
                node.dir = novo_no
                novo_no.pai = node
                self.bubble_up(node)
                self.balancear(node)
            else:
                self.inserir_recursao(node.dir, novo_no)
        else:
            if(node.esq is None):
                node.esq = novo_no
                novo_no.pai = node
                self.bubble_up(node)
                self.balancear(node)
            else:
                self.inserir_recursao(node.esq, novo_no)
   
    def bubble_up(self, node):
        while( node != None ):
            node.h = node.h + 1
            node = node.pai
   
   def rotate_direita( self, node ):
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
   
   def rotate_esquerda( self, node ):
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
   
   #função para balandear a arvore apos uma INSERÇÃO
    def balancear( self, no ):
        #find first unbalanced node
        while( node != None ):
            if( node.esq.h - node.dir.h >= 2):
                if( node.esq.esq.h - node.esq.dir.h == 1 ):
                    #left left case. perform simple right rotation.
                    self.rotate_direita( node )
                    #node.h = node.h - 2
                    
                else: #left right case.
                    rotate_esquerda( node.esq )
                    rotate_direita( node )
                    
                break;
            elif ( node.esq.h - node.dir.h <= -2 ):
                if( node.dir.esq - node.dir.dir == -1 ):
                    #right right case. perform simple right rotation.
                    self.rotate_esquerda( node )
                    #node.h = node.h - 2

                else: #right left case.
                    rotate_direita(node.dir)
                    rotate_esquerda(node)
                
                break;
            node = node.pai
            
            
    def remocao(self):
        pass
        
    def remocao_recursao():
        pass
        
    def busca(self):
        pass

    def busca_recursao():
        pass
