import time
import random

class Player():
    def __init__(self, roll, winner):
        self.roll = [random.randint(1, 6) , 'hold']
        self.winner = sum(random.radint(1,6) >= 100)

    def PlayerTurn(self, roll):
        if self.roll == 1 or 'hold':
            pass
        if self.roll == 2-6:
            self.winner

    def winner(self, winner):
        if self.PlayerTurn() >= 100:
            print ('Player Wins')

class Computer(Player):
    def __init__(self, roll, winner):
        self.roll = [random.randint(1, 6) , 'hold']
        self.winner = sum(random.radint(1,6) >= 100)
    def ComputerTurn(self):

class PlayerFactory():


class Game():

class TimedGameProxy():

Winner = Player(roll, winner)

Winner.winner()

exit(Pig)

if __name__ == "__main__":