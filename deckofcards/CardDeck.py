from itertools import product
from random import shuffle

class Card:
    """
    Represents a playing card with a rank and a suit.
    Cards can be compared using ==, <, and > etc. (see options for extended behaviour)
    The ** operator returns True if 2 cards have same suite.

    Attributes:
        rank (str): The rank of the card ('Ace', '2', ..., 'King').
        suit (str): The suit of the card ('Hearts', 'Diamonds', 'Clubs', 'Spades').
    Options:
        "compare_within_suite_only" : True = any comparison >, <, == etc is applied inside
        the same suite as the calling card. A mismatch in suites returns None.
        Defaults to False.
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
        self.compare_within_suite_only = False # Starts with comparing any 2 suites.
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
            variant (str): Which variation to return. 
                           's' for short, 'l' for long, 'v' for very long.

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
    def __repr__(self):
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

    # Comparison overloaded operators
    # Short circuit evaluation depends on within-suite comparison of ranks. 
    def __lt__(self, c:'Card') -> bool:
        if self.compare_within_suite_only and (not self ** c) : return None 
        return c.rank > self.rank
    def __le__(self, c:'Card') -> bool:
        if self.compare_within_suite_only and (not self ** c) : return None 
        return c.rank >= self.rank    
    def __eq__(self, c:'Card') -> bool:
        if self.compare_within_suite_only and (not self ** c) : return None 
        return c.rank == self.rank
    def __gt__(self, c:'Card') -> bool:
        if self.compare_within_suite_only and (not self ** c) : return None 
        return c.rank < self.rank    
    def __ge__(self, c:'Card') -> bool:
        if self.compare_within_suite_only and (not self ** c) : return None 
        return c.rank <= self.rank        
    def __pow__(self, c:'Card') -> bool:
        return self.suite_short == c.suite_short
    
    # Sub is a comparison that returns 0 if the cards are the same.
    def __sub__(self, c:'Card') -> int:
        if self.suite_short == c.suite_short and self.rank == c.rank :
            return 0
        else:
            return 1



class Deck:
    """
    Represents a deck or hand of Cards.
    You can take, put a card, shuffle the deck etc.

    The deck can fill itself with cards, like 52 cards.
    Under the hood this is a standard python list.

    Attributes:
        No attributes for creating a deck.
    
    

    """

    def __init__(self):
        self.decklist = list()

    def add_traditional_52cards(self) -> None:
        suites = ['c','d','h','s']
        ranks = range(1, 14)

        list_to_append = [Card(rank, suit) for suit, rank in product(suites, ranks)]
        self.decklist.extend(list_to_append) # Extend rather than append bec each item must be inserted individually.

    def shuffle(self) -> None:
        shuffle(self.decklist)
        return None

    def take_card(self, skip_cards:int = 0 ) -> Card:
        try:
            ret = self.decklist.pop(skip_cards)
        except Exception as e:
            return None # If we pop something out of bonds => None        
        return ret

    def put_card(self, c:Card, position:int = 0) -> None:
        return self.decklist.insert(position, c)

    def card_count(self) -> int:
        return len(self.decklist)

    def find_card(self, c:Card) -> int:
        """
        Find the position of a card in deck, as if you saw all the faces.
        The first match is returned, if there are more matches.
        None returned if no match found.

        Parameters:
        c (Card) : what card to search for.

        Returns:
        None: Nothing is returned.
        """
        # We loop to find the first match, as fast as possible
        for index, d in enumerate(self.decklist):
            if (d - c) == 0 : return index
        # Return None if we didn't match any
        return None 
