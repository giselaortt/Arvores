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
        node =  skip.search(1)
        assert node.key == 1


    def test_multiple_insertions(self):
        skip = SkipList()
        skip.insert(1)
        skip.insert(4)
        skip.insert(3)
        skip.insert(2)
        assert str(skip) == "-inf 1 2 3 4 inf "
        assert skip.search(1)
        assert skip.search(3)
        assert skip.search(4)
        assert skip.search(2)


    def test_contains_when_true(self):
        skip = SkipList()
        skip.insert(1)
        skip.insert(4)
        skip.insert(3)
        skip.insert(2)
        assert 1 in skip
        assert 2 in skip


    def test_contains_when_false(self):
        skip = SkipList()
        skip.insert(1)
        skip.insert(4)
        skip.insert(3)
        skip.insert(2)
        assert 5 not in skip
        assert 10 not in skip


    def test_should_not_insert_repeated_elements(self):
        skip = SkipList()
        skip.insert(1)
        with pytest.raises(Exception) as info:
            skip.insert(1)
        assert str(info.value) == "Operation not permitted"

    """
    def test_node_deletion(self):
        skip = SkipList()
        skip.insert(1)
        skip.insert(4)
        skip.insert(3)
        skip.insert(2)
        node = skip.search(3)
        del node
        assert 3 not in skip
    """


    def test_are_all_elements_sorted(self):
        pass


    def test_iter( self ):
        pass


    def test_next( self ):
        pass




