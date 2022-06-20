# num = int(input("Please enter a number: "))
# if num % 4 == 0:
#     print("The number is a multiple of 4")
# elif num % 2 == 0:
#     print("The number is a multiple of 2")
# else:
#     print("Its an odd number!")

num = int(input("Please enter a number: "))
check = int(input("The number to devide it by "))

if num % check == 0:
    print(num, "is a multiple of ", check)
else:
    print(num, "in not a multiple of ", check)