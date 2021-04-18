import random

class BullsAndCows:
    def __init__(self):
        self.difficulty = 0
        self.BullsAndCowsList = []

    def generate_game(self, Difficulty):
        if Difficulty > 10:
            Difficulty = 10
        i = 0
        while i < Difficulty:
            is_unique_number = False
            while is_unique_number == False:
                x = (random.randrange(0, 10))
                is_unique_number = True
                for number in self.BullsAndCowsList:
                    if x == number:
                        is_unique_number = False
            self.BullsAndCowsList.append(x)
            i = i + 1
        return self.BullsAndCowsList

    def interpret_guess(self, Guess):
        order_of_guess = 0
        Bulls = 0
        Cows = 0
        for guess in Guess:
            order_of_number = 0
            for number in self.BullsAndCowsList:
                if guess == number and order_of_guess == order_of_number:
                    Bulls = Bulls + 1
                elif guess == number:
                    Cows = Cows + 1
                order_of_number = order_of_number + 1
            order_of_guess = order_of_guess+1
        return [Bulls, Cows]

