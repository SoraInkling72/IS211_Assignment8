import time
import random

MAX_SCORE = 100


def roll_die():
    """Function that rolls the die"""
    return random.randint(1, 6)


class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def show(self):
        """Print my score"""
        print(f"{self.name}'s score is {self.total_score}")

    def turn(self):
        """Player plays a turn"""
        turn_total = 0
        roll_hold = "r"
        while roll_hold != "h":
            die_value = roll_die()
            print(f"{self.name} rolled a {die_value}.")
            if die_value == 1:
                print(f"****** You scored ZERO POINTS!! ******")
                return
            else:
                turn_total += die_value
                print(f"{self.name} has {turn_total} points in this turn.")
                print(f"If you hold, your score will be {self.total_score + turn_total}")
                roll_hold = input("Roll(r) or Hold(h)? ").lower()

        self.total_score += turn_total


class ComputerPlayer(Player):
    def __int__(self, name):
        self.name = name
        self.total_score = 0

class Pig:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None

    def check_winner(self):
        """Returns True if there is a winner"""
        for player in self.players:
            if player.total_score >= MAX_SCORE:
                self.winner = player
                return True

        return False

    def play(self):
        """Play the game"""
        player_idx = 0
        while not self.check_winner():
            current_player = self.players[player_idx]
            print(f"It's {current_player.name} turn...")
            # play the game
            current_player.turn()
            player_idx = (player_idx + 1) % 2

        print(f"The winner is {self.winner.name}...")
        self.winner.show()


if __name__ == "__main__":
    player1 = Player("You")
    player2 = Player("Computer")
    game = Pig(player1, player2)
    game.play()