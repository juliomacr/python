import random

#choose a random number 
num = random.randint(0, 9)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("you win!!!")
        break
    else:
        print("nope, try again!")

