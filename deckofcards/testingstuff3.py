import CardDeck

mydeck = CardDeck.Deck()
mydeck.add_traditional_52cards()
mydeck.shuffle()

card_to_find1 = CardDeck.Card(rank=10, suite='clubs')
card_to_find2 = CardDeck.Card(rank=1, suite='diamonds')


pos_of_card_1 = mydeck.find_card(card_to_find1)
take_card_1 = mydeck.take_card(pos_of_card_1)
print(take_card_1 == card_to_find1)

pos_of_card_2 = mydeck.find_card(card_to_find2)
take_card_2 = mydeck.take_card(pos_of_card_2)
print(take_card_2 == card_to_find2)

