from cards import Cards
from players import Players

cards_won = []  # List to keep track of cards won in each round

# TASK 1
def start_game():
    """
    Initializes the game by creating a deck of cards, shuffling it, dealing cards to
    and setting players' draw pile.

    Returns:
        player1 (Players): The player 1 object.
        player2 (Players): The player 2 object.
    """
    deck = Cards()          # Creates a new deck of cards
    player1 = Players()     # Creates player 1 object
    player2 = Players()     # Creates player 2 object

    deck.shuffle()
    deck.deal()

    player1.set_player(deck.p1)
    player2.set_player(deck.p2)

    return player1, player2

# TASK 2
def draw_cards(player1, player2):
    """
    Draws a card from the draw pile for each player.

    Args:
        player1 (Players): The player 1 object
        player2 (Players): The player 2 object
    """
    player1.draw()
    player2.draw()

    return None

# TASK 3 and 4
def check(player1, player2):
    """
    Compares drawn cards of both players, determines the winner of the round,
    and updates players' discard pile accordingly.

    Args:
        player1 (Players): The player 1 object
        player2 (Players): The player 2 object

    Returns:
        winner (Players or None): The winner of the round. None if it's a tie.
        n (int): Number of cards won in total in a round.
    """
    print(f"Player 1 ({len(player1.drawpile)+len(player1.discardpile)+1} cards): {player1.drawn_card}")
    print(f"Player 2 ({len(player2.drawpile)+len(player2.discardpile)+1} cards): {player2.drawn_card}")

    global cards_won
    cards_won.extend((player1.drawn_card, player2.drawn_card))
    n = len(cards_won)

    if player1.drawn_card > player2.drawn_card: # Player 1 wins
        player1.discardpile.extend(cards_won)   # Add won cards to player 1's discard pile
        print("Player 1 wins this round\n")
        cards_won = []
        winner = player1

    elif player2.drawn_card > player1.drawn_card:   # Player 2 wins
        player2.discardpile.extend(cards_won)       # Add won cards to player 2's discard pile
        print("Player 2 wins this round\n")
        cards_won = []
        winner = player2

    else:   # It's a tie
        print("No winner in this round\n")
        winner = None
    
    return winner, n

if __name__ == '__main__':

    # TASK 1: Start the game, create a shuffled deck of cards and distribute among players
    player1, player2 = start_game()

    # TASK 2, 3, and 4: Play the game until one player runs out of cards 
    play = True
    while play:
        if player1.drawpile == [] and player1.discardpile == []:    # Player 2 wins if player 1 has no cards left
            print("Player 2 wins the game!\n")
            play = False
        elif player2.drawpile == [] and player2.discardpile == []:  # Player 1 wins if player 2 has no cards left
            print("Player 1 wins the game!\n")
            play = False
        else:
            draw_cards(player1, player2)
            check(player1, player2)
