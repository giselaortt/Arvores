import random
from typing import Type, Union
from collections import deque
import pytest
from multipledispatch import dispatch


END_OF_LIST = float('inf')
BEGINNING_OF_LIST = float('-inf')


class NodeMapSkipList:
    right:'NodeMapSkipList' = None
    left:'NodeMapSkipList' = None
    above:'NodeMapSkipList' = None
    bellow:['NodeMapSkipList'] = None
    key:int
    element:any
    level:int = 1


    def __next__( self ) -> 'NodeMapSkipList':
        if( self.right is not None ):
            return self.right
        raise StopIteration()


    def __iter__( self ):

        return self


    def __init__( self, key:int, element:any=None ):
        self.key = key
        self.element = element


    def __lt__( self, key:int ):

        return self.key <= key


    def __gt__( self, key:int ):

        return self.key >= key


    def __le__( self, key:int ):

        return self.key <= key


    def __ge__( self, key:int ):

        return self.key >= key


    def __ne__( self, key:int ):

        return self.key != key


    def __repr__(self):
        #node_str = "  {1}\n{2}  <{0}>  {3}\n  {4}\n"
        node_str = "{1} {2} <{0}> {3} {4}"
        above = (self.above.key,self.above.element) if self.above else None
        bellow = (self.bellow.key,self.bellow.element) if self.bellow else None
        right = (self.right.key,self.right.element) if self.right else None
        left = (self.left.key,self.left.element) if self.left else None

        return  node_str.format( (self.key,self.element), above, left, right, bellow )


class MapSkipList:

    def __init__( self ):
        self.upper_left:'NodeMapSkipList' = NodeMapSkipList(BEGINNING_OF_LIST)
        self.upper_right:'NodeMapSkipList' = NodeMapSkipList(END_OF_LIST)
        self.down_left:'NodeMapSkipList' = self.upper_left
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
            ans += "("+str(node.key)+", "+str(node.element)+") "
            node = node.right

        return ans


    def __iter__( self ):

        return self.down_left


    def __contains__( self, key:int ):
        node = self.down_left
        if(node.key == key):
            return True
        while(node.right is not None):
            node = node.right
            if(node.key == key):
                return True
        return False


    def __eq__( self, other:'MapSkipList' )->bool:

        return str(self) == str(other)


    def __getitem__( self, index ):
        if isinstance(index, int):
            if index < 0 :
                index = len(self) + index
            node  = self._search_per_index(index)
            return node.key

        elif isinstance(index, tuple):
            node = self.down_left
            answer = MapSkipList()
            ind = 0
            while(node != END_OF_LIST):
                node = next(node)
                if(ind in index):
                    answer.insert(node.key, node.element)
                ind += 1
            return answer

        elif isinstance(index, slice):
            index.stop
            answer = MapSkipList()
            node = self.down_left
            node = next(node)
            answer_node_ptr = answer.down_left
            for i in range(0,index.start):
                node = next(node)
            for i in range(index.stop - index.start):
                answer.insert(node.key, node.element, answer_node_ptr)
                node = next(node)
                answer_node_ptr = next(answer_node_ptr)
            return answer
        else:
            raise ValueError(f'MapSkipList cannot be indexed with values of type {type(index)}')


