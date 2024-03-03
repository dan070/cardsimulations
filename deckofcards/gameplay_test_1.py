# Testing of game play, "Åsna"

import CardDeck

no_of_players = 4

player_closed_deck =  [CardDeck.Deck() for _ in range(4)] 
player_open_deck = [CardDeck.Deck() for _ in range(4)] 

starting_deck = CardDeck.Deck()
starting_deck.add_traditional_52cards()

# Deal cards to the closed deck of all players
while starting_deck.card_count() > 0 :
    for i in player_closed_deck:
        dealcard = starting_deck.take_card()
        dealcard.set_face_up(False)
        i.put_card(dealcard)

# Function to Check if someone wins.
def victory_condition(all_decks: CardDeck.Deck) -> bool :
    for d in all_decks:
        if d.card_count() == 0 : return True
    return False

player = 0

# Game loop
while victory_condition(player_closed_deck) == False:
    # Player that plays now


    # States : has-placed-card somewhere. face-up-empty, face-down-empty.
    # face-up-empty = false + can_put_middle = true
    # face-up-empty = false + can_put_otherplayer = true


    # face

    #   can i put middle. if so, update states.
    #   can i put other player. if so, update states.
    #   
    
    # Check face up - can i put middle, other player. Update has-placed-card to true. Update face-up-empty.
    # 
    # If i 

    # Player loop : 
    # Do i have a face up ? 
    # Yes - 
    #   Can current face up be placed in the middle. Loop face-up.
    #   Can current face up be placed on any other player. Loop face-up.
    # No - 
    # Do i have face down ? 
    #   No - Flip face up pile. And put into face down.
    #   Yes - Do nothing.
    # 
    #   Take card.
    #   Can it be placed in the middle. Then exit and start from top.
    #.  Can it be place on other player. Then exit and start from top.
    #.  Can it be 
    #   
    # No -
    #   
    #
    # If I have closed deck cards, else. 
    # 



    # Take top card
    # Can my top card be place in the middle
    # Can my 


starting_deck
player_closed_deck[4].card_count()

