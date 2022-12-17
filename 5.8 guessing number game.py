def play_game():
    Randno=randint(1,20)
    count=1
    while(1):
        guess=int(input())
        
        if guess>Randno:
            print("Too high")
            count+=1
        elif guess<Randno:
            print("Too low")
            count+=1
        elif guess==Randno:
            break

    return count
       
from random import *
name=input("Hello! what is your name?:")
print(f"Well,{name},I am thinking of a number between 1 and 20",'take a guess',sep='\n')

x=play_game()
print(f'Good job, {name}! You guessed my number in {x} guesses!')



