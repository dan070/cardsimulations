
class Card:
    def __init__(self, value: int, suite: str) -> None:
        # Todo : add tests of value and suite
        # should not be negative. suite has to be string. and start with cdhs, and be >=1 char.
        self.value = 0
        self.value_short = ''
        self.value_long = ''
        self.face_up = False # Card starts as face down.
        match value:
            case 1: 
                self.value_long = 'Ace'
                self.value_short = 'A'
            case 2: 
                self.value_long = 'Two'
                self.value_short = '2'
            case 3: 
                self.value_long = 'Three'
                self.value_short = '3'
            case 4: 
                self.value_long = 'Four'
                self.value_short = '4'
            case 5: 
                self.value_long = 'Five'
                self.value_short = '5'
            case 6: 
                self.value_long = 'Six'
                self.value_short = '6'
            case 7: 
                self.value_long = 'Seven'
                self.value_short = '7'
            case 8: 
                self.value_long = 'Eight'
                self.value_short = '8'
            case 9: 
                self.value_long = 'Nine'
                self.value_short = '9'
            case 10: 
                self.value_long = 'Ten'
                self.value_short = 't'
            case 11: 
                self.value_long = 'Jack'
                self.value_short = 'J'
            case 12: 
                self.value_long = 'Queen'
                self.value_short = 'Q'
            case 13: 
                self.value_long = 'King'
                self.value_short = 'K'
            case 14: 
                self.value_long = 'Ace'
                self.value_short = 'A'
            case _:
                self.value_long = 'unknown'
                self.value_short = '?'


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
        if variant.lower()[0] == 's':
            return f"{self.suite_short}{self.value_short}"
        if variant.lower()[0] == 'l':
            return f"{self.value_long} of {self.suite_long}"        
        return None
    def is_face_up(self) -> bool:
        return self.face_up
    def set_face_up(self, value:bool = True):
        self.face_up = value
    # Comparison
    def is_higher_than(self, c:'Card') -> bool:
        return c.value > self.value
    def is_lower_than(self, c:'Card') -> bool:
        return c.value < self.value
    def is_equal_to(self, c:'Card') -> bool:
        return c.value == self.value
