#This is a program about rock paper scissors

import random

Options = ["Rock", "Paper", "Scissors"]


print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")

while True:
    Choice = input("Chose an option: ")
    AI = random.choice(Options)

    if Choice == "Rock":
        print(AI + "\n")
        if AI == "Scissors":
            print("you win!")
            break
        if AI == "Paper":
            print("you lose")
            break
        if AI == "Rock":
            print("try again")
            pass
    
    if Choice == "Paper":
        print(AI + "\n")
        if AI == "Rock":
            print("you win!")
            break
        if AI == "Scissors":
            print("you lose")
            break
        if AI == "Paper":
            print("try again")
            pass
    
    if Choice == "Scissors":
        print(AI + "\n")
        if AI == "Paper":
            print("you win!")
            break
        if AI == "Rock":
            print("you lose")
            break
        if AI == "Scissors":
            print("try again")
            pass
    
    else:
        print("Invaild Option")

    if Choice == "Quit":
        break