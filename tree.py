class Node:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.dir = None
        self.esq = None
        self.pai = None

#arvores não balanceadas
class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, id, nome):
        novo = Node(id, nome)
        if(self.raiz == None):
            self.raiz = novo
        else:
            self.inserir_recursao( self.raiz, novo )

    def inserir_recursao(self, node, novo_no):
        if node.id < novo_no.id:
            if node.dir is None:
                node.dir = novo_no
                novo_no.pai = node
            else:
                self.inserir_recursao(node.dir, novo_no)
        else:
            if(node.esq is None):
                node.esq = novo_no
                novo_no.pai = node
            else:
                self.inserir_recursao(node.esq, novo_no)

    def buscar(self, id):
        node = self.busca(self.raiz, id)
        return node.nome

    def tras_ai(self, node, id):
        if node is None:
            return False
        if node.id == id:
            return node
        if id > node.id:
            return self.busca(node.dir, id)
        return self.busca(node.esq, id)

    def remover( self, id ):
        node = self.tras_ai( self.raiz, id )
        if( node is False ):
            print("nó não encontrado na arvore. tente novamente.")
            return
        
        #se o nó for um nó folha:
        if( node.esq is None && node.dir is None ):
            if( node.pai != None ):
                if( node.pai.dir == node ):
                    node.pai.dir = None
                else:
                    node.pai.esq = None
            return

        #se o nó possui apenas 1 filho, e esse filho está a esquerda
        if( node.dir is None ):
            node.esq.pai = node.pai
            if( node.pai != None && node.pai.esq == node ):
                node.pai.esq = node.esq
            else if( node.pai != None && node.pai.dir == node ):
                node.pai.dir = node.esq
        return
        
        #se o nó possui apenas um filho, que está a direita
        if( node.esq is None ):
            node.dir.pai = node.pai
            if( node.pai != None && node.pai.esq == node ):
                node.pai.esq = node.dir
            else if( node.pai != None && node.pai.dir == node ):
                node.pai.dir = node.dir
        return
        
        #se o nó possui dois filhos
        #podemos pegar o nó mais esquerdo do ramo direito, ou o nó mais direito do ramo esquerdo.
        #implemeitarei a primeira opção, a outra é analoga.
        substituto = node.dir
        while( substituto.esq != None ):
            substituto = substituto.esq
        
        #fazer o pai do substituto apontar para o null
        if( substituto.pai.esq == substituto )
            pai.substituto.esq = None
        else:
            pai.substituto.dir = None
        
        #fazer o substituto apontar pras ligações do nó a ser removido
        substituto.pai = node.pai
        substituto.esq = node.esq
        substituto.dir = node.dir
        
        #fazer as ligações do nó a ser removido apontarem pro substituto
        node.esq.pai = substituto
        node.dir.pai = substituto
        if( node.pai!=None and node.pai.esq == node )
            node.pai.esq = substituto
        else if( node.pai!=None and node.pai.dir == node )
            node.pai.dir = substituto
