import pytest
from map_skip_list import NodeMapSkipList, MapSkipList
import random


class Test:

    def test(self):
        assert True


    def test_insertion_should_increase_counter(self):
        skip = MapSkipList()
        skip.insert(-15, 1)
        assert skip.length == 1


    def test_are_all_pointers_none(self):
        node = NodeMapSkipList(50,100)
        assert (node.above is None and node.bellow is None and node.right is None and node.left is None)


    def test_coin_flip(self):
        value = MapSkipList._flip_coin()
        assert (value==1 or value==0)is True


    def test_search_on_empty(self):
        skip = MapSkipList()
        assert skip._search(50) is not None
        assert skip._search(50).key == float('-inf')


    def test_search_on_length_one_list(self):
        skip = MapSkipList()
        skip.insert(1, 'a')
        assert 1 in skip


    def test_user_search_on_empty_list_should_return_none(self):
        skip = MapSkipList()
        assert skip.search(50) is None


    def test_insert_one_element_and_finds_it(self):
        skip = MapSkipList()
        assert skip.upper_left is not None
        skip.insert(1,'a')
        node = skip.search(1)
        assert node is not None
        assert node.key == 1


    def test_insertion(self):
        skip = MapSkipList()
        skip.insert(1,-5)
        node = skip.down_left.right
        node = skip.search(1)
        assert node is not None
        assert node.right is not None
        assert node.left is not None
        assert node.right.key == float('inf')
        assert node.left.key == float('-inf')
        assert node.key == 1


    def test_multiple_insertions(self):
        skip = MapSkipList()
        skip.insert(1,'a')
        skip.insert(4,'b')
        skip.insert(3,'c')
        skip.insert(2,'e')
        assert skip.search(1)
        assert skip.search(3)
        assert skip.search(4)
        assert skip.search(2)



    def test_contains_when_true(self):
        skip = MapSkipList()
        skip.insert(1,'a')
        skip.insert(4,'a')
        skip.insert(3,'a')
        skip.insert(2,'a')
        assert 1 in skip
        assert 2 in skip


    def test_contains_when_false(self):
        skip = MapSkipList()
        skip.insert(1,'a')
        skip.insert(4,'a')
        skip.insert(3,'a')
        skip.insert(2,'a')
        assert 5 not in skip
        assert 10 not in skip


    def test_contains_on_empty_list(self):
        skip = MapSkipList()
        assert float('inf') in skip
        assert float('-inf') in skip


    def test_should_not_insert_repeated_elements(self):
        skip = MapSkipList()
        skip.insert(1,'a')
        with pytest.raises(Exception) as info:
            skip.insert(1,'a')
        assert "Operation not permitted" in str(info.value)


    def test_random_level_generation(self):
        level = MapSkipList._random_level()


    def test_adjust_tree_level_should_update_counter(self):
        skip = MapSkipList()
        skip._adjust_tree_level(5)
        assert skip.number_of_levels == 5


    def test_size_of_side_lists(self):
        skip = MapSkipList()
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


    def test_adjust_tree_level_should_link_sides(self):
        skip = MapSkipList()
        skip._adjust_tree_level(10)
        node_left = skip.upper_left
        node_right = skip.upper_right
        level = 0
        while(node_left is not None and node_right is not None and level <= 1000):
            level += 1
            assert node_left.right is node_right
            assert node_right.left is not None
            assert node_right.left is node_left
            assert (node_left.above is None) or node_left.above.bellow is node_left
            assert (node_right.above is None) or node_right.above.bellow is node_right
            node_left = node_left.bellow
            node_right = node_right.bellow
        assert node_left is None and node_right is None
        assert level == 10


    def test_node_chaining_links(self):
        node = MapSkipList.create_node_chaining(0,'a',5)
        counter = 0
        while(node is not None and counter <= 1000):
            counter += 1
            assert node.right is None and node.left is None
            assert node.above is None or node.above.bellow is node
            node = node.above
        assert counter == 4


    def test_chain_has_desired_height(self):
        node = MapSkipList.create_node_chaining(0,'a',5)
        counter = 0
        while(node is not None and counter <= 1000):
            counter += 1
            node = node.above
        assert counter == 4


    def test_empty_list(self):
        skip = MapSkipList()
        node = skip._search(0)
        assert node.key == float('-inf')
        assert node.right is not None
        assert node.right.key == float('inf')


    def test_insertion_links(self):
        skip = MapSkipList()
        level = 10
        first_chain = skip.create_node_chaining(0,'a',10)
        skip._adjust_tree_level(10)
        skip.link_node_chain(first_chain, skip.down_left)
        node = first_chain
        while(node is not None):
            node.left is not None
            node.right is not None
            node.left.key == float('-inf')
            node.right.key == float('inf')
            node = node.above
        second_chain = skip.create_node_chaining(1,'a',10)
        skip.link_node_chain( second_chain, first_chain )
        while( second_chain is not None):
            assert second_chain.left is first_chain
            second_chain = second_chain.above
            first_chain = first_chain.above


    def test_single_deletion(self):
        skip = MapSkipList()
        skip.insert(10,'a')
        skip.delete(10)
        assert 10 not in skip


    def test_multiple_deletions(self):
        skip = MapSkipList()
        skip.insert(1,'a')
        skip.insert(4,'a')
        skip.insert(3,'a')
        skip.insert(2,'a')
        skip.insert(-2,'a')
        skip.insert(-20,'a')
        skip.insert(15,'a')
        skip.insert(-4,'a')
        skip.insert(10,'a')
        skip.delete(3)
        assert 3 not in skip
        skip.delete(2)
        assert 2 not in skip
        skip.delete(1)
        assert 1 not in skip
        skip.delete(4)
        assert 4 not in skip


    #How to test speed complexity?
    def test_functional(self):
        skip = MapSkipList()
        numbers = random.sample( range(-1000, 1000), 100 )
        to_delete = random.sample(numbers, 20)

        for number in numbers:
            skip.insert(number,'a')

        for number in to_delete:
            skip.delete(number)
            assert number not in skip

        for number in numbers:
            node = skip.search(number)
            if(number in to_delete):
                assert node is None
            else:
                assert node is not None
                assert node.key == number


    def test_search(self):
        skip = MapSkipList()
        numbers = random.sample( range(-1000, 1000), 100 )
        to_delete = random.sample(numbers, 20)

        for number in numbers:
            skip.insert(number,'a')

        for number in numbers:
            node = skip.search(number)
            assert node is not None
            assert node.key == number
            assert node.bellow is None


    def test_node_to_str(self):
        node = NodeMapSkipList(4)
        node.right = NodeMapSkipList(2)
        node.left = NodeMapSkipList(3)
        print(str(node))
        #assert str(node) == "  None\n3  <4>  2\n  None\n"
        assert str(node) == "None (3, None) <(4, None)> (2, None) None"


    def test_merge_empty_lists_should_be_empty_list(self):
        a = MapSkipList()
        b = MapSkipList()
        c = a + b
        assert len(c) == 0
        assert isinstance(c, MapSkipList)


    def test_iadd_empty_list(self):
        a = MapSkipList()
        b = MapSkipList()
        b += a
        assert len(b) == 0
        assert isinstance(b, MapSkipList)
        assert str(b) == "(-inf, None) (inf, None) "


    def test_equal(self):
        a = MapSkipList()
        b = MapSkipList()
        a.insert(1, 'a')
        a.insert(4, 'a')
        a.insert(3, 'a')
        b.insert(1, 'a')
        b.insert(4, 'a')
        b.insert(3, 'a')
        b.insert(-1, 'b')
        a.insert(-1, 'b')
        assert a == b


