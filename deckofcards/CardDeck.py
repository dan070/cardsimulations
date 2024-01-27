from itertools import product
from random import shuffle

class Card:
    """
    Represents a playing card with a rank and a suit.

    Attributes:
        rank (str): The rank of the card ('Ace', '2', ..., 'King').
        suit (str): The suit of the card ('Hearts', 'Diamonds', 'Clubs', 'Spades').
    """

    def __init__(self, rank: int, suite: str) -> None:
        """
        The constructor for the Card class.

        Parameters:
            rank (int): The rank of the card. Ace is 1, and 14. 
            suit (str): The suit of the card. "Clubs", or "clubs" or "c" or "C" is equivalent.
        """


        # Todo : add tests of rank and suite
        # should not be negative. suite has to be string. and start with cdhs, and be >=1 char.
        self.rank = rank
        self.rank_short = ''
        self.rank_long = ''
        self.face_up = False # Card starts as face down.
        match rank:
            case 1: 
                self.rank_long = 'Ace'
                self.rank_short = 'A'
            case 2: 
                self.rank_long = 'Two'
                self.rank_short = '2'
            case 3: 
                self.rank_long = 'Three'
                self.rank_short = '3'
            case 4: 
                self.rank_long = 'Four'
                self.rank_short = '4'
            case 5: 
                self.rank_long = 'Five'
                self.rank_short = '5'
            case 6: 
                self.rank_long = 'Six'
                self.rank_short = '6'
            case 7: 
                self.rank_long = 'Seven'
                self.rank_short = '7'
            case 8: 
                self.rank_long = 'Eight'
                self.rank_short = '8'
            case 9: 
                self.rank_long = 'Nine'
                self.rank_short = '9'
            case 10: 
                self.rank_long = 'Ten'
                self.rank_short = 't'
            case 11: 
                self.rank_long = 'Jack'
                self.rank_short = 'J'
            case 12: 
                self.rank_long = 'Queen'
                self.rank_short = 'Q'
            case 13: 
                self.rank_long = 'King'
                self.rank_short = 'K'
            case 14: 
                self.rank_long = 'Ace'
                self.rank_short = 'A'
            case _:
                self.rank_long = 'unknown'
                self.rank_short = '?'


        # Set Suite
        firstletter = suite.lower()[0]
        match firstletter:
            case 's':
                self.suite_short = '\u2660'
                self.suite_long = 'Spades'
            case 'h':
                self.suite_short = '\u2665'
                self.suite_long = 'Hearts'
            case 'd':
                self.suite_short = '\u2666'
                self.suite_long = 'Diamonds'
            case 'c':
                self.suite_short = '\u2663'
                self.suite_long = 'Clubs'
            case _:
                raise Exception('Suite of new created Card invalid. Error.')
            
    def to_string(self, variant: str = 'long') -> str:
        """
        Return string representation of card for printing.

        Parameters:
            variant (str): Which variation to return. s for short, l for long, v for very long.

        Returns:
        str: Either 2 characters with ascii-character for suite, and 1 character for rank.
        Or a longer string, eg 'Two of Clubs'.
        Or a very long string, eg 'Ace of Spades (face down)'

        """
        if variant.lower()[0] == 's':
            return f"{self.suite_short}{self.rank_short}"
        if variant.lower()[0] == 'l':
            return f"{self.rank_long} of {self.suite_long}"        
        if variant.lower()[0] == 'v':
            return f"{self.rank_long} of {self.suite_long} ({'face up' if self.face_up else 'face down'})"                
        return None
    
    def __str__(self):
        return f"{self.to_string()}"
    def is_face_up(self) -> bool:
        """
        If card is face up or not.

        Returns:
        bool: The card is face up = true, if face down = false.
        """
        return self.face_up
    def set_face_up(self, value:bool = True) -> None:
        """
        Set face up or down on card, i.e flip it.

        Parameters:
        value (bool) : What to set the face up attribute to.

        Returns:
        None: Nothing is returned.
        """

        self.face_up = value
    # Comparison
    def is_higher_than(self, c:'Card') -> bool:
        return c.rank < self.rank
    def is_lower_than(self, c:'Card') -> bool:
        return c.rank > self.rank
    def is_equal_to(self, c:'Card') -> bool:
        return c.rank == self.rank
    def is_same_suit(self, c:'Card') -> bool:
        return self.suite_short == c.suite_short
    # Comparison overloaded operators
    def __gt__(self, c:'Card') -> bool:
        return self.is_higher_than(c)
    def __lt__(self, c:'Card') -> bool:
        return self.is_lower_than(c)
    def __eq__(self, c:'Card') -> bool:
        return self.is_equal_to(c)
    def __pow__(self, c:'Card') -> bool:
        return self.is_same_suit(c)

class Deck:
    def __init__(self):
        self.decklist = list()

    def add_traditional_52cards(self) -> None:
        suites = ['c','d','h','s']
        ranks = range(1, 14)

        list_to_append = [Card(rank, suit) for suit, rank in product(suites, ranks)]
        self.decklist.extend(list_to_append)

    def shuffle(self) -> None:
        shuffle(self.decklist)
        return None

    def take_card(self, skip_cards:int = 0 ) -> Card:
        return self.decklist.pop(skip_cards)

    def put_card(self, c:Card, position:int = 0) -> None:
        return self.decklist.insert(position, c)

    def card_count(self) -> int:
        return len(self.decklist)
