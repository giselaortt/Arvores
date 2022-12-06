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



