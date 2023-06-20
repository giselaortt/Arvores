import pytest
from BTrees import *
from random import shuffle


class Test():

    def test_insert_key( self ):
        node = NodeBTree()
        node.insert(2)
        node.insert(1)
        assert 2 in node


    def test_has_exceded( self ):
        node = NodeBTree( )
        for i in range(21):
            node.keys.append(i)
        assert node.hasExceded()


    def test_has_exceded_should_be_false( self ):
        node = NodeBTree( )
        node.insert(-2)
        node.insert(3)
        assert (not node.hasExceded())


    def test_split( self ):
        node = NodeBTree()
        node.insert(1)
        node.insert(2)
        node.insert(3)
        node._split()
        assert len(node) == 1
        assert node.keys == [2]


    def test_node_must_split_automatically( self ):
        node = NodeBTree()
        for i in range(21):
            node.insert(i)
        assert len(node) == 1
        assert len(node.children[1]) == 10
        assert len(node.children[0]) == 10


    def test_children_type( self ):
        node = NodeBTree()
        for i in range(100):
            node.insert(i)
        assert type( node.children[1] ) == NodeBTree
        assert type( node.children[0] ) == NodeBTree


    def test_is_leaf_node( self ):
        node = NodeBTree( )
        node.insert(2)
        assert node.isLeaf() is True


    def test_add_key_greater( self ):
        node = NodeBTree( )
        node.insert( 3 )
        node.insert( 4 )
        assert node.keys[0] == 3 and node.keys[1] == 4


    def test_add_key_smaller( self ):
        node = NodeBTree(  )
        node.insert( 3 )
        node.insert( 2 )
        assert node.keys[0] == 2 and node.keys[1] == 3


    def test_contain_on_empty_tree_returns_false( self ):
        tree = BTree()
        assert (0 in tree) is False


    def test_is_empty_when_false( self ):
        tree = BTree()
        tree.insert( 0 )
        assert tree.isEmpty() is False


    def test_is_empty( self ):
        tree = BTree()
        assert tree.isEmpty()


    def test_single_insertion( self ):
        tree = BTree()
        tree.insert(1)
        assert 1 in tree


    def test_should_add_multiple_keys_in_tree( self ):
        tree = BTree()
        keys = list(range(1000))
        shuffle(keys)
        for key in keys:
            tree.insert( key )
        assert all([ key in tree for key in keys ])


    @staticmethod
    def calculate_height( node:object ) ->  int:
        if node is None:
            return 0
        if( node.isLeaf() ):
            return 1
        return max([ Test.calculate_height(child) for child in node.children ])+1


    @staticmethod
    def is_node_perfectly_balanced( node:object ) -> bool:
        if node is None or node.isLeaf():
            return True
        return ( len(set([ Test.calculate_height(child) for child in node.children  ])) == 1)


    def test_all_nodes_should_be_perfectly_balanced( self ):
        tree = BTree()
        for key in range( 10000 ):
            tree.insert(key)
        nodes = tree.pre_order()
        for node in nodes:
            assert Test.is_node_perfectly_balanced(node)


    def test_is_b_tree( self ):
        pass


    def test_repetitive_insertion_should_fail(self):
        tree = BTree()
        for key in range( 100 ):
            tree.insert(key)
        with pytest.raises(Exception) as info:
            tree.insert(25)
        assert str(info.value) == "Operation not allowed."


    def test_to_string(self):
        tree = BTree()
        keys = range(21)
        for key in keys:
            tree.insert( key )


