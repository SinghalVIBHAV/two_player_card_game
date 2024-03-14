import unittest
import sys
import os

dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(dir))

from play import check, draw_cards
from players import Players

class TestCardGame(unittest.TestCase):
    """
    Test cases for the card game functionality.
    """
    def test_winner(self):
        """
        Test if the correct winner is determined when one player has a higher drawn card value.
        """
        player1 = Players()
        player2 = Players()

        player1.drawn_card = 5
        player2.drawn_card = 8

        winner, _ = check(player1, player2)

        self.assertEqual(winner, player2)
    
    def test_winner_after_tie(self):
        """
        Test if the correct number of cards are won after a tie.
        """
        player1 = Players()
        player2 = Players()
        player1.drawpile = [2, 3, 9]
        player2. drawpile = [1, 3, 4]
        play = True
        while play:
            if player1.drawpile == [] and player1.discardpile == []:
                print("Player 2 wins the game!\n")
                play = False
            elif player2.drawpile == [] and player2.discardpile == []:
                print("Player 1 wins the game!\n")
                play = False
            else:
                draw_cards(player1, player2)
                _, n_cards_won = check(player1, player2)

        self.assertEqual(n_cards_won, 4)

if __name__ == '__main__':
    unittest.main()
