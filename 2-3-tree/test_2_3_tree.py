import pytest
from tree_2_3 import Node


class Test_node():


    def test_is_leaf_node( self ):
        node = Node( 2 )
        assert node.isLeaf() is True


    def test_is_leaf_should_return_false( self ):
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


    def test_third_key( self ):
        pass


