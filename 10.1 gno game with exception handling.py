class TooLargeGuess(Exception):
    pass
def play_game():
    Randno = randint(1, 20)
    count = 1
    while (1):
        try:
            guess = int(input())
            if guess > 20:
                raise TooLargeGuess

            elif guess > Randno:
                print("The entered value is larger than the random no.")

                count += 1
            elif guess < Randno:
                print("The entered value is smaller than the random no.")
                count += 1

            elif guess == Randno:
                return count

        except ValueError:
            print("please enter the valid number between 1 and 20")
        except TooLargeGuess:
            print('Guess the Number only between 1 and 20')

from random import *

name = input("Hello! what is your name?:")
print(f"Well,{name},I am thinking of a number between 1 and 20", 'take a guess', sep='\n')

x = play_game()
print(f'Good job, {name}! You guessed my number in {x} guesses!')



