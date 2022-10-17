# -*- coding: utf-8 -*-


class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.right = None
        self.left = None
        self.father = None


    def is_leaf( self ):

        return ( self.right == None and self.left == None )


    def is_left_child( self ):

        return ( self.father is not None and self.id < self.father.id )


    def is_right_child( self ):

        return ( self.father is not None and self.id > self.father.id )


class Tree:
    def __init__(self):
        self.root = None


    def insert(self, id, name):
        new_node = Node(id, name)
        if(self.root is None):
            self.root = new_node
        else:
            self._insert(self.root, new_node)


    def _insert(self, node, novo_no):
        if node.id == novo_no.id:
            raise Exception("keyword already exists.")
        if node.id < novo_no.id:
            if node.right is None:
                node.right = novo_no
                novo_no.father = node
            else:
                self._insert(node.right, novo_no)
        else:
            if(node.left is None):
                node.left = novo_no
                novo_no.father = node
            else:
                self._insert(node.left, novo_no)


    def search(self, id):
        node = self._search(self.root, id)
        if node:
            return node.name
        return  None


    def _search(self, node, id):
        if node is None:
            return False
        if node.id == id:
            return node
        if id > node.id:
            return self._search(node.right, id)
        return self._search(node.left, id)


    def height( self ):
        return _height( self.root )


    def _height( self, node ):
        if node is None:
            return 0
        return max( self._height(node.right), self._height(node.left) ) + 1


    @staticmethod
    def prune( node ):
        if( node.father is not None ):
            node.father = None


    @staticmethod
    def find_natural_successor( node ):
        if( node.is_leaf() ):
            return None
        if( node.right is None ):
            return node.left
        if( node.left is None ):
            return node.right
        successor = node.right
        while( successor.left is not None ):
            successor = successor.left
        return successor


    @staticmethod
    def swap_node_informations( first, second ):
        first.name, second.name = second.name, first.name
        first.id, second.id = second.id, first.id


    @staticmethod
    def succeed( node, successor ):
        if( successor is not None ):
            successor.father = node.father
        if( node is self.root ):
            self.root = successor
        elif( node.is_left_child() ):
            node.father.left = node.left
        elif( node.is_right_child() ):
            node.father.right = node.left


    def remove(self, id):
        node = self._search(self.root, id)

        if node is False:
            raise Exception('unexisting key')

        if( node.is_leaf() ):
            Tree.succeed( node, None)
            return

        if( node.right is None ):
            Tree.succeed( node, node.left )
            return

        if( node.left is None ):
            Tree.succeed( node, node.right )
            return

        successor = Tree.find_natural_successor( node )
        Tree.swap_node_informations( node, successor )
        Tree.prune( successor )


