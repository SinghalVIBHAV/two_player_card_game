import unittest
import copy
import sys
import os

dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(dir))

from players import Players

class TestPlayer(unittest.TestCase):
    """
    Test cases for the Players class.
    """
    def test_empty_draw_pile(self):
        """
        Test if drawing a card from an empty draw pile results in the discard
        pile to be reshuffled into the draw pile and then being drawn from it. 
        """
        player = Players()
        discardpile = [1, 2, 3, 4]
        player.drawpile = []
        player.discardpile = copy.copy(discardpile)
        player.draw()

        self.assertIn(player.drawn_card, discardpile)

if __name__ == '__main__':
    unittest.main()
