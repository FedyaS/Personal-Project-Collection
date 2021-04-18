'''
Program generates set of digits (limit of digits and number of digits can be determined by user), digits can not repeat
    Ex: (1, 5, 4, 8, 2)

Program says "ready" and "input your guess"

User inputs guess
    Ex: (1, 2, 3, 4, 5)
        (b, c, _, c, c)
Program outputs number in correct position and number in incorrect position (via bull and cow)
    Ex: (1 bull, 3 cow)

User continues guessing until gets everything correct (There can be a limit set to the # of guesses the user gets)
    Ex: (1, 5, 4, 8, 2)

Once correct, program outputs victory message
'''

import BullsAndCows
import BullsAndCowsAI

my_game = BullsAndCows.BullsAndCows()

difficulty = 0

# print(BullsAndCowsAI.combinations(["a", "b", "c", "d"], 3))

def start_game():
    print("Welcome to Bulls and Cows\n Choose your game mode:")
    i = 0
    while i == 0:
        try:
            game_mode = int(input("1: Human Guesses vs AI\n"
                                  "2: AI Guesses vs Human\n"
                                  "3: AI vs AI\n"
                                  "Enter 1, 2, or 3:\n"))
            i = 1
        except:
            print("Please enter an integer 1, 2, or 3")

    return game_mode


def human_guesses():
    print("What difficulty?")
    global difficulty
    difficulty = int(input())
    my_game.generate_game(difficulty)


# AI guess vs human
def game_mode_2():
    diff = int(input("Make a secret number. Write it down. How long is your number?\n"))
    ai = BullsAndCowsAI.BullsAndCowsAI(diff)
    run = True
    while run:
        guess = ai.make_guess()
        print("There are currently", len(ai.all_possible_answers), "possible answers!")
        print("I guess: ", guess, end =' ')
        bulls_cows = input("\nHow many bulls and how many cows are there (enter with space)?:\n")
        h = bulls_cows.split()
        hint = [int(x) for x in h]
        if hint == [diff, 0]:
            print("Looks like I won! Good game :)")
            break
        ai.run_hint_through_new_answers(hint)

# AI vs AI
def game_mode_3():
    print("AI will play vs AI")
    difficulty = int(input("What difficulty shall the ai play at (how many #s to guess):\n"))
    ai = BullsAndCowsAI.BullsAndCowsAI(difficulty)
    answer = my_game.generate_game(difficulty)
    run = True
    while run:
        guess = ai.make_guess()
        print("There are currently", len(ai.all_possible_answers), "possible answers!")
        print("\nAI 1- Guesses ", guess)
        if guess == answer:
            print(guess, "Is the correct answer\n"
                         "AI 1 has guessed correctly and won the game\n"
                         "AI 2 says: Good job bro, I always believed in you")
            break
        hint = my_game.interpret_guess(guess)
        print("AI 2- Gives Hint ", hint)
        ai.run_hint_through_new_answers(hint)
        x = input("\nContinue")


def RunHumanGuessesGame():
    input_guess=input("Enter your guess, separated by spaces:\n")
    GuessStr = input_guess.split()
    Guess=[]
    for guess in GuessStr:
        integer_guess=int(guess)
        Guess.append(integer_guess)
    hint = my_game.interpret_guess(Guess)
    return hint


def HintToText(hint):
    hint_text = ("Bulls: " + str(hint[0]) + "  Cows: " + str(hint[1]))
    return hint_text


def RepeatRunHumanGuessesGame():
    correct_guess=False
    while correct_guess == False:
        hint=RunHumanGuessesGame()
        print(HintToText(hint))
        if hint == [difficulty, 0]:
            correct_guess = True
            print("You won, Nice Job!!!\n The numbers were:", my_game.BullsAndCowsList)

# Human guesses vs AI
def game_mode_1():
    human_guesses()
    RepeatRunHumanGuessesGame()

i = True
while i == True:
    game_mode = start_game()
    if game_mode == 1:
        game_mode_1()
    elif game_mode == 2:
        game_mode_2()
    elif game_mode == 3:
        game_mode_3()
    n = input("\nWant to play again?\n")
    if "n" in n or "N" in n:
        break