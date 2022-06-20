import random

start = True


number = random.randint(1,9)

guess = 0

while start != "exit":
    player = int(input("Guess the number: "))
    if number == player:
        guess += 1
        print("Thats the number, you needed ", guess, "attempts")
        break
    elif player > number:
        print("You guessed too high!")
        guess += 1
        start = input("type exit if you want to stop, anything else to continue! ")
    else:
        print("You guessed too low!")
        guess += 1
        start = input("type exit if you want to stop, anything else to continue! ")
