

class Node:
    right:'Node' = None
    left:'Node' = None
    above:'Node' = None
    bellow:'Node' = None
    key:int
    level:int = 0

    def __init__( self, key:int ):
        self.key = key


    def __lt__( self, key:int ):

        return self.key < key


    def __gt__( self, key:int ):

        return self.key > key


    def __eq__( self, key:int ):

        return self.key==key



class SkipList:
    upper_left:'Node' = None
    upper_right:'Node' = None
    number_of_levels:int = 0
    length:int = 0

    def __init__( self ):
        pass


    def __len__( self ):

        return self.length


    def __iter__( self ):
        pass


    def __contains__( self, key ):
        pass


    def __getitem__( self ):
        pass


    def __add__( self, other:'SkipList' ):
        pass


    def __iadd__( self, other:'SkipList' ):
        pass


    @classmethod
    def _flip_coin() -> bool:
        pass


    def search( self, key ):
        pass


    def _search( self, key ):
        pass


    def insert( self, key ):
        pass


    def remove( self, key ):
        pass


