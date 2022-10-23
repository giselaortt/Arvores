# -*- coding: utf-8 -*-

from trees import Tree
import pytest

class Test():
    tree = Tree()
    tree.insert(3, 'Igor')
    tree.insert(6, 'Jurema')
    tree.insert(1, 'Lidia')
    tree.insert(4, 'Carlos')
    tree.insert(24, 'gi')
    tree.insert(2, 'aurora')

    def test_search_existing_key( self ):
        name = self.tree.search(3)
        assert name == 'Igor'
        name = self.tree.search(4)
        assert name == 'Carlos'


    def test_search_unexisting_key( self ):
        name = self.tree.search(9)
        assert name is False


    def test_deleting_existing_keys( self ):
        self.tree.remove( 6 )
        print( self.tree.search(6) )
        print( self.tree.search(4) )
        assert self.tree.search(6) is False
        self.tree.remove( 4 )
        #assert self.tree.search(4) is False


    def test_delete( self ):
        with pytest.raises(Exception) as info:
            self.tree.remove( 10 )
        assert  str(info.value) == "unexisting key"


    def test_delete_all_keys( self ):
        tree = Tree()
        tree.insert(3, 'Igor')
        tree.insert(6, 'Jurema')
        tree.insert(1, 'Lidia')
        tree.insert(4, 'Carlos')
        tree.insert(24, 'gi')
        tree.insert(2, 'aurora')
        keys = [3,6,1,4,24,2]
        for key in keys:
            tree.remove(key)
            assert tree.search( key ) is False


    def test_deleting_existing_key_multiple_times( self ):
        self.tree.remove( 2 )
        with pytest.raises(Exception) as info:
            self.tree.remove( 2 )
        assert  str(info.value) == "unexisting key"


    def test_successor_should_be_a_leaf( self ):
        pass


    def test_swaping( self ):
        pass




