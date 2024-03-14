=======================================================================
            Two Player Card Game Implementation - README
=======================================================================

This project contains the implementation of a simple two player card game in Python. 
It consists of the following components:

1. cards.py
2. players.py
3. play.py
4. Unit tests: test_task1.py, test_task2.py, test_task3.py

To run the game execute the 'play.py' script.

1. cards.py:
   - Description: Defines the Cards class representing a deck of cards.
   - Functionality:
     - Initializes a deck of cards.
     - Provides methods to shuffle the deck and deal cards to players.

2. players.py:
   - Description: Defines the Players class representing players in the card game.
   - Functionality:
     - Initializes players' draw pile and discard pile.
     - Provides methods to set the draw pile, an draw a card.

3. Play.py:
   - Description: Contains the main logic of the card game.
   - Functionality:
     - Implements the game flow, including drawing cards, checking winners, and handling ties.

4. Unit tests:
   - test_task1.py: Contains unit tests for testing the number of cards in a new deck and 
   verifying that shuffling changes the order of cards.
   - test_task2.py: Contains unit tests for testing the situation when drawing from an
   empty draw pile.
   - test_task3.py: Contains unit tests for the overall card game functionality, ensuring
   that winners are determined correctly, handling ties, and that the game progresses as expected.
