# -*- coding: utf-8 -*-
from avl import AVL
import pytest
from collections import deque


class Test():
    test_avl = AVL()
    test_avl.insert(3, 'Igor')
    test_avl.insert(6, 'Jurema')
    test_avl.insert(1, 'Lidia')
    test_avl.insert(4, 'Carlos')
    test_avl.insert(24, 'gi')
    test_avl.insert(2, 'aurora')

    def test_search_first( self ):
        test_search1 = self.test_avl.search(3)
        assert test_search1.name == 'Igor'


    def test_search_second( self ):
        test_search2 = self.test_avl.search(4)
        assert test_search2.name == 'Carlos'


    def test_search_inexistend_key( self ):
        test_search3 = self.test_avl.search(9)
        assert test_search3 is None


    def test_insert_with_repetition( self ):
        with pytest.raises(Exception) as info:
            self.test_avl.insert( 3, "Igor" )
        assert  str(info.value) == "Repetitions are not allowed."


    def proof_height( self, avl_node ):
        if avl_node is None:
            return 0
        height = max( self.proof_height(avl_node.right), self.proof_height(avl_node.left) ) + 1

        return height


    def test_are_all_heights_correct( self ):
        stack = deque()
        node = self.test_avl.root

        while( node is not None ):
            stack.append( node.right )
            stack.append( node.left )
            assert node.height == self.proof_height( node )
            node = stack.popleft()


    def test_proof_height_third( self ):
        self.test_avl.insert(26, 'b')
        self.test_avl.insert(27, 'c')
        self.test_avl.insert(28, 'd')
        self.test_avl.insert(29, 'e')
        self.test_avl.insert(30, 'f')
        self.test_avl.insert(-1, 'k')
        self.test_avl.insert(-10, 'g')
        self.test_avl.insert(-5, '_proof_height')
        self.test_are_all_heights_correct()


    def _is_avl( self, node ):
        if( node == None ):
            return True
        if( node.left is None and node.right is None ):
            return True
        if( node.left is None ):
            return node.right.height <= 2
        if( node.right is None ):
            return node.left.height <= 2
        if( abs( node.left.height - node.right.height ) >= 2 ):
            return False
        return (self._is_avl( node.right ) and self._is_avl( node.left ))


    def test_is_avl( self ):
        assert self._is_avl( self.test_avl.root ) is True


    def test_is_inorder_sorted( self ):
        inorder = self.test_avl.in_order()
        print( inorder )
        for i in range( len( inorder )-1 ):
            assert inorder[i] < inorder[i+1]


    def test_remove_existing_element( self ):
        self.test_avl.remove( 6 )
        assert self.test_avl.search(6) is None


    def test_remove_unexisting_element( self ):
        with pytest.raises(Exception) as info:
            self.test_avl.remove( 32 )


    def test_pre_order( self ):
        pass


    def test_pos_order( self ):
        pass


    def test_in_order( self ):
        pass

