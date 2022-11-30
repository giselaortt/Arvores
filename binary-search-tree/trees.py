# -*- coding: utf-8 -*-
from typing import Type


class Node:
    def __init__(self, id, name:str):
        self.id = id
        self.name = name
        self.right = None
        self.left = None
        self.parent = None


    def is_leaf( self ) -> bool:

        return ( self.right == None and self.left == None )


    def is_left_child( self ) -> bool:

        return self.parent is not None and self.parent.left == self


    def is_right_child( self ) -> bool:

        return self.parent is not None and self.parent.right == self


class Tree:
    def __init__(self):
        self.root = None


    def insert(self, id, name:str) -> None:
        new_node = Node(id, name)
        if(self.root is None):
            self.root = new_node
        else:
            self._insert(self.root, new_node)


    def _insert(self, node:Type[Node], other:Type[Node]) -> None:
        if node.id == other.id:
            raise Exception("keyword already exists.")
        if node.id < other.id:
            if node.right is None:
                node.right = other
                other.parent = node
            else:
                self._insert(node.right, other)
        else:
            if(node.left is None):
                node.left = other
                other.parent = node
            else:
                self._insert(node.left, other)


    def search(self, id) -> str :
        node = self._search(self.root, id)
        if node:
            return node.name
        return False


    def _search(self, node:Type[Node], id) -> Type[Node]:
        if node is None:
            return False
        if node.id == id:
            return node
        if id > node.id:
            return self._search(node.right, id)
        return self._search(node.left, id)


    def height( self ) -> int:
        return _height( self.root )


    def _height( self, node:Type[Node] ) -> int:
        if node is None:
            return 0
        return max( self._height(node.right), self._height(node.left) ) + 1


    def _prune( self, node:Type[Node] ) -> None:
        if( self.root is node ):
            self.root = None
        if( node.parent is None ):
            return
        if( node.is_left_child() ):
            node.parent.left = None
        else:
            node.parent.right = None
        node.parent = None


    @staticmethod
    def find_logical_successor( node:Type[Node] ) -> Type[Node]:
        successor = node.right
        while( successor.left is not None ):
            successor = successor.left
        return successor


    @staticmethod
    def _swap_node_informations( first:Type[Node], second:Type[Node] ) -> None:
        first.name, second.name = second.name, first.name
        first.id, second.id = second.id, first.id


    def succeed( self, node:Type[Node], successor:Type[Node] ) -> None:
        if( successor is not None ):
            successor.parent = node.parent

        if( node is self.root ):
            self.root = successor
            return

        if( node.is_left_child() ):
            node.parent.left = successor

        elif( node.is_right_child() ):
            node.parent.right = successor


    def remove(self, id) -> None:
        node = self._search(self.root, id)

        if( node is False ):
            raise Exception('unexisting key')

        if( node.is_leaf() ):
            self._prune( node )
            return

        if( node.right is None ):
            self.succeed( node, node.left )
            return

        if( node.left is None ):
            self.succeed( node, node.right )
            return

        successor = Tree.find_logical_successor( node )
        Tree._swap_node_informations( node, successor )
        self._prune( successor )

