import unittest
import sys
import os

dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(dir))

from cards import Cards

class TestDeck(unittest.TestCase):
    """
    Test cases for the cards class.
    """
    def test_deck_contains_40_cards(self):
        """
        Test if the deck contains 40 cards upon initialization.
        """
        deck1 = Cards()

        self.assertEqual(len(deck1.deck), 40)

    def test_shuffle_deck(self):
        """
        Test if shuffling the deck changes the order of cards.
        """
        deck1 = Cards()
        initial_order = list(deck1.deck)
        deck1.shuffle()

        self.assertNotEqual(list(deck1.deck), initial_order)

if __name__ == '__main__':
    unittest.main()
