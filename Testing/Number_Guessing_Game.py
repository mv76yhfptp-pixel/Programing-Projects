import random

Number = random.randint(0, 100)

Attempts = 0

while True:
    Attempts += 1
    Choice = int(input("Pick a number between 0 and 100: "))

    if Choice == Number:
        print('You win!')
        break
    if Choice >= Number:
        print("Less")
    if Choice <= Number:
        print("More")

print(f"It took you {Attempts} to get it")