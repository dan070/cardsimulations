# cardsimulations
help me simulate cards 

# Ideas
- The classes are for simulation. 
- There are "cards", and "stacks". 
- The initial stack has to be randomized. 
- A stack can be initialized, with any number of cards. The cards will be created.
- Special initialization can be done. With ace =1 or ace = 14. No court cards. All court cards = 10. etc.

### Cards
- what suite 
    - datatype string, for ease of use. "spades" "hearts"
    - return a ascii symbol as well. There are 4 special ascii that will print the symbol.
- what value
    - datatype integer, for the value. Typically King = 13. But Ace could be = 1 or 14. 
    - the value also has a string datatype, "Queen", "King" etc. 
    - and a string datatype "Q", "K", "A" , "2" etc. 
- Print methods : "toString('short')" ,'long'
- Is face up or face down / flip
- Is compared to another card
    - higher
    - lower
    - equal
- Is same suite

### Stacks
- Generic list of cards, but has a top and bottom.
- Is constituted by 0..m cards.
- check card - returns a view-only copy of the card.
- take card - takes the card off the stack.
    - Take top card, n:th card from top. 
    - Take bottom card. nth card from bottom.
- Stack shuffle / randomize
- Stack can be empty, and this is not an error. Each function returns empty object.


### Hands
- Hands are also stacks, but with certain logic to facilitate game play. 
- Draw a card from a stack and place on hand. 
- Check if hand has certain combinations of cards. Like "has 3 aces", "all same suite", 
- Flag or calculate certain conditions : "sum of card values"
- Pick out certain cards : "highest card, in x suite", "random card"
- "All cards in suite"
- Hands has mechanism to pipe together selections of cards.
    - if no hearts, and no queen spades, select suite with most cards, take highest card.
    - select suit with highest card, if number of value card > X is more than 2, pick lowest card higher than P.



### General play
Stacks can be pick-up-stacks, or throw-away-stacks, or hands of players.
Cards can be checked against your own. 
Hands are stacks, but they have certain extra functions, that extends the stack.
