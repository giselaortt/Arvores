from copy import deepcopy
from multipledispatch import dispatch
import collections

class Node():

    precision = 0.00001

    def __init__( self, key:int, parentNode = None ):
        #making a list instead of assigning the children manually will make it easier to adpt for a b-tree in the future
        #should it be a deque instead ?
        self.children =  [None, None]
        self.keys = [ key ]
        self.numberOfChildren = 0
        self.parent = parentNode


    def isLeaf( self ) -> bool:

        return ( self.children[0] is None and self.children[1] is None )


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


    def insertChild( self, child:object ) -> bool:
        key = child.keys[0]
        self.numberOfChildren += 1
        if( key < self.keys[0] ):
            self.children[0] = child
        elif( self.isTwoNode() or key < self.keys[1] ):
            self.children[1]=child
        else:
            self.children.append(child)


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
        for i in range( len(self.children) ):
            if( self.children[i] is child ):
                del self.children[i]


    def isFistChild():
        pass


    def isSecondChild():
        pass


    def isThirdChild( self ):
        pass


    def split( self ):
        newLeftNode = Node( self.keys[0], parentNode = self )
        newRightNode = Node( self.keys[2], parentNode = self )
        if( not self.isLeaf() ):
            print( "children ",  self.children )
            newLeftNode.children = self.children[0:2]
            newRightNode.children = self.children[2:4]
        self.children = [newLeftNode, newRightNode]
        self.keys = [self.keys[1]]


    #not covered
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


class Tree_2_3():

    def __init__( self ):
        self.root = None


    def __repr__( self ):
        if( self.root is None ):
            return None.__repr__()
        ans = ""
        queue = collections.deque()
        queue.append(self.root)
        while( len(queue) > 0 ):
            nextNode = queue.popleft()
            for child in nextNode.children:
                if child is not None:
                    queue.append(child)
            ans += " " + nextNode.__repr__()

        return ans


    def __contains__( self, key:int ) -> bool:

        return ( self.search( key ) is not None )


    def isEmpty( self ):

        return ( self.root is None )


    def search( self, key:int ) -> Node:

        return Tree_2_3._search( key, self.root )


    #not covered
    @staticmethod
    def _search( key, node ) -> Node:
        if( node is None ):
            return None
        if( key in node ):
            return node
        if( node.isLeaf() ):
            return None
        if( key < node.keys[0] ):
            return _search( key, node.children[0] )
        if( node.isThreeNode() and key > node.keys[1] ):
            return _search( key, node.children[2] )
        return _search( key, node.children[1] )


    def insert( self, key:int ) -> None:
        if( self.root is None ):
            self.root = Node( key )
            return
        node = Tree_2_3._findNodeToInsert( key, self.root )
        if( node.isTwoNode() ):
            node.insertKey( key )
            return
        node.insertKey(key)
        node.split()
        #not covered
        if(node.parent is not None):
            parent = node.parent
            node.parent.removeChild( node )
            node.parent = None
            parent.insertNode( node )
            if( parent.parent is not None and parent.hasExceded() ):
                self.bubbleUp(parent)


    def bubbleUp( self, node:object ) -> None:
        node.split()
        while( node.parent is not None ):
            node.parent.removeChild(node)
            node.parent.insertNode( node )
            if( node.parent.hasExceded() ):
                node.parent.split()
                node = node.parent


    @staticmethod
    def _findNodeToInsert( key, node ) -> object:
        if( node is None ):
            raise Exception("Unexpected error occured.")
        if( key in node ):
            raise Exception("Operation not allowed.")
        if( node.isLeaf() ):
            return node
        #not covered
        if( key < node.keys[0] ):
            return Tree_2_3._findNodeToInsert( key, node.children[0] )
        if( node.isThreeNode() and key > node.keys[1] ):
            return Tree_2_3._findNodeToInsert( key, node.children[2] )
        return Tree_2_3._findNodeToInsert( key, node.children[1] )


    def remove( self, key ):
        pass


if __name__ == '__main__':
    tree = Tree_2_3()
    tree.insert( 0 )
    tree.insert( 1 )
    tree.insert( 2 )
    tree.insert( 3 )
    tree.insert( 4 )
    tree.insert( 5 )
    tree.insert( 6 )
    tree.insert( 7 )
    tree.insert( 8 )
    tree.insert( 9 )
    tree.insert( 10 )
    tree.insert( 11 )
    tree.insert( 12 )
    tree.insert( 13 )
    tree.insert( 14 )
    print(tree.root)
    print(tree.root.children)
    print(tree)
    """
    """
    #print(tree.root)
    #print(tree.root.children)



