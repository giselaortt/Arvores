import random
from typing import Type
from collections import deque

INFINITY = float('inf')
NEGATIVE_INFINITY = float('-inf')


class Node:
    right:'Node' = None
    left:'Node' = None
    above:'Node' = None
    bellow:'Node' = None
    key:int
    level:int = 1

    def __init__( self, key:int, level:int = 0 ):
        self.key = key
        self.level = level


    def __lt__( self, key:int ):

        return self.key < key


    def __gt__( self, key:int ):

        return self.key > key



    def __eq__( self, key:int ):

        return self.key == key


#TODO: skip lists need a upper bound. Which should it be ?
class SkipList:
    upper_left:'Node' = Node(NEGATIVE_INFINITY)
    upper_right:'Node' = Node(INFINITY)
    down_left:'Node' = upper_left
    number_of_levels:int = 1
    length:int = 0

    def __init__( self ):
        self.upper_left.right = self.upper_right
        self.upper_left.left = self.upper_left


    def __len__( self ):

        return self.length


    def __repr__( self ):
        ans = ""
        node = self.down_left
        while( node is not None ):
            ans += str(node.key) + " "
            node = node.right
        return ans


    def __next__( self, node:Type[Node] )-> Type[Node]:
        if( node.right is not None ):
            return node.right
        if( node.bellow is not None ):
            return node.bellow
        return None


    def __iter__( self ):

        return self.down_left


    def __contains__( self, key:int ):

        return bool(self.search( key ))


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


    @classmethod
    def _random_level(cls)->int:
        ans = 1
        while( SkipList._flip_coin() ):
            ans += 1

        return ans


    def delete_node(self, key:int)->None:
        node = self.search(key)
        while(node is not None):
            SkipList._delete_node(node)
            node = node.above


    @classmethod
    def _delete_node( cls, node:Type[Node] )->None:
        node.right.left = node.left
        node.left.right = node.right
        if( node.bellow is not None ):
            node.bellow.above = node.above
        if( node.above is not None ):
            node.above.bellow = node.bellow


    def search( self, key ):
        if( self.length == 0 ):
            return None
        node = self._search(key)
        if(node.key == key):
            return node
        return None


    #refactor to use next
    def _search( self, key:int, keep_path:bool = False )->[Type[Node],deque]:
       # if(keep_path):
       #     stack = collections.deque()
        node = self.upper_left
        while( node.key != key ):
            while( node.right is not None and node.right.key <= key ):
        #        if(keep_path):
         #           stack.append(node)
                node = node.right
            if(node.bellow is not None):
                node = node.bellow
            else:
                break

        return node, stack


    def _increase_tree_level( self, node:Type[Node] )->None:
        node.upper_left.above = Node(NEGATIVE_INFINITY)
        node.upper_left.above.bellow = node
        node.upper_left = node.upper_left.above
        node.upper_right.above = Node(INFINITY)
        node.upper_right = node.upper_right.above
        self.number_of_levels += 1


    def _promotion( self, node:Type[Node] )->None:
        node.above = Node(node.key, level = node.level+1)
        node.above.bellow = node


    def insert( self, key:int )->None:
        node = self._search(key)

        if(node.key == key):
            raise Exception("Operation not permitted")

        #level = SkipList._random_level()
        #

        other_node = node.right
        inserted = Node(key)
        node.right = inserted
        inserted.left = node
        other_node.left = inserted
        inserted.right = other_node
        self.length += 1




