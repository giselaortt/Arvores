import random
from typing import Type, Union
from collections import deque
import pytest
from multipledispatch import dispatch


END_OF_LIST = float('inf')
BEGINNING_OF_LIST = float('-inf')


class NodeSkipList:
    right:'NodeSkipList' = None
    left:'NodeSkipList' = None
    above:'NodeSkipList' = None
    bellow:['NodeSkipList'] = None
    key:any
    level:int = 1

    def __next__(self) -> 'NodeSkipList':
        if( self.right is not None ):
            return self.right
        raise StopIteration()


    def __iter__(self):

        return self


    def __init__( self, key:any ):
        self.key = key


    def __lt__( self, key:any ):

        return self.key < key


    def __gt__( self, key:int ):

        return self.key > key


    @dispatch((int,float))
    def __eq__( self, key:int ):

        return self.key == key


    @dispatch(object)
    def __eq__( self, other:'NodeSkipList' ):

        return self.key == other.key


    def __repr__(self):
        node_str = "  {1}\n{2}  <{0}>  {3}\n  {4}\n"
        above = self.above.key if self.above else None
        bellow = self.bellow.key if self.bellow else None
        right = self.right.key if self.right else None
        left = self.left.key if self.left else None

        return  node_str.format( self.key, above, left, right, bellow )


