import random
from typing import Type


INFINITY = float('inf')
NEGATIVE_INFINITY = float('-inf')


class Node:
    right:'Node' = None
    left:'Node' = None
    above:'Node' = None
    bellow:'Node' = None
    key:int
    level:int = 0

    def __init__( self, key:int ):
        self.key = key


    def __lt__( self, key:int ):

        return self.key < key


    def __gt__( self, key:int ):

        return self.key > key


    def __del__( self ):
        pass


    def __eq__( self, key:int ):

        return self.key==key



class SkipList:
    upper_left:'Node' = Node(NEGATIVE_INFINITY)
    upper_right:'Node' = Node(INFINITY)
    number_of_levels:int = 0
    length:int = 0

    def __init__( self ):
        self.upper_left.right = self.upper_right
        self.upper_left.left = self.upper_left


    def __len__( self ):

        return self.length


    def __next__( self, node:Type[Node] )-> Type[Node]:
        while( True ):
            if( node.right is not None ):
                return node.right
            if( node.bellow is not None ):
                node = node.bellow
            else:
                return node


    def __iter__( self ):

        return self.upper_left


    def __contains__( self, key ):
        pass


    def __getitem__( self ):
        pass


    def __add__( self, other:'SkipList' ) -> 'SkipList':
        pass


    def __iadd__( self, other:'SkipList' ):
        pass


    def __del__( self ):
        pass


    @classmethod
    def _flip_coin(cls) -> bool:

        return random.randint(0,1)


    def search( self, key ):
        if( self.length == 0 ):
            return None
        node = self._search(key)
        if(node.key == key):
            return node
        return None


    def getnextnode( self, node:Type[Node], key:int ) -> Type[Node]:
        pass


    def _search( self, key:int ):
        node = self.upper_left
        while( node.key != key ):
            while( node.right is not None and node.right.key <= key ):
                node = node.right
            if(node.bellow is not None):
                node = node.bellow
            else:
                break

        return node


    def add_level( self, node:Type[Node] )->None:
        pass


    def insert( self, key:int )->None:
        node = self._search(key)
        other_node = node.right
        inserted = Node(key)
        node.right = inserted
        inserted.left = node
        other_node.left = inserted
        inserted.right = other_node
        self.length += 1


    def remove( self, key ):
        pass



