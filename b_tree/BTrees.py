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
    middle = 10 # should be (max_len / 2) +1


    def __init__( self, parent:'NodeBTree'=None, keys:list=None, children:list=None ):
        self.parent = parent
        if(keys is not None):
            self.keys = list(keys) #deep copy is important!
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


    def _get_child( self, index:int ):

        raise NotImplementedError


    def _promoteChild( self, child:'NodeBTree' )->None:
        if(len(child.keys) != 1):
            raise ValueError('')
        position = self.children.index(child)
        del self.children[position]
        self._insertChild( position, child.children[1] )
        self._insertChild( position, child.children[0] )
        self.keys.insert( position, child.keys[0] )


    def _insertChild( self, position:int, child:'NodeBTree' )->None:
        self.children.insert(position, child)
        child.parent = self


    def _split( self ):
        pointer = self.keys
        self.keys = [ self.keys[self.middle] ]
        left = NodeBTree( parent=self, keys=pointer[0:self.middle])
        right = NodeBTree( parent=self, keys=pointer[self.middle+1:])
        if( not self.isLeaf() ):
            left.children = list(self.children[0:self.middle+1])
            right.children = list(self.children[self.middle+1:])
        self.children = [left,right]


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



