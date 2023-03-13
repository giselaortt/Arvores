from copy import deepcopy
from multipledispatch import dispatch
import collections
from array import array
from typing import Type
from skip_list import SkipList


class NodeBTree():
    precision = 0.00001

    def __init__( self, key:int, parentNodeBTree:'NodeBTree' = None, children:list = None, max_len:int = 10 ):
        self.keys = SkipList( )
        self.keys.insert( key )
        self.numberOfChildren = 0
        self.parent = parentNodeBTree
        if( children is not None ):
            #deep copy is important!
            self.children = list(children)
            for child in children:
                child.parent = self
        else:
            self.children = None
        self.max_len = max_len



    
    def isLeaf( self ) -> bool:

        return ( self.children is None )


    @dispatch( object )
    def __eq__( self, other:'NodeBTree' ):

        return (self.keys == other.keys)


    def __repr__( self ):

        return "["+ ", ".join([str(value) for value in self.keys])+"]"


    def __len__( self ):

        return len(self.keys)


    def hasExceded( self ):

        return ( len(self.keys) >= self.max_len )


    @dispatch( (int,float) )
    def __contains__( self, value:int ):

        return ( value in self.keys )


    @dispatch(int)
    def insert( self, key:int ) -> None:
       self.keys.insert(key)


    def promoteChild( self, child:'None' )->None:
       raise NotImplementedError


    def split( self ):
        right_child = SkipList()
        left_child = SkipList()
        middle = len(slef/2)
        right_child.keys = self.keys[0:len(self/2)]
        left_child.keys = self.keys[len(self/2)+1:]
        self.key = self.keys[ len(self)/2 ]


class BTree():

    def __init__( self ):
        self.root = None


    def __contains__( self, key:int ) -> bool:

        return ( self.search( key ) is not None )


    def __repr__( self ):
        if( self.root is None ):
            return "< >"
        #ans = "<"+ " ".join([str(node) for node in self.pre_order()])+">"
        ans = "<"+ " ".join([str(self.pre_order())])+">"
        return ans


    def pre_order( self ) -> list:
        if(self.root is None):
            return []
        answer = []
        BTree._pre_order(self.root, answer)
        return answer


    @staticmethod
    def _pre_order( node:'NodeBTree', answer:list ) -> list:
        pass


    def isEmpty( self ):

        return ( self.root is None )


    def search( self, key:int ) -> 'NodeBTree':
        if( self.isEmpty() ):
            return None
        node = BTree._search( key, self.root )
        if(key in node):
            return node
        return None


    def _findNodeBTreeToInsert( self, key:int ) -> 'NodeBTree':
        node = BTree._search( key, self.root )
        if( key in node ):
            raise Exception("Operation not allowed.")
        return node


    @staticmethod
    def _search( key:int, node:'NodeBTree' ) -> 'NodeBTree':
        if( type(node) is not NodeBTree ):
            raise TypeError('expected type NodeBTree')
        if( key in node or node.isLeaf() ):
            return node
        """
        if( key < node.keys[0] ):
            return BTree._search( key, node.children[0] )
        if( node.isThreeNodeBTree() and key > node.keys[1] ):
            return BTree._search( key, node.children[2] )
        return BTree._search( key, node.children[1] )
        """


    def insert( self, key:int ) -> None:
        if( self.root is None ):
            self.root = NodeBTree( key )
            return
        node = self._findNodeBTreeToInsert( key )
        node.insert(key)
        self.bubbleUp(node)


    def bubbleUp( self, node:'NodeBTree' ) -> None:
        while(node.hasExceded()):
            node.split()
            if(node.parent is not None):
                node.parent.removeChild( node )
                node.parent.insert( node )
                node = node.parent


    def remove( self, key ):
        pass







