import random

number= random.randint(1,100)
guess=0

while guess != number:
    
    guess=int(input("Enter your Guess:"))
    
    if (guess < number):
        print("Guess Higher!")
    elif (guess > number):
        print("Guess Lower!")
    else:
        print("Congratulations, You Won!")