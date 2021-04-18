import unittest
import sys
import logging
import BullsAndCowsAI
import BullsAndCows
import Permutation


class BullsAndCowsAITests(unittest.TestCase):

    def test_no_hits_difficulty_1(self):
        all_answers = BullsAndCowsAI.gen_no_hits_answers(["a", "b", "c", "d"], ["b"], 1)
        expected = [["a"], ["c"], ["d"]]
        self.assertListEqual(expected, all_answers)

    def test_no_hits_difficulty_2(self):
        all_answers = BullsAndCowsAI.gen_no_hits_answers(["a", "b", "c", "d"], ["a", "b"], 2)
        expected = [["c", "d"], ["d", "c"]]
        self.assertListEqual(expected, all_answers)

    def test_no_hits_difficulty_3(self):
        all_answers = BullsAndCowsAI.gen_no_hits_answers(["a", "b", "c", "d", "e", "f"], ["a", "b", "c"], 3)
        expected = [["d", "e", "f"],
                    ["d", "f", "e"],
                    ["e", "d", "f"],
                    ["e", "f", "d"],
                    ["f", "d", "e"],
                    ["f", "e", "d"]
                    ]
        self.assertListEqual(expected, all_answers)

    def reinsert_bulls(self, bull_positions, bull_values, combinations):
        for combination in combinations:
            for i in range(0, len(bull_positions)):
                combination.insert(bull_positions[i], bull_values[i])
        return combinations

    def test_reinsert_bulls(self):
        list1 = self.reinsert_bulls([0], [1], [[3, 4], [3, 5]])
        self.assertListEqual([[1, 3, 4], [1, 3, 5]], list1)

        list2 = self.reinsert_bulls([0, 2], [1, 2], [[3, 4], [3, 5]])
        self.assertListEqual([[1, 3, 2, 4], [1, 3, 2, 5]], list2)

        list3 = self.reinsert_bulls([2, 3], [1, 2], [[3, 4], [3, 5]])
        self.assertListEqual([[3, 4, 1, 2], [3, 5, 1, 2]], list3)

    def select_bulls(self, guess, number_of_bulls):
        selected_bulls = []
        position_alphabet = list(range(0, len(guess)))
        all_bull_positions = BullsAndCowsAI.permutations(position_alphabet, number_of_bulls)
        for bulls_pos_indexes in all_bull_positions:
            bull_values = []
            for p in bulls_pos_indexes:
                bull_values.append(guess[p])
            selected_bulls.append([bulls_pos_indexes, bull_values])
        return selected_bulls


    def test_select_one_bull_of_two_positions(self):
        combinations = self.select_bulls([2, 3], 1)
        expected_combinations = [
            [[0], [2]],
            [[1], [3]]
         ]
        self.assertListEqual(expected_combinations, combinations)

    def test_reinsert_letters(self):
        result = BullsAndCowsAI.reinsert_letters(["a", "b", "*", "*"], [0, 1], ["c", "d"])
        self.assertListEqual(["a", "b", "c", "d"], result, "reinsert letters")

        result = BullsAndCowsAI.reinsert_letters(["*", "a", "*", "b"], [1, 3], ["c", "d"])
        self.assertListEqual(["c", "a", "d", "b"], result, "reinsert letters")

    def test_only_bulls_difficulty_2(self):
        all_answers = BullsAndCowsAI.gen_bulls_only_answers(["a", "b", "c", "d"], ["a", "b"], 1, 2)
        expected = [["a", "c"], ["a", "d"],
                    ["c", "b"], ["d", "b"]
                    ]
        self.assertListEqual(expected, all_answers)

    def test_only_bulls_difficulty_3(self):
        all_answers = BullsAndCowsAI.gen_bulls_only_answers(['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c'], 1, 3)
        expected = [
                    ['a', 'd', 'e'],
                    ['a', 'e', 'd'],
                    ['d', 'b', 'e'],
                    ['e', 'b', 'd'],
                    ['d', 'e', 'c'],
                    ['e', 'd', 'c']
                ]
        self.assertListEqual(expected, all_answers)


    def test_only_cow_difficulty_2(self):
        all_answers = BullsAndCowsAI.gen_cows_only_answers(["a", "b", "c", "d"], ["a", "b"], 1, 2)
        expected = [["c", "a"],
                    ["d", "a"],
                    ["b", "c"],
                    ["b", "d"]
                    ]
        self.assertListEqual(expected, all_answers)

    def test_one_bull_one_cow_difficulty_2(self):
        all_answers = BullsAndCowsAI.gen_bulls_and_cows_answers(['a', 'b', 'c', 'd'], ['a', 'b', 'c'], 1, 1, 3)
        expected = [
                    ['a', 'd', 'b'],
                    ['a', 'c', 'd'],
                    ['d', 'b', 'a'],
                    ['c', 'b', 'd'],
                    ['d', 'a', 'c'],
                    ['b', 'd', 'c']
                    ]
        self.assertListEqual(expected, all_answers, 'one bull one cow')


class BullsAndCowsGuessesTests(unittest.TestCase):
    def test_initialization(self):
        AI = BullsAndCowsAI.BullsAndCowsAI(3)
        self.assertEqual(Permutation.number_of_permutations(len(AI.alphabet), AI.difficulty), AI.count_possible_answers())

    def test_make_guess(self):
        AI = BullsAndCowsAI.BullsAndCowsAI(3)
        self.assertIn(AI.make_guess(), AI.all_possible_answers)

    def test_one_bull(self):
        AI = BullsAndCowsAI.BullsAndCowsAI(3)
        AI.last_guess = AI.all_possible_answers[0]
        AI.receive_hint([1, 0])
        AI.analyze_hint()
        # 126 is the # Permutations, given hint of 1 bull in difficulty 3, alphabet size 10. # = 7P2 * 3
        self.assertEqual(126, len(AI.reduced_answers))

    def test_reduction(self):
        AI = BullsAndCowsAI.BullsAndCowsAI(3)
        AI.last_guess = AI.all_possible_answers[0]
        AI.receive_hint([1, 0])
        AI.analyze_hint()
        AI.merge_answers()
        self.assertEqual(126, len(AI.all_possible_answers))

    def test_second_reduction(self):
        AI = BullsAndCowsAI.BullsAndCowsAI(3)
        AI.last_guess = [1, 2, 3]
        AI.run_hint_through_new_answers([1, 0])
        # self.assertListEqual([0], AI.all_possible_answers)
        AI.last_guess = [1, 4, 5]
        AI.run_hint_through_new_answers([1, 1])
        # self.assertListEqual([0], AI.all_possible_answers)

    def test_game_vs_ai(self):
        game = BullsAndCows.BullsAndCows()
        game.generate_game(3)
        ai = BullsAndCowsAI.BullsAndCowsAI(3)
        i = 0
        solved = 0
        while i < 10:
            i += 1
            guess = ai.make_guess()
            hint = game.interpret_guess(guess)
            if hint == [3, 0]:
                solved = 1
                break
            ai.run_hint_through_new_answers(hint)
        self.assertEqual(1, solved)



if __name__ == '__main__':
    unittest.main()