#    def test_get_above_level(self):
#        pass
#
#
#    def test_are_all_elements_sorted(self):
#        pass
#
#
#    def test_is_fully_coneected(self):
#        pass
#
#
    def test_getitem_with_int(self):
        skip = MapSkipList()
        skip.insert(-20,'a' )
        skip.insert(-4, 'a' )
        skip.insert(-2, 'a' )
        skip.insert(1 , 'a' )
        skip.insert(2 , 'a' )
        skip.insert(3 , 'a' )
        skip.insert(4 , 'a' )
        skip.insert(15, 'a' )
        assert len(skip) == 8
        assert skip[3] == 1
        assert skip[4] == 2
        assert skip[0] == -20
        assert skip[-1] == 15
        assert skip[1] == -4
        assert skip[2] == -2


    def test_getitem_tuple(self):
        skip = MapSkipList()
        skip.insert(-20, 'a' )
        skip.insert(-4 , 'a' )
        skip.insert(-2 , 'a' )
        skip.insert(1  , 'a' )
        skip.insert(2  , 'a' )
        skip.insert(3  , 'a' )
        skip.insert(4  , 'a' )
        skip.insert(15 , 'a' )
        b = MapSkipList()
        b.insert(-2, 'a')
        b.insert(1, 'a')
        b.insert(2, 'a')
        b.insert(3, 'a')
        assert skip[2,3,4,5] == b


    def test_getitem_slice(self):
        skip = MapSkipList()
        skip.insert(-20,'a' )
        skip.insert(-4, 'a' )
        skip.insert(-2, 'a' )
        skip.insert(1,  'a' )
        skip.insert(2,  'a' )
        skip.insert(3,  'a' )
        skip.insert(4,  'a' )
        skip.insert(15, 'a' )
        b = MapSkipList()
        b.insert(1, 'a')
        b.insert(-2, 'a')
        assert skip[2:4] == b
        #assert skip[0:4:2] == b


    def test_add_lists(self):
        skip = MapSkipList()
        other = MapSkipList()
        skip.insert(-2 , 'a')
        skip.insert(3  , 'a')
        other.insert(2 , 'a')
        other.insert(-3, 'a')
        result = skip + other
        assert str(result) == '(-inf, None) (-3, a) (-2, a) (2, a) (3, a) (inf, None) '


    def test_add_inplace_with_deep_copy(self):
        skip = MapSkipList()
        other = MapSkipList()
        skip.insert(-2 , 'a')
        skip.insert(3  , 'a')
        other.insert(2 , 'a')
        other.insert(-3, 'a')
        skip += other
        #testing the deep copy
        other.insert(5, 'a')
        assert str(skip) == '(-inf, None) (-3, a) (-2, a) (2, a) (3, a) (inf, None) '

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
