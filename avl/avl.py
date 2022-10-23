# -*- coding: utf-8 -*-


class Node:

    def __init__(self, key:int, name:str) -> None:
        self.key = key
        self.name = name
        self.right = None
        self.left = None
        self.parent = None
        self.height = 1


    def is_leaf(self) -> bool:

        return ( self.right == None and self.left == None )


    def is_left_child(self) -> bool:

        return ( self.parent is not None and self.id < self.parent.id )


    def is_right_child(self) -> bool:

        return ( self.parent is not None and self.id > self.parent.id )


    def factor(self) -> int:
        if self.right is None and self.left is None:
            return 0
        if self.left is None:
            return -1 * self.right.height
        if self.right is None:
            return self.left.height
        return self.left.height - self.right.height


    def calculate_height(self) -> int:
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


#"""
#     y                               x
#    / \     Right Rotation          /  \
#   x   T3   - - - - - - - >        T1   y
#  / \       < - - - - - - -            / \
# T1  T2     Left Rotation            T2  T3
#"""
class AVL:
    def __init__(self):
        self.root = None
        self.height = -1


    def insert(self, key:int, name:str) -> None:
        new_node = Node(key, name)
        if self.root is None:
            self.root = new_node
            return
        node = self._find_node_to_insert( self.root, key )
        if( node.key > new_node.key ):
            node.left = new_node
        else:
            node.right = new_node
        new_node.parent = node
        self._update_heights(node)
        self._rebalance_after_insertion( new_node )


    def _find_node_to_insert( self, node:Node, new_key:int ) -> Node:
        if node.key == new_key:
            raise Exception("Repetitions are not allowed.")
        if node.key < new_key:
            if node.right is None:
                return node
            else:
                return self._find_node_to_insert(node.right, new_key)
        else:
            if node.left is None:
                return node
            else:
                return self._find_node_to_insert(node.left, new_key)


    def _rebalance_after_insertion( self, node:Node ) -> None:
        leaf = node
        while( node != None ):
            if( node.factor()  >= 2):
                if( node.left.factor() == 1 ):
                    self._rotate_right( node )
                else:
                    self._rotate_left( node.left )
                    self._rotate_right( node )
                break;
            elif( node.factor() <= -2 ):
                if( node.right.factor() == -1 ):
                    self._rotate_left( node )
                else:
                    self._rotate_right( node.right )
                    self._rotate_left( node )
                break;
            node = node.parent


    def _rotate_right( self, node:Node ) -> None:
        new_parent = node.left
        new_parent.parent = node.parent
        if(node is self.root):
            self.root = new_parent
        else:
            if( node.parent.key > node.key ):
                node.parent.left = new_parent
            else:
                node.parent.right = new_parent
        node.parent = new_parent
        node.left = new_parent.right
        if( new_parent.right is not None ):
            new_parent.right.parent = node
        new_parent.right = node
        self._update_heights( node )


    def _rotate_left( self, node:Node ) -> None:
        new_parent = node.right
        new_parent.parent = node.parent
        if(node is self.root):
            self.root = new_parent
        else:
            if( node.parent.key > node.key ):
                node.parent.left = new_parent
            else:
                node.parent.right = new_parent
        node.parent = new_parent
        node.right = new_parent.left
        if( new_parent.left is not None ):
            new_parent.left.parent = node
        new_parent.left = node
        self._update_heights( node  )


    def _rotate_left_right( self, first_node, second_node ):
        pass


    def _rotate_right_left( self, first_node, second_node ):
        pass


    def in_order( self ) -> list:
        answer = []
        AVL._in_order( self.root, answer )
        return answer


    @staticmethod
    def _in_order( node:Node, answer:list ) -> list:
        if( node == None ):
            return
        AVL._in_order( node.left, answer )
        answer.append( node.key )
        AVL._in_order( node.right, answer )


    def pos_order( self ) -> list:
        answer = []
        AVL._pos_order( self.root, answer )
        return answer


    @staticmethod
    def _pos_order( node:None, answer:list ) -> list:
        if( node == None ):
            return
        AVL._pos_order( node.left, answer )
        AVL._pos_order( node.right )
        answer.append( node.key, answer )


    def pre_order( self ) -> list:
        answer = []
        AVL._pos_order( self.root, answer )
        return answer


    @staticmethod
    def _pre_order( node:None, answer:list ) -> list :
        if( node == None ):
            return
        answer.append( node.key, answer )
        AVL._pre_order( node.left )
        AVL._pre_order( node.right, answer )


    def search(self, key:int) -> Node:

        return self._search(self.root, key)


    def _search(self, node:Node, key:int) -> Node:
        if( node is None or node.key == key):
            return node
        if key > node.key:
            return self._search(node.right, key)
        return self._search(node.left, key)


    @staticmethod
    def _update_heights( node:Node ) -> None:
        if( node is None ):
            return
        new_height = node.calculate_height()
        if( new_height == node.height ):
            return
        node.height = new_height
        AVL._update_heights(node.parent)


    def _remove_conection_child_parent( node:Node, child_node:Node ) -> None:
        if node is None or child_node is None :
            return
        if node.left == child_node :
            node.left = None
        elif node.right == child_node:
            node.right = None
        child_node.parent = None


    @staticmethod
    def _find_logical_successor( node:Node ) -> Node :
        if( node.is_leaf()):
            return node

        if( node.right is None):
            return node.left

        if node.left is None:
            return node.right

        successor = node.right
        while successor.left is not None:
            successor = successor.left

        return successor


    @staticmethod
    def _swap_node_informations( first:Node, second:Node ) -> None:
        first.name, second.name = second.name, first.name
        first.key, second.key = second.key, first.key


    @staticmethod
    def _prune( node:Node ) -> None:
        if( node.parent is None ):
            return
        if( node.is_left_child() ):
            node.parent.left = None
        else:
            node.parent.right = None


    def remove( self, key:int ) -> None:
        node = self.search( key )
        if node is None:
            raise Exception("key does not exist.")
            return

        if( node.is_leaf() and self.root == node ):
            self.root = None
            return

        successor = _find_logical_successor( node )
        AVL._swap_node_informations( node, successor )
        AVL._prune( successor )
        AVL._update_heights( successor.parent )
        self._rebalance_after_deletion( successor.parent )

        if( node == self.root ):
            self.root = successor


    def _rebalance_after_deletion( self, node:Node ) -> None :
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

