import pytest
from tree_2_3 import Node, Tree_2_3


class Test_node():
    def test_is_leaf_when_first_child_is_not_present( self ):
        node = Node(1)
        other = Node(2)
        temp = Node(3)
        node.insertChild( other )
        node.insertChild( temp )
        node.removeChild( 2 )
        assert node.isLeaf() is False


    def test_is_leaf_node( self ):
        node = Node( 2 )
        assert node.isLeaf() is True


    def test_is_leaf_when_not_leaf( self ):
        node = Node(1)
        other = Node(2)
        node.insertChild( other )
        assert node.isLeaf() is False


    def test_create_node_with_key( self ):
        node = Node( 4 )
        assert node.keys == [4]


    def test_is_smaller_than( self ):
        node = Node( 2 )
        other_node = Node( 3 )
        assert node < other_node


    def test_is_equal( self ):
        node = Node(2)
        other = Node(2)
        assert node == other


    def test_is_greater_than( self ):
        node = Node(2)
        other = Node(4)
        assert other > node


    def test_greater_equal( self ):
        node = Node( 3 )
        other_node = Node( 3 )
        assert node >= other_node


    def test_greater_equal_with_diferent_values( self ):
        node = Node( 3 )
        other_node = Node( 2 )
        assert node >= other_node


    def test_add_key_greater( self ):
        node = Node( 3 )
        node.insertKey( 4 )
        assert node.keys[0] == 3 and node.keys[1] == 4


    def test_add_key_smaller( self ):
        node = Node( 3 )
        node.insertKey( 2 )
        assert node.keys[0] == 2 and node.keys[1] == 3


    def test_contain_on_empty_tree_returns_false( self ):
        tree = Tree_2_3()
        assert (0 in tree) is False


    def test_should_add_one_element_on_tree( self ):
        tree = Tree_2_3()
        tree.insert( 0 )
        assert tree.isEmpty() is False


    def test_should_add_multiple_keys_in_tree( self ):
        tree = Tree_2_3()
        tree.insert( 0 )
        tree.insert( 2 )
        """tree.insert( 3 )
        tree.insert( 4 )
        tree.insert( 5 )
        tree.insert( 6 )
        tree.insert( 7 )
        tree.insert( 8 )"""




