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


    def test_insertion_should_increase_counter(self):
        skip = SkipList()
        skip.insert(-15)
        assert skip.length == 1


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
        node = skip._search(1)
        assert node.key == 1


    def test_multiple_insertions(self):
        skip = SkipList()
        skip.insert(1)
        skip.insert(4)
        skip.insert(3)
        skip.insert(2)
        assert str(skip) == "-inf 1 2 3 4 inf "
        assert skip._search(1)
        assert skip._search(3)
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


    def test_node_deletion(self):
        skip = SkipList()
        skip.insert(1)
        skip.insert(4)
        skip.insert(3)
        skip.insert(2)
        skip.delete_node(3)
        assert 3 not in skip


    def test_random_level_generation(self):
        level = SkipList._random_level()


    def test_adjust_tree_level_should_update_counter(self):
        skip = SkipList()
        skip._adjust_tree_level(5)
        assert skip.number_of_levels == 5


    def test_adjust_tree_level_should_increase_side_lists(self):
        skip = SkipList()
        skip._adjust_tree_level(5)
        node = skip.upper_left
        level_right = 0
        while(node is not None and level_right <= 1000):
            level_right += 1
            node = node.bellow
        assert level_right == 5
        node = skip.upper_right
        level_left = 0
        while(node is not None and level_left <= 1000):
            level_left += 1
            node = node.bellow
        assert level_left == 5


    def test_node_chaining(self):
        node = SkipList.node_chaining(0,5)
        counter = 0
        while(node is not None):
            counter += 1
            node = node.above
        assert counter == 5


    def test_are_all_elements_sorted(self):
        pass


    def test_iter( self ):
        pass


    def test_next( self ):
        pass




