from copy import deepcopy
from multipledispatch import dispatch


class Node():

    precision = 0.00001

    def __init__( self, key:int, parentNode = None ):
        #making a list instead of assigning the children manually will make it easier to adpt for a b-tree in the future
        self.children =  [None, None, None, None]
        #should it be a deque instead ?
        self.keys = [ key ]
        self.numberOfChildren = 0
        self.parent = parentNode


    def isLeaf( self ) -> bool:

        #return ( self.children[0] is None and self.children[1] is None and self.children[2] is None )
        return (self.numberOfChildren==0)


    @dispatch( int )
    def __eq__( self, other:int ):

        return self.keys[0] == other


    @dispatch( object )
    #needs reimplementation
    def __eq__( self, other:object ):

        return  self.keys == other.keys


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


    def __le__( self, other ):
        if( other is None ):
            return False

        return self.keys[0] <= other.keys[0]


    def __repr__( self ):

        return str( self.keys )


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
            self.children[2]=child


    def insertKey( self, key:int ) -> None:
        self.keys.append(key)
        self.keys.sort()


    def getSecondtKey( self ) -> int:
        if( len(self.keys) == 1 ):
            raise Exception( "This operation is not permitted" )
        return self.keys[1]


    def getFirstKey( self ) -> int:
        return self.keys[0]


    def removeChild( self, child:object ) -> None:
        for i in range( len(self.children) ):
            if( self.children[i] == child ):
                self.children[i] = None


    def isFistChild():
        pass


    def isSecondChild():
        pass


    def isThirdChild( self ):
        pass


    def split( self ):
        newLeftNode = Node( self.keys[0] )
        newRightNode = Node( self.keys[2] )
        newLeftNode.children = self.children[0:2]
        newRightNode.children = self.children[2:4]
        self.children = [newLeftNode, newRightNode]
        self.keys = [self.keys[1]]


    def insertNode( self ):
        pass


class Tree_2_3():

    def __init__( self ):
        self.root = None


    def __repr__( self ):
        pass


    def __contains__( self, key:int ) -> bool:

        return ( self.search( key ) is not None )


    def isEmpty( self ):

        return ( self.root is None )


    def search( self, key:int ) -> Node:

        return Tree_2_3._search( key, self.root )


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
        print("k = ", node.keys)
        node.split()

        if(node.parent is not None):
            parent = node.parent
            if( node.parent is not None ):
                node.parent.removeChild( node )
            node.parent = None
            parent.insertNode( node )


    def _insertOnThreeNode( node, newNode ):
        node.parent.removeChild( node )


    @staticmethod
    def _findNodeToInsert( key, node ):
        if( node is None ):
            raise Exception("Unexpected error occured.")

        if( key in node ):
            raise Exception("Operation not allowed.")

        if( node.isLeaf() ):
            return node

        if( key < node.keys[0] ):
            return Tree_2_3._findNodeToInsert( key, node.children[0] )

        if( node.isThreeNode() and key > node.keys[1] ):
            return Tree_2_3._findNodeToInsert( key, node.children[2] )

        return Tree_2_3._findNodeToInsert( key, node.children[1] )


    def remove( self, key ):
        pass


if __name__ == '__main__':
    node = Node(5)
    print(node)



