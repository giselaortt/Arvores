import pytest
from BTrees import *


class Test():

    def test_insert_key( self ):
        node = NodeBTree(1)
        node.insert(2)
        assert 2 in node


    @staticmethod
    def is_ordered(nums):
        return all(nums[i-1] < nums[i] for i in range(1, len(nums)))


    #remember it should not be used on the root, since it is the only noode that does not follow to this rule
    @staticmethod
    def node_should_have_between_5_and_10_keys(node):
        assert (len(node.keys) >= 5 and len(node.keys) <= 10 )


    def test_has_exceded( self ):
        node = NodeBTree( -2 )
        for i in range(10):
            node.insert(i)
        assert node.hasExceded()


    def test_has_exceded_should_be_false( self ):
        node = NodeBTree( 2 )
        node.insert(-2)
        node.insert(3)
        assert (not node.hasExceded())


    def test_is_leaf_node( self ):
        node = NodeBTree( 2 )
        assert node.isLeaf() is True


    def test_add_key_greater( self ):
        node = NodeBTree( 3 )
        node.insert( 4 )
        assert node.keys[0] == 3 and node.keys[1] == 4


    def test_add_key_smaller( self ):
        node = NodeBTree( 3 )
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


    #causing infinit looping
    def should_add_multiple_keys_in_tree( self ):
        pass
        tree = BTree()
        keys = [0,1,2,3,4,5,6,7,8,9,10]
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


    def all_nodes_should_be_perfectly_balanced( self ):
        tree = BTree()
        for key in range( 100 ):
            tree.insert(key)
        nodes = tree.pre_order()
        for node in nodes:
            assert Test.is_node_perfectly_balanced(node)


    def repetitive_insertion_should_fail(self):
        tree = BTree()
        for key in range( 100 ):
            tree.insert(key)
        with pytest.raises(Exception) as info:
            tree.insert(25)
        assert str(info.value) == "Operation not allowed."









