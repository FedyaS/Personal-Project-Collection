import random
from Permutation import permutations
from Permutation import combinations


def gen_no_hits_answers(alphabet, guess, difficulty):
    """Returns list of valid answers, assuming no bulls and cows in a given guess"""
    new_alphabet = [x for x in alphabet if x not in guess]
    alphabet = new_alphabet.copy()
    all_answers = permutations(alphabet, difficulty)
    return all_answers


def gen_bulls_and_cows_answers(alphabet, guess, bulls, cows, difficulty):
    """
    Choose all legal bulls combinations
    For each bull combination
        Call Cows with reduced guess, alphabet, and difficulty
        For each Cow combination reinsert bull combs into correct positions
        Append final combinations into result
    """
    result = []
    valid_bulls = combinations(list(range(0, difficulty)), bulls)
    new_difficulty = difficulty - bulls
    for bull_combination in valid_bulls:
        removed_letters = [guess[x] for x in bull_combination]
        new_alphabet = [x for x in alphabet if x not in removed_letters]
        new_guess = [x for x in guess if x not in removed_letters]
        cow_combinations = gen_cows_only_answers(new_alphabet, new_guess, cows, new_difficulty)
        for cow_combination in cow_combinations:
            result.append(reinsert_letters(guess, bull_combination, cow_combination))
    return result


def gen_bulls_only_answers(alphabet, guess, bulls, difficulty):
    """Returns list of all valid answers, for hint with bulls
        Selects bulls, for all possible indexes of bulls in guess.
        For each combination of bulls, we reduce difficulty by number of bulls and reduce alphabet by all letters in guess
        Then we generate all possible combinations using newly reduced difficulty and alphabet
        Then we insert bulls from guess into proper position for each possible combination
    """
    valid_bulls = combinations(list(range(0, difficulty)), bulls)
    new_alphabet = [x for x in alphabet if x not in guess]
    new_difficulty = difficulty - bulls
    new_combinations = permutations(new_alphabet, new_difficulty)
    result = []

    for combination_of_bull_indexes in valid_bulls:
        for new_combination in new_combinations:
            result.append(reinsert_letters(guess, combination_of_bull_indexes, new_combination))
    return result

def gen_cows_only_answers(alphabet, guess, cows, difficulty):
    """ Generate all possible positions of cows
        Then for each combination of cows positions
            Generate all possible answers using alphabet reduced by non-cows
            Then remove answers with cows on the same position as in guess
            Append remaining answers into the result
    """
    result = []
    valid_cows = combinations(list(range(0, difficulty)), cows)
    for cow_positions in valid_cows:
        new_alphabet = []
        for x in alphabet:
            if x not in guess:
                new_alphabet.append(x)
            for i in cow_positions:
                if x == guess[i]:
                    new_alphabet.append(x)
        new_combinations = permutations(new_alphabet, difficulty)
        for combination in new_combinations:# filtering out
            good_combination = True
            for i in cow_positions:
                if combination[i] == guess[i]:
                    good_combination = False
                if guess[i] not in combination:
                    good_combination = False
            if good_combination:
                result.append(combination.copy())
    return result


def reinsert_letters(letters_list, letter_positions, combination=[]):
    result = combination.copy()
    for i in range(0, len(letter_positions)):
        result.insert(letter_positions[i], letters_list[letter_positions[i]])

    return result

class BullsAndCowsAI:
    def __init__(self, difficulty, alphabet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]):
        self.difficulty = difficulty
        self.alphabet = alphabet
        self.all_possible_answers = []
        self.gen_all_answers()
        self.last_guess = []
        self.number_last_bulls = 0
        self.number_last_cows = 0
        self.reduced_answers = []


    def gen_all_answers(self):
        self.all_possible_answers = permutations(self.alphabet, self.difficulty)

    def count_possible_answers(self):
        return len(self.all_possible_answers)

    def make_guess(self):
        self.last_guess = random.choice(self.all_possible_answers)
        return self.last_guess

    def receive_hint(self, hint):
        self.number_last_bulls = hint[0]
        self.number_last_cows = hint[1]

    def analyze_hint(self):
        self.reduced_answers = []
        if self.number_last_bulls == 0 and self.number_last_cows == 0:
            self.reduced_answers = gen_no_hits_answers(self.alphabet, self.last_guess, self.difficulty)
        elif self.number_last_bulls > 0 and self.number_last_cows == 0:
            self.reduced_answers = gen_bulls_only_answers(self.alphabet, self.last_guess, self.number_last_bulls, self.difficulty)
        elif self.number_last_bulls == 0 and self.number_last_cows > 0:
            self.reduced_answers = gen_cows_only_answers(self.alphabet, self.last_guess, self.number_last_cows, self.difficulty)
        else:
            self.reduced_answers = gen_bulls_and_cows_answers(self.alphabet, self.last_guess, self.number_last_bulls, self.number_last_cows, self.difficulty)

    def merge_answers(self):
        answers = [x for x in self.reduced_answers if x in self.all_possible_answers]
        self.all_possible_answers = answers

    def run_hint_through_new_answers(self, hint):
        self.receive_hint(hint)
        self.analyze_hint()
        self.merge_answers()




# class BullsAndCowsAI:
#     def __init__(self, difficulty):
#         self.difficulty = difficulty
#         self.list_of_randoms = []
#         self.list_of_guesses = []
#         self.list_of_hints = []
#         self.guess = []
#         self.list_of_all_possible_answers = []
#         self.randomize_numbers()
#         self.generate_list_of_all_possible_answers()
#
#     def randomize_numbers(self):
#         for number in range(0, 10):
#             i = 0
#             while i == 0:
#                 i = 1
#                 x = random.randrange(0, 10)
#                 idx = list_tools.locate_idx(x, self.list_of_randoms)
#                 if list_tools.is_found(idx, self.list_of_randoms):
#                     i = 0
#             self.list_of_randoms.append(x)
#
#     def get_guess(self):
#         self.calculate_guess()
#         return self.guess
#
#     def calculate_guess(self):
#         matching_guess_idx = 0
#         start_idx = 0
#         current_guess = []
#         while matching_guess_idx >= 0:
#             # print("While start:", start_idx, "guess", self.guess, "list_of_guesses", self.list_of_guesses)
#             current_guess = self.attempt_to_gen_new_guess(start_idx)
#             matching_guess_idx = list_tools.locate_idx(current_guess, self.list_of_guesses)
#             start_idx = start_idx + 1
#             # print("While end: ", start_idx, "guess", current_guess, "list_of_guesses", self.list_of_guesses)
#             if start_idx > 20:
#                 break
#         self.guess = current_guess
#         self.list_of_guesses.append(current_guess)
#
#     def attempt_to_gen_new_guess(self, start_idx):
#         i = start_idx
#         current_guess = []
#         while len(current_guess) < self.difficulty:
#             # print("index out of range: ", i)
#             # print("current_guess", current_guess)
#             # print("list_of_randoms",  self.list_of_randoms)
#             # print("list_of_guesses", self.list_of_guesses)
#             current_guess.append(self.list_of_randoms[i])
#             i = i + 1
#         return current_guess
#
#     def receive_hint(self, BullsAndCowsHint):
#         self.LastBulls = BullsAndCowsHint[0]
#         self.LastCows = BullsAndCowsHint[1]
#         self.list_of_hints.append(BullsAndCowsHint)
#
#     def generate_list_of_all_possible_answers(self):
#         self.list_of_all_possible_answers = permutations(self.list_of_randoms, self.difficulty)
#
#     def list_of_potentials_and_list_of_bulls_to_list_of_answers(self, potentials, bulls):
#         pass