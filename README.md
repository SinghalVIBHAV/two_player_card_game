# Two Player Card Game

This project simulates a simple two player card game where two players compete against each other. It consists of the following components:

* cards.py: Defines the 'Cards' class, which represents a deck of cards and handles shuffling and dealing.
* player.py: Defines the 'Players' class, which represents players in the card game and manages their draw and discard piles.
* play.py: Defines the gameplay logic, including functions for drawing cards, determining winners, and checking the game's progress.
* Unit test for testing various functionalities of the game components.

## How to Run
To run the game execute the 'play.py' script.

## Components
### cards.py
The Cards class provides functionalities related to managing the deck of cards. It includes methods for shuffling the deck and dealing cards to players.

### players.py
The 'Players' class represents players in the card game. It manages each player's draw pile and discard pile, allowing players to draw cards and handle their discard piles.

### play.py
The 'play.py' module contains the gameplay logic for the card game. It includes functions for drawing cards, determining winners based on drawn card values, and checking the game's progress.

## Unit Tests
Unit tests are provided to ensure the correctness of the implemented functionalities. The unit tests cover various scenarios, including drawing cards, determing winners, and handling ties.

* test_task1.py: Contains unit tests for the 'Cards' class, including testing the number of cards in the deck and verifying that shuffling changes the order of cards.
* test_task2.py: Includes unit tests, such as testing drawing a card from an empty draw pile.
* test_task3.py: Contains unit tests for the gameplay logic, ensuring that winners are determined correctly, handling ties, and that the game progresses as expected.