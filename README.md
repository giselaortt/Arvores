# Data Structures with python

## Contains:

    1. binary search tree

    2. AVL

    3. 2-3-trees 
    
    4. B-Trees
    
    5. Skip Lists (used on BTrees)

    6. Map Skip Lists (used on B Trees)

## to be implemented:


## Things to note:

    - Even thought python is not typed and would allow for an inserction with a float type, the trees would not work as expected with a float because i have not implemented the precision on float comparisson. The AVL and BST could potentially be used with chars but not in the case of the 2-3 trees. Adaptation would be simple thought.

    - Note that the implementation on the keys handling on the 2-3 trees is not efficient as many insertions appends and dels are made on the python arrays and lists. It is not worthy optimizing as a 2-3 tree only has few keys. in order to convert this code for a b-tree a skip list data structure is required which is not available on python, and is the reason why i didnt code b-trees yet (even though an extention on existing 2-3 trees would be simple). For this reason B-trees might come in another language soon.

## References and usefull links:

 - (bst)[https://www.ime.usp.br/~pf/estruturas-de-dados/aulas/st-bst]

 - (2 3 trees)[https://www.ime.usp.br/~pf/estruturas-de-dados/aulas/st-twothree]

 - (b trees)[https://www.ime.usp.br/~pf/estruturas-de-dados/aulas/B-trees]

 ### Skip List:
 - (complexity analyses)[https://m.youtube.com/watch?v=2g9OSRKJuzM&t=1s]

 - (Original paper)[https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf]


feel free to reach out and discuss!

