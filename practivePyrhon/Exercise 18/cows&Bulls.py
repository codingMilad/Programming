import random

def cowAndBulls():
    randomNumber = str(random.randint(1000,9999))
    print(randomNumber)
    cows = 0
    while cows != 4:
        cows = 0
        bulls = 0
        number = input("")
        for i in range(4):
            if (number[i] in randomNumber) and (number[i] == randomNumber[i]):
                cows += 1
            elif (number[i] in randomNumber) and (number[i] != randomNumber[i]):
                bulls += 1
        print("cows: ", cows, " bulls: ", bulls)

cowAndBulls()