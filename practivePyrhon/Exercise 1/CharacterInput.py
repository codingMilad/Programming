name = input("Please enter your name: ")
age = int(input("How old are you? "))
repeat = int(input("How many times do you want me to repeat the sentence? "))

for i in range(0, repeat):
    print("Hi " + name + " you will be 100 year old in " + str(2022+100-age))