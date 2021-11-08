class Player:
    def __init__(self, name, cup_range, cup_num):
        self.name = name
        self.total_score = 0
        self.side_cup_range = [num for num in cup_range]
        self.cup_number = cup_num

    def prompt(self):
        temp_cup_range = self.side_cup_range
        return input("\n" + "Your turn, " + self.name + ". Please select which cup from your side to grab stones between (" + str(temp_cup_range[0]) + "-" + str(temp_cup_range[len(temp_cup_range) - 1]) + ")\n< ")

    def get_name(self):
        return self.player_name

    def get_cup_number(self):
        return self.cup_number

    def get_cup_range(self):
        return self.side_cup_range

    def within_range(self, value):
        return value >= self.side_cup_range[0] and value <= self.side_cup_range[len(self.side_cup_range) - 1]

    def update_score(self, total):
        self.total_score += total

    def get_score(self):
        return self.total_score
