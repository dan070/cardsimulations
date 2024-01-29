import CardDeck

mydeck = CardDeck.Deck()
mydeck.add_traditional_52cards()
mydeck.shuffle()

card_to_find1 = CardDeck.Card(rank=10, suite='clubs')
card_to_find2 = CardDeck.Card(rank=1, suite='diamonds')
