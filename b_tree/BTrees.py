from copy import deepcopy
from multipledispatch import dispatch
import collections
from array import array
from typing import Type
import sys
from bisect import bisect_left
from bisect import bisect_right



class NodeBTree():
    precision = 0.00001
    max_len = 20


    def __init__( self, parent:'NodeBTree'=None, keys:list=None, children:list=None ):
        self.parent = parent
        if(keys is not None):
            self.keys = list(keys)
        else:
            self.keys:list = []
        if(children is not None):
            self.children = list(children)
        else:
            self.children:list = []


    def isLeaf( self ) -> bool:

        return len(self.children)==0


    def __repr__( self ):

        return str(self.keys)


    def __len__( self ):

        return len(self.keys)


    def hasExceded( self ):

        return ( len(self.keys) > self.max_len )


    @dispatch( (int,float) )
    def __contains__( self, value:int ):

        return ( value in self.keys )


    @dispatch(int)
    def insert( self, key:int ) -> None:
       self.keys.append(key)
       self.keys.sort()
       if( self.hasExceded() ):
           self._split()


    @dispatch(object)
    def insert( self, node:'NodeBTree' ) -> None:

        raise NotImplementedError


    def _get_child( self, index:int ):

        raise NotImplementedError


    def _promoteChild( self, child:'None' )->None:

        raise NotImplementedError


    def split( self ):

        raise NotImplementedError


    def _split( self ):
        pointer = self.keys
        middle = int(len(self.keys)/2)
        self.keys = [ self.keys[middle] ]
        left = NodeBTree( parent=self, keys=pointer[0:middle])
        right = NodeBTree( parent=self, keys=pointer[middle+1:])
        if( self.isLeaf() ):
            self.children = [left,right]
        else:
            raise NotImplementedError


class BTree():

    def __init__( self ):
        self.root = None


    def __contains__( self, key:int ) -> bool:

        return ( self.search(key) is not None )


    def __repr__( self ):
        if( self.root is None ):
            return "< >"
        ans = "<" + " ".join([str(self.pre_order())]) + ">"

        return ans


    def insert( self, key:int ) -> None:
        if( self.root is None ):
            self.root = NodeBTree( )
            self.root.insert(key)
            return
        node = self._findNodeToInsert( key )
        node.insert(key)
        self.bubbleUp(node)


    def _findNodeToInsert( self, key:int ) -> 'NodeBTree':
        node = BTree._search( key, self.root )
        if( key in node ):
            raise Exception("Operation not allowed.")
        return node


    def bubbleUp( self, node:'NodeBTree' ) -> None:
        while(node.hasExceded()):
            node.split()
            if( node is not self.root ):
                node.parent.removeChild( node )
                node.parent.insert( node )
                node = node.parent


    def search( self, key:int ) -> 'NodeBTree':
        if( self.isEmpty() ):
            return None
        node = BTree._search( key, self.root )
        if(key in node):
            return node
        return None


    @staticmethod
    def _search( key:int, node:'NodeBTree' ) -> 'NodeBTree':
        if( type(node) is not NodeBTree ):
            raise TypeError('expected type NodeBTree')
        if( key in node or node.isLeaf() ):
            return node
        pos = bisect_right(node.keys, key)
        return BTree._search(key,node.children[ pos ])


    def pre_order( self ) -> list:
        if(self.root is None):
            return []
        answer = []
        BTree._pre_order(self.root, answer)

        return answer


    @staticmethod
    def _pre_order( node:'NodeBTree', answer:list ) -> list:
        answer.append( node )
        if( not node.isLeaf() ):
            for child in node.children:
                BTree._pre_order( child, answer )


    def isEmpty( self ):

        return ( self.root is None )


    def remove( self, key ):
        pass


    def _merge(self, node, other):
        pass



