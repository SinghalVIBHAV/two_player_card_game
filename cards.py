import numpy as np
import random

class Cards():
    """
    Represents a deck of cards and deals cards to two players
    """
    def __init__(self):
        """
        Initializes the deck of cards and players' hands.
        """
        # Create a deck of cards with numbers from 1 to 10 repeated four times (total 40 cards)
        self.deck = np.tile(np.arange(1, 11, 1), 4)
        # Initialize players' hands as empty lists
        self.p1 = []
        self.p2 = []
    
    def shuffle(self, pile=None):
        """
        Shuffles the deck of cards

        Args:
            pile (array-like): The pile of cards to be shuffled.
                               Defaults to None, which shuffles the main deck.
        """
        if pile == None: # If no pile is specified, shuffle the main deck
            pile = self.deck
        self.n_cards = len(pile)
        # Implement Fisher-Yates Shuffle Algorithm to shuffle the given deck of cards
        for i in range(self.n_cards-1, 0, -1):
            j = random.randint(0, i)
            pile[i], pile[j] = pile[j], pile[i]
        self.deck = pile
        
        return None
    
    def deal(self):
        """
        Deals cards to two players.
        """
        # Iterate over the deck and distribute cards alternately to two players
        for i in range(0, self.n_cards, 2):
            self.p1.append(self.deck[i])
            self.p2.append(self.deck[i+1])
        return None