#    def __delitem__(key):
#        pass
#
#
    def __add__( self, other:'MapSkipList')->'MapSkipList':
        first = self.down_left.right
        second = other.down_left.right
        return_list = MapSkipList()
        return_list_node = return_list.down_left
        while(first != END_OF_LIST or second != END_OF_LIST):
            if( first < second ):
                return_list.insert( first.key, first.element, return_list_node )
                first = next(first)
                return_list_node = next(return_list_node)
            elif( second < first ):
                return_list.insert( second.key, second.element, return_list_node )
                second = next(second)
                return_list_node = next(return_list_node)
            elif( first == second ):
                return_list.insert( second.key, second.element, return_list_node )
                first = next(first)
                second = next(second)
                return_list_node = next(return_list_node)

        return return_list


    def __iadd__( self, other:'MapSkipList', deep_copy:bool=True )->None:
        first = self.down_left
        second = other.down_left.right
        self._adjust_tree_level(other.number_of_levels)
        while( second != END_OF_LIST):
            if( second > first and second < first.right ):
                self.insert( second.key, second.element, first )
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
    def _random_level(cls) -> int:
        ans = 1
        while( MapSkipList._flip_coin() and ans <= 100 ):
            ans += 1

        return ans


    def delete(self, key:int) -> None:
        node = self.search(key)
        while(node is not None):
            MapSkipList._delete_node(node)
            node = node.above


    @classmethod
    def _delete_node( cls, node:'NodeMapSkipList' ) -> None:
        if( node.right is not None ):
            node.right.left = node.left
        if( node.left is not None ):
            node.left.right = node.right
        if( node.bellow is not None ):
            node.bellow.above = node.above
        if( node.above is not None ):
            node.above.bellow = node.bellow


    def search( self, key:int ) -> any:
        if( self.length == 0 ):
            return None
        node = self._search(key)
        if(node.key == key):
            return node
        return None


    def _search_per_index(self, index:int)->'NodeMapSkipList':
        node = self.down_left.right
        for _ in range(index):
            node = node.right

        return node


    @dispatch(int)
    def _search( self, key:int )->'NodeMapSkipList':
        node = self._search( self.upper_left, key )
        return node


    @dispatch(object,int)
    def _search( self, node:'NodeMapSkipList', key:int )->'NodeMapSkipList':
        if( node.right.key <= key ):
            return self._search( node.right, key )
        if( node.bellow is not None ):
            return self._search( node.bellow, key )
        return node


    def _increase_one_level( self ) -> None:
        left_top = NodeMapSkipList(BEGINNING_OF_LIST)
        right_top = NodeMapSkipList(END_OF_LIST)
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
    def create_node_chaining(cls, key:int, element:any, number_of_levels:int) -> 'NodeMapSkipList':
        bottom = NodeMapSkipList(key, element)
        node = bottom
        #why -2 ??
        for i in range(number_of_levels-2):
            next_node = NodeMapSkipList(key,element)
            node.above = next_node
            next_node.bellow = node
            node = next_node
        return bottom


    @classmethod
    def link_node_chain(cls, to_be_inserted:'NodeMapSkipList', list_node:'NodeMapSkipList')->None:
        while(to_be_inserted is not None and list_node is not None):
            other_node = list_node.right
            list_node.right = to_be_inserted
            to_be_inserted.left = list_node
            other_node.left = to_be_inserted
            to_be_inserted.right = other_node
            to_be_inserted = to_be_inserted.above
            list_node = MapSkipList.get_above_level_node(list_node)


    @classmethod
    def get_above_level_node(cls, node:'NodeMapSkipList') -> 'NodeMapSkipList':
        if(node.above is not None):
            return node.above
        while(node.above is None and node.left is not None):
            node = node.left
        if(node.above is None):
            raise Exception('end of the road')
        return node.above


    @dispatch(int,object)
    def insert( self, key:int, element:any ) -> None:
        if(key in self):
            raise Exception("Operation not permitted, no repetitions are allowed.")
        node = self._search(key)
        self.insert(key, element, node)


    @dispatch((int,float),object,object)
    def insert( self, key:int, element:any, node:'NodeMapSkipList' ) -> None:
        node_level = MapSkipList._random_level()
        self._adjust_tree_level( node_level+1 )
        to_be_inserted = MapSkipList.create_node_chaining( key, element, node_level )
        MapSkipList.link_node_chain( to_be_inserted, node )
        self.length += 1



#    def get(self, key:int):
#        pass
#
#
#    def set(self, key:int, newValue:any)->None:
#        pass
#

