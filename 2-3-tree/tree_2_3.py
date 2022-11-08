from copy import deepcopy
from multipledispatch import dispatch
import collections


class Node():
    precision = 0.00001
    def __init__( self, key:int, parentNode:object = None, children:list = None ):
        #making a list instead of assigning the children manually will make it easier to adpt for a b-tree in the future
        #should it be a deque instead ?
        self.keys = [ key ]
        self.numberOfChildren = 0
        self.parent = parentNode
        self.children = children
        if( children is not None ):
            for child in children:
                child.parent = self


    def isLeaf( self ) -> bool:
        return ( self.children is None )


    @dispatch( int )
    def __eq__( self, other:int ):
        return self.keys[0] == other


    @dispatch( object )
    #needs reimplementation
    def __eq__( self, other:object ):
        return (self.keys == other.keys)


    def __ne__( self, other ):
        return self.keys[0] != other.keys[0]


    def __gt__( self, other ):
        if( other is None ):
            return True
        return self.keys[0] > other.keys[0]


    def __ge__( self, other ):
        if( other is None ):
            return True
        return self.keys[0] >= other.keys[0]


    def __lt__( self, other ):
        if( other is None ):
            return False
        return self.keys[0] < other.keys[0]


    def __repr__( self ):
        return str( self.keys )


    def hasExceded( self ):
        return ( len(self.keys) >= 3 )


    @dispatch( object )
    def __contains__( self, other:object ):
        for child in self.children:
            if child is other:
                return True
        return False


    @dispatch( int )
    def __contains__( self, value:int ):
        return ( value in self.keys )


    def isTwoNode( self ) -> bool:
        return len(self.keys)==1


    def isThreeNode( self ) -> bool:
        return len(self.keys) == 2


    def insertKey( self, key:int ) -> None:
        self.keys.append(key)
        self.keys.sort()


    #not covered
    def getSecondtKey( self ) -> int:
        if( len(self.keys) == 1 ):
            raise Exception( "This operation is not permitted" )
        return self.keys[1]


    def getFirstKey( self ) -> int:
        return self.keys[0]


    def removeChild( self, child:object ) -> None:
        if( self.children is None ):
            return
        for i in range( len(self.children) ):
            if( self.children[i] is child ):
                del self.children[i]
                return


    def split( self ):
        newLeftNode = Node( self.keys[0], parentNode = self )
        newRightNode = Node( self.keys[2], parentNode = self )
        if( not self.isLeaf() ):
            newLeftNode.children = self.children[0:2]
            newRightNode.children = self.children[2:4]
        if( not self.isLeaf() ):
            self.children[0].parent = newLeftNode
            self.children[1].parent = newLeftNode
            self.children[2].parent = newRightNode
            self.children[3].parent = newRightNode
        self.children = [newLeftNode, newRightNode]
        self.keys = [self.keys[1]]


    def insertNode( self, node:object )->None:
        if( node.keys[0] < self.keys[0] ):
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


class Tree_2_3():

    def __init__( self ):
        self.root = None


    def __repr__( self ):
        if( self.root is None ):
            return "< >"
        ans = ""
        queue = collections.deque()
        queue.append(self.root)
        while( len(queue) > 0 ):
            nextNode = queue.popleft()
            if( nextNode.children is not None ):
                queue.extend(nextNode.children)
            ans += " " + nextNode.__repr__()

        return ans


    def __contains__( self, key:int ) -> bool:

        return ( self.search( key ) is not None )


    def isEmpty( self ):

        return ( self.root is None )


    def search( self, key:int ) -> Node:
        if( self.isEmpty() ):
            return None
        node = Tree_2_3._search( key, self.root )
        if(key in node):
            return node
        return None


    def _findNodeToInsert( self, key:int ) -> object:
        node = Tree_2_3._search( key, self.root )
        if( node is None ):
            raise Exception("Unexpected error occured.")
        if( key in node ):
            raise Exception("Operation not allowed.")
        return node


    @staticmethod
    def _search( key:int, node:object ) -> Node:
        if( node is None ):
            return None
        if( key in node or node.isLeaf() ):
            return node
        if( key < node.keys[0] ):
            return Tree_2_3._search( key, node.children[0] )
        if( node.isThreeNode() and key > node.keys[1] ):
            return Tree_2_3._search( key, node.children[2] )
        return Tree_2_3._search( key, node.children[1] )


    def insert( self, key:int ) -> None:
        if( self.root is None ):
            self.root = Node( key )
            return
        node = self._findNodeToInsert( key )
        node.insertKey(key)
        while( node.hasExceded() ):
            node.split()
            if(node.parent is not None):
                node.parent.removeChild( node )
                node.parent.insertNode( node )
                node = node.parent


    def bubbleUp( self, node:object ) -> None:
        pass


    def remove( self, key ):
        pass


if __name__ == '__main__':
    tree = Tree_2_3()
    for key in range(8):
        tree.insert( key )
        print(tree)
    print(tree.root)
    print(tree.root.children)
    print(tree)
    print(tree.search(6).parent)


