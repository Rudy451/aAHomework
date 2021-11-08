from os import system
import time

from board import Board
from player import Player

import random

class Mancala:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = self.player1 if random.randint(0, 1) == 0 else self.player2

    def play(self):
        while not self.board.over():
            system("cls")
            self.board.render(self.player1.name, self.player2.name)
            self.take_turn()
        print(self.current_player.get_name() + "WINS!!!! Score: " + self.get_current_player.get_score())

    def update_everything(self, cup_index):
        total_stones = self.board.cup_list[cup_index]
        player_score = self.board.cup_list[self.current_player.get_cup_number()]
        if self.current_player.get_score() != player_score:
            self.current_player.update_score(player_score)
        if(total_stones == 1) and (cup_index != self.current_player.get_cup_number()):
            self.switch()

    def take_turn(self):
        last_cup_index = self.board.make_move(self.player2 if self.current_player == self.player1 else self.player1, self.current_player.prompt())
        if last_cup_index == self.current_player.get_cup_number():
            print(self.current_player.get_name() + ", you ended in your cup. Take another turn!")
        elif last_cup_index == 15:
            temp_cup_range = self.current_player.get_cup_range()
            print("Incorrect. Please enter between ", str(temp_cup_range[0]) and str(temp_cup_range[len(temp_cup_range) - 1]))
        else:
            self.update_everything(last_cup_index)

    def switch(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

player1 = Player("David", range(7, 14), 13)
player2 = Player("Goliath", range(1, 7), 6)
new_game = Mancala(player1, player2)
new_game.play()
