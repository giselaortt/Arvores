import random
from typing import Type
from collections import deque
import pytest
from multipledispatch import dispatch

INFINITY = float('inf')
NEGATIVE_INFINITY = float('-inf')


class Node:
    right:'Node' = None
    left:'Node' = None
    above:'Node' = None
    bellow:'Node' = None
    key:int
    level:int = 1

    def __next__(self, key:int) -> 'Node':
        if( self.right is not None ):
            return self.right
        if( self.bellow is not None ):
            return self.bellow
        raise StopIteration()


    def __iter__(self):

        return self


    def __init__( self, key:int, level:int = 0 ):
        self.key = key


    def __lt__( self, key:int ):

        return self.key < key


    def __gt__( self, key:int ):

        return self.key > key


    @dispatch((int,float))
    def __eq__( self, key:int ):

        return self.key == key


    @dispatch(object)
    def __eq__( self, other:'Node' ):

        return self.key == other.key


class SkipList:

    def __init__( self ):
        self.upper_left:'Node' = Node(NEGATIVE_INFINITY)
        self.upper_right:'Node' = Node(INFINITY)
        self.down_left:'Node' = self.upper_left
        self.number_of_levels:int = 1
        self.length:int = 0
        self.upper_left.right = self.upper_right
        self.upper_right.left = self.upper_left


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
        node = self.down_left
        if(node == key):
            return True
        while(node.right is not None):
            node = node.right
            if(node == key):
                return True
        return False


    def __getitem__( self ):
        pass


    def __add__( self, other:'SkipList' )->'SkipList':
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
        while( SkipList._flip_coin() and ans <= 100 ):
            ans += 1

        return ans


    def delete_node(self, key:int)->None:
        node = self.search(key)
        while(node is not None):
            SkipList._delete_node(node)
            node = node.above


    @classmethod
    def _delete_node( cls, node:Type[Node] )->None:
        if( node.right is not None ):
            node.right.left = node.left
        if( node.left is not None ):
            node.left.right = node.right
        if( node.bellow is not None ):
            node.bellow.above = node.above
        if( node.above is not None ):
            node.above.bellow = node.bellow


    def search( self, key:int ):
        if( self.length == 0 ):
            return None
        node = self._search(key)
        if(node.key == key):
            return node
        return None


    def _search( self, key:int, keep_path:bool = False )->[Type[Node],deque]:
        #if(keep_path):
        #    stack = collections.deque()
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

        #return node, stack
        return node


    def _increase_one_treee_level( self ) -> None:
        left_top = Node(NEGATIVE_INFINITY)
        right_top = Node(INFINITY)

        left_top.right = right_top
        right_top.left = left_top

        self.upper_left.above = left_top
        self.upper_right.above = right_top

        left_top.bellow = self.upper_left
        right_top.bellow = self.upper_right

        self.upper_left = left_top
        self.upper_right = right_top
        self.number_of_levels += 1


    def _adjust_tree_level(self, level:int) -> None:
        while( self.number_of_levels < level ):
            self._increase_one_treee_level()


    @classmethod
    def create_node_chaining(cls, key:int, number_of_levels:int)->'Node':
        bottom = Node(key)
        node = bottom
        for i in range(number_of_levels-2):
            next_node = Node(key)
            node.above = next_node
            next_node.bellow = node
            node = next_node
        return bottom


    @classmethod
    def link_node_chaining(cls, to_be_inserted:'Node', previous:'Node')->None:
        pass


    @classmethod
    def get_above_level_node(cls, node:'Node')->'Node':
        if(node.above is not None):
            return node.above
        while(node.above is None and node.left is not None):
            node = node.left
        if(node.above is None):
            raise Exception('end of the road')


    def insert( self, key:int )->None:
        if(key in self):
            raise Exception("Operation not permitted, no repetitions are allowed.")

        node = self._search(key)
        node_level = SkipList._random_level()
        self._adjust_tree_level(node_level+1)
        to_be_inserted = SkipList.create_node_chaining(key, node_level)

        while(to_be_inserted is not None and node is not None):
            other_node = node.right
            node.right = to_be_inserted
            to_be_inserted.left = node
            other_node.left = to_be_inserted
            to_be_inserted.right = other_node
            to_be_inserted = to_be_inserted.above
            node = SkipList.get_above_level_node(node)

        self.length += 1






