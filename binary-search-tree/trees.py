# -*- coding: utf-8 -*-

class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.right = None
        self.left = None
        self.father = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, id, name):
        novo = Node(id, name)
        if(self.root is None):
            self.root = novo
        else:
            self._insert(self.root, novo)

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


    def remove(self, id):
        node = self._search(self.root, id)
        if node is False:
            raise Exception('unexisting key')

        if( node.left is None and node.right is None ):
            if node is self.root :
                self.root = None
            else:
                if node.father.right == node:
                    node.father.right = None
                else:
                    node.father.left = None
            return


        if( node.right is None ):
            node.left.father = node.father
            if node is self.root:
                self.root = node.left
                node.left.father = None
            elif node.father.left == node:
                node.father.left = node.left
            elif node.father.right == node:
                node.father.right = node.left
            return


        if node.left is None:
            node.right.father = node.father
            if node is self.root:
                self.root = node.right
            elif node.father.left == node:
                node.father.left = node.right
            elif node.father.right == node:
                node.father.right = node.right
            return

        new_node = node.right
        while new_node.left is not None:
            new_node = new_node.left

        if( node.right is new_node ):
            new_node.left = node.left
            node.left.father = new_node

        elif( node.left is new_node ):
            new_node.right = node.right
            node.right.father = new_node

        else:
            if new_node.father.id > new_node.id:
                new_node.father.left = None
            else:
                new_node.father.right = None
            new_node.left = node.left
            new_node.right = node.right
            node.left.father = new_node
            node.right.father = new_node

        new_node.father = node.father
        if node is self.root:
            self.root = new_node
        elif node.father.left == node:
            node.father.left = new_node
        elif node.father.right == node:
            node.father.right = new_node

