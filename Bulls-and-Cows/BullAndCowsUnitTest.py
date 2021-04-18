import unittest
import BullsAndCows

class MyTestCase(unittest.TestCase):

    def setup_game(self):
        self.game = BullsAndCows.BullsAndCows()
        self.game.BullsAndCowsList = [0, 2, 6]
        self.game.difficulty = 3;

    def test_one_cow(self):
        self.setup_game()
        self.assertListEqual(self.game.interpret_guess([2, 3, 4]) , [0, 1], "One Cow works")

    def test_one_bull(self):
        self.setup_game()
        self.assertListEqual(self.game.interpret_guess([3, 2, 4]) , [1, 0], "One Bull works")

    def test_one_bull_one_cow(self):
        self.setup_game()
        self.assertListEqual(self.game.interpret_guess([6, 2, 4]) , [1, 1], "One Bull One Cow works")


    def test_correct_guess(self):
        self.setup_game()
        self.assertListEqual(self.game.interpret_guess([0, 2, 6]) , [3, 0], "Correct guess works")

if __name__ == '__main__':
    unittest.main()
