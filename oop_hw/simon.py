from os import system
import random
import time

class Simon:

    colors = ["red", "blue", "green", "yellow"]

    def __init__(self):
        self.color_count = 4
        self.color_sequence = []

    def play(self):
        game_on = True
        print("LET'S PLAY A GAME :)")
        time.sleep(2)
        while game_on:
            system("cls")
            game_on = self.take_turn()
            system("cls")
            if game_on:
                print(self.round_success_message())
            else:
                print(self.game_over_message())
            time.sleep(2)
        play_again = input("Wanna play again? (Yes or No)\n> ")
        if play_again.lower().find("y") > -1:
            self.reset_game()


    def take_turn(self):
        self.show_sequence()
        my_sequence = self.require_sequence()
        result = False
        if len(self.color_sequence) == len(my_sequence):
            for color_spot in range(0, len(self.color_sequence)):
                if self.color_sequence[color_spot] == my_sequence[color_spot]:
                    result = True
                else:
                    result = False
                    break
        self.color_sequence = []
        self.color_count += 1
        return result


    def show_sequence(self):
        for num in range(0, self.color_count):
            self.color_sequence.append(self.add_random_color())
            print(self.color_sequence[len(self.color_sequence) - 1])
            time.sleep(1)
            system("cls")

    def require_sequence(self):
        result = input("You turn to repeat the sequence:\nformat=color,color,color\n> ")
        return result.split(",")

    def add_random_color(self):
        return self.colors[random.randint(0, 3)]

    def round_success_message(self):
        return "We have a match!!!!"

    def game_over_message(self):
        return "Uh oh. That's no match. GAME OVER!!!!!"

    def reset_game(self):
        self.color_count = 4
        self.play()


my_game = Simon()
my_game.play()
