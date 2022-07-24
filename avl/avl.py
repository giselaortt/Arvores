# -*- coding: utf-8 -*-


class Node:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.right = None
        self.left = None
        self.parent = None
        self.height = 1 #definirei a height de uma folha como 1


    def factor(self):
        if self.right is None and self.left is None:
            return 0
        if self.left is None:
            return -1 * self.right.height
        if self.right is None:
            return self.left.height
        return self.left.height - self.right.height


    def calculate_height( self ):
        if( self.right is None and self.left is None ):
            return 1
        if( self.right is None ):
            return self.left.height + 1
        if( self.left is None ):
            return self.right.height + 1
        if( self.right.height < self.left.height ):
            return self.left.height + 1
        else:
            return self.right.height + 1


"""
         y                               x
        / \     Right Rotation          /  \
       x   T3   - - - - - - - >        T1   y
      / \       < - - - - - - -            / \
     T1  T2     Left Rotation            T2  T3
"""
class AVL:
    def __init__(self):
        self.root = None


    def insert(self, id, name):
        novo = Node(id, name)
        if self.root is None:
            self.root = novo
        else:
            self._insert_recursion( self.root, novo )


    def _insert_recursion( self, node, novo_no):
        if node.id == novo_no.id:
            raise Exception("Repetitions are not allowed.")
            return
        if node.id < novo_no.id:
            if node.right is None:
                node.right = novo_no
                novo_no.parent = node
                self._redefine_height(novo_no.parent)
                self._balance_after_insertion(node)
            else:
                self._insert_recursion(node.right, novo_no)
        else:
            if(node.left is None):
                node.left = novo_no
                novo_no.parent = node
                self._redefine_height(novo_no.parent)
                self._balance_after_insertion(node)
            else:
                self._insert_recursion(node.left, novo_no)


    def _balance_after_insertion( self, node ):
        folha = node
        while( node != None ):
            if( node.factor()  >= 2):
                if( node.left.factor() == 1 ):
                    self._rotate_right( node )
                    self._redefine_height(folha)
                else: #left right case.
                    self._rotate_left( node.left )
                    self._rotate_right( node )
                break;
            elif( node.factor() <= -2 ):
                if( node.right.factor() == -1 ):
                    self._rotate_left( node )
                else: #right left case.
                    self._rotate_right(node.right)
                    self._rotate_left(node)
                break;
            node = node.parent


    def in_order( self, node ):
        if( node == None ):
            return
        self.in_order( node.left )
        print( node.id, end = ' ' )
        self.in_order( node.right )


    def pos_order( self, node ):
        if( node == None ):
            return
        self.pos_order( node.left )
        self.pos_order( node.right )
        print( node.id, end = ' ' )


    def pre_order( self, node ):
        if( node == None ):
            return
        print( node.id, end = ' ' )
        self.pre_order( node.left )
        self.pre_order( node.right )


    def search(self, id):
        return self._search(self.root, id)


    def _search(self, node, id):
        if node is None:
            return node
        if node.id == id:
            return node
        if id > node.id:
            return self._search(node.right, id)
        return self._search(node.left, id)


    def height( self ):
        return self._height( self.root )


    def _height( self, node ):
        if node is None:
            return 0
        return max( self._height(node.right), self._height(node.left) ) + 1


    def _is_avl( self, node ):
        if( node == None ):
            return True
        if( node.left is None and node.right is None ):
            return True
        left_height = 0
        right_height = 0
        if( node.left is not None ):
            left_height =  node.left.calculate_height()
        if( node.right is not None ):
            right_height = node.right.calculate_height()
        if( abs(left_height - right_height) >= 2 ):
            return False
        return (self._is_avl( node.right ) and self._is_avl( node.left ))


    def _rotate_right( self, node ):
        new_parent = node.left
        new_parent.parent = node.parent
        if(node is self.root):
            self.root = new_parent
        else:
            if( node.parent.id > node.id ):
                node.parent.left = new_parent
            else:
                node.parent.right = new_parent
        node.parent = new_parent
        node.left = new_parent.right
        if( new_parent.right is not None ):
            new_parent.right.parent = node
        new_parent.right = node
        self._redefine_height( node )


    def _rotate_left( self, node ):
        new_parent = node.right
        new_parent.parent = node.parent
        if(node is self.root):
            self.root = new_parent
        else:
            if( node.parent.id > node.id ):
                node.parent.left = new_parent
            else:
                node.parent.right = new_parent
        node.parent = new_parent
        node.right = new_parent.left
        if( new_parent.left is not None ):
            new_parent.left.parent = node
        new_parent.left = node
        self._redefine_height( node  )


    def _redefine_height( self, node ):
        if( node is None ):
            return
        nh = node.calculate_height()
        #if( nh == node.height ):
        #    return
        node.height = nh
        self._redefine_height(node.parent)


    def remove( self, id ):
        node = self.search( id )
        if node is None:
            raise Exception("id não encontrado")
            return

        if node.left is None and node.right is None:
            if node.parent is not None:
                if node.parent.right == node:
                    node.parent.right = None
                else:
                    node.parent.left = None
            else:
                self.root = None
            return

        if node.right is None:
            node.left.parent = node.parent
            if node is self.root:
                self.root = node.left
                node.left.parent = None
            elif node.parent.left == node:
                node.parent.left = node.left
            elif node.parent.right == node:

                node.parent.right = node.left
            return

        if node.left is None:
            node.right.parent = node.parent
            if node is self.root:
                self.root = node.right
            elif node.parent.left == node:
                node.parent.left = node.right
            elif node.parent.right == node:
                node.parent.right = node.right
            return

        #TODO: refactor.
        right_temporary_node = node.right
        dist_right = 1
        while right_temporary_node.left is not None:
            right_temporary_node = right_temporary_node.left
            dist_right += 1

        left_temporary_node = node.left
        dist_left = 1
        while left_temporary_node.right is not None:
            left_temporary_node = left_temporary_node.right
            dist_left += 1

        if( dist_right > dist_left ):
            temporary = right_temporary_node

        else:
            temporary = left_temporary_node

        temporary = temporary.parent # vamos guardar uma referencia para esse nó pois é a partir daqui que será necessário rebalance.

        if( node.right is temporary ):
            temporary.left = node.left
            node.left.parent = temporary

        if( node.left is temporary ):
            temporary.right = node.right
            node.right.parent = temporary

        else:
            if temporary.parent.id > temporary.id:
                temporary.parent.left = None
            else:
                temporary.parent.right = None
            temporary.right = node.right
            temporary.left = node.left
            node.left.parent = temporary
            node.right.parent = temporary

        temporary.parent = node.parent
        if node is self.root:
            self.root = temporary
        if node.parent.left == node:
            node.parent.left = temporary
        elif node.parent.right == node:
            node.parent.right = temporary

        node = temporary
        if node.right is None and node.left is None:
            node.height = 0
        elif node.right is None:
            node.height = node.left.height+1
        elif node.left is None:
            node.height = node.right.height+1

        while( node.parent is not None ):
            node = node.parent
            if( (node.right is not None and node.right.height < node.height-1) and ( node.left is not None and node.left.height < node.height-1) ):
                node.height -= 1
            else:
                break

        node = temporary
        while( node != None ):
            if abs(node.factor()) <= 1:
                node = node.parent
            else:
                node_z = node
                if( node_z.right.height > node_z.left.height ):
                    node_y = node_z.right
                else:
                    node_y = node_z.left
                if( node_y.right.height > node_y.left.height ):
                    node_x = node_y.right
                else:
                    node_x = node_y.left

                ##Left-left case
                if( node_z.left is node_y and node_y.left is node_x ):
                    _rotate_right(node_z)

                #Left-right case
                if( node_z.left is node_y and node_y.right is node_x ):
                    _rotate_left( node_y )
                    _rotate_right( node_z )

                #right-left case
                if( node_z.right is node_y and node_y.left is node_x ):
                    _rotate_right( node_y )
                    _rotate_left( node_z )

                #right-right case
                if( node_z.right is node_y and node_y.right is node_x ):
                    _rotate_left( node_z )

