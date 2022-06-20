number = int(input("Type in a number and I will tell you if its a prime number or no: "))

for i in range(2, number):
    if number % i == 0:
        print("It`s not a prime number!")
        exit()
    else:
        continue

print("prime")