from copy import deepcopy
from multipledispatch import dispatch


class Node():

    def __init__( self, key, parentNode = None ):
        self.children =  [None, None, None]
        self.keys = [ key ]
        self.numberOfChildren = 0
        self.numberOfKeys = 1
        self.parent = parentNode


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
        pass


    def addKey( self, newKey ):
        if( self.numberOfKeys == 2 ):
            raise Exception( "This operation is not permitted" )
        self.numberOfKeys += 1
        if( newKey > self.keys[0] ):
            self.keys.append(newKey )
        else:
            self.keys.insert( 0, newKey )


    @dispatch( object, int )
    def transformToThreeNode( self, newKey ):
        if( not self.isTwoNode() ):
            raise Exception( "Ooops! Unexpected path." )
        self.numberOfKeys += 1
        self.keys.append(newKey)
        self.keys.sort()


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


    #should only be used for sppliting a node
    def addThirdKey( self, newKey ):
        self.numberOfKeys += 1
        self.keys.append(newKey)
        self.keys.sort()


    def split_node( self ):
        pass


    def __repr__( self ):

        return str( self.keys )


class Trees_2_3():

    def __init__( self ):
        self.root = None


    def search( self, key ):

        return _searchRecursion( key, self.root )


    def _searchRecursion( key, node ):
        if( node is None ):
            return None

        if( key in node.keys ):
            return node

        if( key < node.keys[0] ):
            return _searchRecursion( key, node.children[0] )

        if(  key > node.keys[1] ):
            return _searchRecursion( key, node.children[2] )

        return _searchRecursion( key, node.children[1] )


    def insert( self, key ):
        if( self.root is None ):
            self.root = Node( key )
            return

        node = _findNodeToInsert( key, self.root )
        if( node.isTwoNode() ):
            node.transformToThreeNode( key )
            return

        if( node.parent == None ):
            node.addThirdKey( key )
            newLeftNode = Node(node.keys[0], parentNode = node)
            newRightNode = Node(node.keys[2], parentNode = node)
            del(node.keys[2]), del(node.keys[0])
            node.children[0] = newLeftNode
            node.children[1] = newLeftNode
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




    def _insertOnThreeNode( node, newNode ):
        keys = [node.keys[2], node.keys[0], newNode.keys[2] ]
        children = []
        keys.sort
        node.parent.removeChild( node.key )
        newLeftNode     = Node( keys[0],  )
        newRightNode    = Node( keys[2],  )


    def _findNodeToInsert( key, node ):
        if( node is None ):
            raise Exception("Unexpected error occured.")

        if( key in node.keys ):
            raise Exception("Operation not allowed.")

        if( node.numberOfChildren == 0 ):
            return node

        if( key < node.keys[0] ):
            return _findNodeToInsert( key, node.children[0] )

        if( key > node.keys[1] ):
            return _findNodeToInsert( key, node.children[2] )

        return _findNodeToInsert( key, node.children[1] )


    def remove( self, key ):
        pass


if __name__ == '__main__':
    node = Node(5)
    print(node)



