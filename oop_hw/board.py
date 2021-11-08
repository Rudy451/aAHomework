#from mancala import Mancala
import time

class Board:
    def __init__(self):
        self.cup_list = [4 for num in range(0, 14)]
        self.update_cup_number(6, -4)
        self.update_cup_number(13, -4)

    def build_board(self):
        self.cup_list = [4 for num in range(0, 14)]
        self.update_cup_number(6, -4)
        self.update_cup_number(13, -4)

    def make_move(self, player, cup_index):
        try:
            cup_index = int(cup_index)
            if not player.within_range(cup_index):
                cup_index = cup_index - 1 if cup_index < 7 else cup_index
                return self.update_cup_numbers(cup_index, player.get_cup_number()) - 1
            else:
                return 15
        except:
            return 15

    def update_cup_number(self, cup_index, value):
        self.cup_list[cup_index] += value

    def update_cup_numbers(self, cup_index, skip_cup_index):
        total_stones = self.cup_list[cup_index]
        for stone in range(0, total_stones + 1):
            stone_number = (total_stones * -1) if stone == 0 else 1
            self.cup_list[cup_index] += stone_number
            cup_index = (cup_index + (2 if cup_index + 1 == skip_cup_index else 1)) % 14
        return cup_index


    def over(self):
        return (sum(self.cup_list[0:6]) or sum(self.cup_list[7:13])) == 0

    def render(self, name1, name2):
        layout = [[], [], [], [], []]
        layout[0].append(" " * len(name1))
        layout[0] += [str(num) if num > 9 else " " + str(num) for num in range(12, 6, -1)]
        layout[0].append(" " * len(name2))
        layout[1] += [(" ") * len(name1)]+ [str(num) if num > 9 else " " + str(num) for num in self.cup_list[12:6:-1]] + [" " * len(name2)]
        layout[2] = name1 + (" " * 19) + name2
        layout[3] += [" " * len(name1)] + [str(num) if num > 9 else " " + str(num) for num in range(1, 7)] + [" " * len(name2)]
        layout[4] += [" " * len(name1)] + [str(num) if num > 9 else " " + str(num) for num in self.cup_list[0:6]] + [" " * len(name2)]
        print(" ".join(layout[0]))
        print(" ".join([str(val) for val in layout[1]]))
        print(layout[2])
        print(" ".join(layout[3]))
        print(" ".join(layout[4]))