class SkipList:

    def __init__( self ):
        self.upper_left:'NodeSkipList' = NodeSkipList(BEGINNING_OF_LIST)
        self.upper_right:'NodeSkipList' = NodeSkipList(END_OF_LIST)
        self.down_left:'NodeSkipList' = self.upper_left
        self.number_of_levels:int = 1
        self.length:int = 0
        self.upper_left.right = self.upper_right
        self.upper_right.left = self.upper_left
        self.middle = None


    def __len__( self ):

        return self.length


    def __repr__( self ):
        ans = ""
        node = self.down_left
        while( node is not None ):
            ans += str(node.key) + " "
            node = node.right

        return ans


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


    def __eq__( self, other:'SkipList' )->bool:

        return str(self) == str(other)


    def __getitem__( self, index ):
        if isinstance(index, int):
            if index < 0 :
                index = len(self) + index
            node  = self._search_per_index(index)
            return node.key

        elif isinstance(index, tuple):
            node = self.down_left
            answer = SkipList()
            ind = 0
            while(node != END_OF_LIST):
                node = next(node)
                if(ind in index):
                    answer.insert(node.key)
                ind += 1
            return answer

        elif isinstance(index, slice):
            index.stop
            answer = SkipList()
            node = self.down_left
            node = next(node)
            answer_node_ptr = answer.down_left
            for i in range(0,index.start):
                node = next(node)
            for i in range(index.stop - index.start):
                answer.insert(node.key, answer_node_ptr)
                node = next(node)
                answer_node_ptr = next(answer_node_ptr)
            return answer
        else:
            raise ValueError(f'SkipList cannot be indexed with values of type {type(index)}')


    def __delitem__(key):
        pass


    def __add__( self, other:'SkipList')->'SkipList':
        first = self.down_left.right
        second = other.down_left.right
        return_list = SkipList()
        return_list_node = return_list.down_left
        while(first != END_OF_LIST or second != END_OF_LIST):
            if( first < second ):
                return_list.insert( first.key, return_list_node )
                first = next(first)
                return_list_node = next(return_list_node)
            elif( second < first ):
                return_list.insert( second.key, return_list_node )
                second = next(second)
                return_list_node = next(return_list_node)
            elif( first == second ):
                return_list.insert( second.key, return_list_node )
                first = next(first)
                second = next(second)
                return_list_node = next(return_list_node)

        return return_list


    def __iadd__( self, other:'SkipList', deep_copy:bool=True )->None:
        first = self.down_left
        second = other.down_left.right
        self._adjust_tree_level(other.number_of_levels)
        while( second != END_OF_LIST):
            if( second > first and second < first.right ):
                self.insert( second.key, first )
                second = next(second)
            elif(second == first):
                first = next(first)
                second = next(second)
            else:
                first = next(first)
        return self


    @classmethod
    def _flip_coin(cls) -> bool:

        return random.randint(0,1)


    @classmethod
    def _random_level(cls)->int:
        ans = 1
        while( SkipList._flip_coin() and ans <= 100 ):
            ans += 1

        return ans


    def delete(self, key:int)->None:
        node = self.search(key)
        while(node is not None):
            SkipList._delete_node(node)
            node = node.above


    @classmethod
    def _delete_node( cls, node:'NodeSkipList' )->None:
        if( node.right is not None ):
            node.right.left = node.left
        if( node.left is not None ):
            node.left.right = node.right
        if( node.bellow is not None ):
            node.bellow.above = node.above
        if( node.above is not None ):
            node.above.bellow = node.bellow


    def search( self, key:int )->any:
        if( self.length == 0 ):
            return None
        node = self._search(key)
        if(node.key == key):
            return node
        return None


    #@dispatch(int)
    def _search_per_index(self, index:int)->'NodeSkipList':
        node = self.down_left.right
        for _ in range(index):
            node = node.right

        return node


    @dispatch(int)
    def _search( self, key:int )->'NodeSkipList':
        node = self._search( self.upper_left, key )
        return node


    #@dispatch(object,int)
    @classmethod
    def _search( cls, node:'NodeSkipList', key:int )->'NodeSkipList':
        if( node.right.key <= key ):
            return BTree._search( node.right, key )
        if( node.bellow is not None ):
            return BTree._search( node.bellow, key )
        return node


    def _increase_one_level( self ) -> None:
        left_top = NodeSkipList(BEGINNING_OF_LIST)
        right_top = NodeSkipList(END_OF_LIST)
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
            self._increase_one_level()


    @classmethod
    def create_node_chaining(cls, key:int, number_of_levels:int)->'NodeSkipList':
        bottom = NodeSkipList(key)
        node = bottom
        for i in range(number_of_levels-2):
            next_node = NodeSkipList(key)
            node.above = next_node
            next_node.bellow = node
            node = next_node
        return bottom


    @classmethod
    def link_node_chain(cls, to_be_inserted:'NodeSkipList', list_node:'NodeSkipList')->None:
        while(to_be_inserted is not None and list_node is not None):
            other_node = list_node.right
            list_node.right = to_be_inserted
            to_be_inserted.left = list_node
            other_node.left = to_be_inserted
            to_be_inserted.right = other_node
            to_be_inserted = to_be_inserted.above
            list_node = SkipList.get_above_level_node(list_node)


    @classmethod
    def get_above_level_node(cls, node:'NodeSkipList')->'NodeSkipList':
        if(node.above is not None):
            return node.above
        while(node.above is None and node.left is not None):
            node = node.left
        if(node.above is None):
            raise Exception('end of the road')
        return node.above


    #@dispatch((int,float), any)
    def insert( self, key:int, element:any )->None:
        if(key in self):
            raise Exception("Operation not permitted, no repetitions are allowed.")
        node = self._search(key)
        self.insert(key,node, element)


    @classmethod
    def attach_element_to_node_chain( cls, node:'NodeSkipList', element:any ):
        element_node = NodeSkipList(element)
        element_node.parent = node
        node.bellow = element_node


    #@dispatch((int,float), object, any)
    def insert( self, key:int, node:'NodeSkipList', element:any )->None:
        node_level = SkipList._random_level()
        self._adjust_tree_level(node_level+1)
        to_be_inserted = SkipList.create_node_chaining(key, node_level)
        BTree.link_node_chain( to_be_inserted, node )
        BTree.attach_element_to_node_chain( node, element )
        self.length += 1


    def split(self):
        pass


    def get(self, key):
        pass



