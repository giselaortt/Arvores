
from copy import deepcopy
from multipledispatch import dispatch
import collections
from array import array
from typing import Type
import skip_list


class Node():
    precision = 0.00001

    def __init__( self, key:int, parentNode:'Node' = None, children:list = None, max_len:int = 10 ):
        self.keys = skip_list( )
        self.keys.insert( key )
        self.numberOfChildren = 0
        self.parent = parentNode
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
    def __eq__( self, other:'Node' ):
        pass
        #implement it on the skip list first...
        #return (self.keys == other.keys)


    def __repr__( self ):
        return "["+ ", ".join([str(value) for value in self.keys])+"]"


    def hasExceded( self ):
        return ( len(self.keys) >= self.max_len )


    """@dispatch( object )
    def __contains__( self, other:'Node' ):
        if(self.children is None):
            return False
        #for child in self.children:
        #    if child is other:
        #        return True
        #return False
        pass
    """


    @dispatch( int )
    def __contains__( self, value:int ):
        return ( value in self.keys )


    def isTwoNode( self ) -> bool:
        return len(self.keys)==1


    def isThreeNode( self ) -> bool:
        return len(self.keys) == 2


    def insertKey( self, key:int ) -> None:
        #should follow skip list insertion methods
        self.keys.insert(key)


    def removeChild( self, child:'None' ) -> None:
        if( self.children is None ):
            return
        for i in range( len(self.children) ):
            if( self.children[i] is child ):
                del self.children[i]
                return


    def split( self ):
        #newLeftNode = Node( self.keys[0], parentNode = self )
        #newRightNode = Node( self.keys[2], parentNode = self )
        if( not self.isLeaf() ):
            newLeftNode.children = self.children[0:2]
            newRightNode.children = self.children[2:4]
            #self.children[0].parent = newLeftNode
            #self.children[1].parent = newLeftNode
            #self.children[2].parent = newRightNode
            #self.children[3].parent = newRightNode
        self.children = [newLeftNode, newRightNode]
        #should be a definition of a new skip list
        #self.keys = [self.keys[1]]
        self.keys = SkipList()
        #self.keys.insert(self.keys[1])


    def insertNode( self, node:'Node' )->None:
        """if( node.keys[0] < self.keys[0] ):
            self.keys.insert( 0, node.keys[0] )
            self.children = node.children + self.children
        elif( node.keys[0] > self.keys[-1] ):
            self.keys.append( node.keys[0] )
            self.children.extend(node.children)
        else:
            self.keys.insert( 1, node.keys[0] )
            self.children = [self.children[0]]+node.children+[self.children[1]]
        for child in self.children:
            child.parent = self
        """


class BTree():

    def __init__( self ):
        self.root = None


    def __contains__( self, key:int ) -> bool:
        return ( self.search( key ) is not None )


    def __repr__( self ):
        if( self.root is None ):
            return "< >"
        ans = "<"+ " ".join([str(node) for node in self.pre_order()])+">"
        return ans


    def pre_order( self ) -> list:
        if(self.root is None):
            return []
        answer = []
        BTree._pre_order(self.root, answer)
        return answer


    @staticmethod
    def _pre_order( node:Type[Node], answer:list ) -> list:
        answer.append(node)
        if( node.children is None ):
            return
        for child in node.children:
            BTree._pre_order( child, answer )


    def isEmpty( self ):
        return ( self.root is None )


    def search( self, key:int ) -> Node:
        if( self.isEmpty() ):
            return None
        node = BTree._search( key, self.root )
        if(key in node):
            return node
        return None


    def _findNodeToInsert( self, key:int ) -> Type[Node]:
        node = BTree._search( key, self.root )
        if( key in node ):
            raise Exception("Operation not allowed.")
        return node


    @staticmethod
    def _search( key:int, node:Type[Node] ) -> Type[Node]:
        if( type(node) is not Node ):
            raise TypeError('expected type Node')
        if( key in node or node.isLeaf() ):
            return node
        """
        if( key < node.keys[0] ):
            return BTree._search( key, node.children[0] )
        if( node.isThreeNode() and key > node.keys[1] ):
            return BTree._search( key, node.children[2] )
        return BTree._search( key, node.children[1] )
        """


    def insert( self, key:int ) -> None:
        if( self.root is None ):
            self.root = Node( key )
            return
        node = self._findNodeToInsert( key )
        node.insertKey(key)
        self.bubbleUp(node)


    def bubbleUp( self, node:Type[Node] ) -> None:
        while(node.hasExceded()):
            node.split()
            if(node.parent is not None):
                node.parent.removeChild( node )
                node.parent.insertNode( node )
                node = node.parent


    def remove( self, key ):
        pass


