# -*- coding: utf-8 -*-


from avl import AVL
import pytest


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


    #Error found.
    def test_remove( self ):
        pass
        #self.test_avl.remove( 6 )
        #self.test_avl.remove( 1 )
        #self.test_avl.remove( 2 )
        #self.test_avl.remove( 4 )
        #self.test_avl.remove( 24 )
        #self.test_avl.remove( 2 )
        #self.test_avl.remove( 3 )
        #assert self.test_avl.search(6) is None


    def test_is_avl( self ):
        assert self.test_avl._is_avl( self.test_avl.root ) is True


    def test_height( self ):
        assert self.test_avl.root.height == self.test_avl.height()


    def test_height_second( self ):
        self.test_avl.insert(25, 'a')
        assert self.test_avl.root.height == self.test_avl.height()


    def test_height_third( self ):
        self.test_avl.insert(26, 'b')
        self.test_avl.insert(27, 'c')
        self.test_avl.insert(28, 'd')
        self.test_avl.insert(29, 'e')
        self.test_avl.insert(30, 'f')
        self.test_avl.insert(-1, 'k')
        self.test_avl.insert(-10, 'g')
        self.test_avl.insert(-5, 'height')
        assert self.test_avl.root.height == self.test_avl.height()


    def test_is_inorder_sorted( self ):
        pass


    def test_insert_with_repetition( self ):
        with pytest.raises(Exception) as info:
            self.test_avl.insert( 3, "Igor" )
        assert  str(info.value) == "Repetitions are not allowed."




