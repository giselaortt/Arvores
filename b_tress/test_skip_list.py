import pytest
from skip_list import Node, SkipList


class Test:

    def test_node_comparison(self):
        node = Node(50)
        assert (node == 50)
        assert (node < 51)
        assert (node > 40)
        assert (node > 50) is False
        assert (node < 40) is False


    def test_are_all_pointers_none(self):
        node = Node(50)
        assert (node.above is None and node.bellow is None and node.right is None and node.left is None)


    def test_coin_flip(self):
        value = SkipList._flip_coin()
        assert (value==1 or value==0)is True


    def test_search_on_empty_list_should_return_none(self):
        skip = SkipList()
        assert skip.search(50) is None


    def test_insert_one_element_and_finds_it(self):
        skip = SkipList()
        assert skip.upper_left is not None
        skip.insert(1)
        node =  skip._search(1)
        assert node.key == 1


    def test_are_all_elements_sorted(self):
        pass


    def test_iter( self ):
        pass


    def test_next( self ):
        pass




