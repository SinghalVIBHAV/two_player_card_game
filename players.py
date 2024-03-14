from cards import Cards

class Players():
    """
    Represents players in a card game.
    """
    def __init__(self):
        """
        Initializes players' draw pile and discard pile.
        """
        self.drawpile = []
        self.discardpile = []
    
    def set_player(self, pile):
        """
        Sets the draw pile for the player.
        
        Args:
            pile (array-like): The pile of cards to be set as the draw pile.
        """
        self.drawpile = pile

        return None
    
    def draw(self):
        """
        Draws a card from the draw pile.

        If the draw pile is empty, reshuffles the discard pile into the draw pile
        and the draws a card from the newly shuffled draw pile.
        """
        if self.drawpile == []: # If draw pile is empty
            # Reshuffle the discard pile into the draw pile
            player_deck = Cards()
            player_deck.shuffle(pile=self.discardpile)
            self.drawpile = player_deck.deck
            self.discardpile = [] # Reset the discard pile

        # Draw the first card from the draw pile
        self.drawn_card = self.drawpile.pop(0)
        
        return None
