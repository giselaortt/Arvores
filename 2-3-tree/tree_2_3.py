from copy import deepcopy
from multipledispatch import dispatch


class Node():

    def __init__( self, key, parentNode = None ):
        self.children =  [ None, None, None ]
        self.keys = [ key ]
        self.numberOfChildren = 0
        self.numberOfKeys = 1


    def __eq__( self, other ):

        return self.keys[0] == other.keys[0]


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


    def isTwoNode( self ):

        return ( self.children[0] is not None and self.children[1] is None )


    def insertChild( self, child ):
        if( not child ):
            return
        child.parent = self
        if( node.keys[0] > self.keys[ self.numberOfKeys-1 ] ):
            node.children[ self.numberOfKeys ] = child
        if( node.keys[0] < self.keys[ 0 ] ):
            node.children[ 0 ] = child
        node.children[ 1 ] = child


    def addKey( self, newKey ):
        if( numberOfChildren == 2 ):
            raise Exception( "This operation is not permitted" )
        self.keys.append(newKey)
        self.keys.sort()
        children = deepcopy(self.children)
        self.children = [None, None, None]
        for child in children:
            self.insertChild( child )


    @dispatch( object, int )
    def transformToThreeNode( self, newKey ):
        pass


    @dispatch( object, object )
    def transformToThreeNode( self, newKey ):
        pass


    def removeChild( self, key ):
        if( node.children[2].key == key ):
            node.children[2] = None

        elif( node.children[0].key == key ):
            node.children[0] = None

        elif( node.children[1] == key ):
            node.middle = None


    def __repr__( self ):

        return str( self.keys[0] ) + " " + str( self.keys[2] )


class Trees_2_3():

    def __init__( self ):
        self.root = None


    def search( self, key ):

        return _searchRecursion( key, self.root )


    def _searchRecursion( key, node ):
        #TODO: consider the 3 node case!!
        if( node is None ):
            return None

        if( node.keys[2] == key ):
            return node

        if( key < node.keys[2] ):
            return _searchRecursion( key, node.children[0] )

        if( node.keys[0] is None or key > node.keys[0] ):
            return _searchRecursion( key, node.children[2] )

        return _searchRecursion( key, node.middle )


    def _insertOnThreeNode( node, newNode ):
        keys = [node.keys[2], node.keys[0], newNode.keys[2] ]
        children = []
        keys.sort
        node.parent.removeChild( node.key )
        newLeftNode     = Node( keys[0],  )
        newRightNode    = Node( keys[2],  )


    def insert( self, key ):
        if( root is None ):
            node = Node( key )
            root = node
            return

        node = _findNodeToInsert( key, self.root )
        if( node.isTwoNode() ):
            node.transformToThreeNode( key )
            return

        if( node.parent == None ):
            newLeftNode = Node(node.keys[2], parentNode = node)
            newRightNode = Node(node.keys[0], parentNode = node)
            node.keys[2], node.keys[0] = key, None
            node.children[0] = newLeftNode
            node.children[2] = newLeftNode
            return

        if( node.parent.isTwoNode ):
            keys = [node.keys[2], node.secondkey, key]
            keys.sort()
            x,y,z = keys
            newLeftNode = Node(x, parentNode = node.parent)
            newRightNode = Node(z, parentNode = node.parent)
            node.parent.secondkey = y
            if( node.keys[2] < node.parent.key ):
                node.parent.children[0] = newLeftNode
                node.parent.middle = newRightNode
            else:
                node.parent.children[2] = newRightNode
                node.parent.middle = newLeftNode
            return

        #while( node.isThreeNode() ):
            #insert on three node

            #node = node.parent



    def _findNodeToInsert( key, node ):
        #TODO: throw error if key alredy exists or node is none
        if( key < node.keys[2] ):
            if( node.children[0] is None ):
                return node
            else:
                return _findNodeToInsert( key, node.children[0] )

        if( node.keys[0] is None or key > node.keys[0] ):
            if( node.children[2] is None ):
                return node
            else:
                return _findNodeToInsert( key, node.children[2] )

        if( key > node.keys[2] and key < node.keys[0] ):
            return _findNodeToInsert( key, node.middle )


    def remove( self, key ):
        pass


if __name__ == '__main__':
    node = Node(5)
    print(node)



