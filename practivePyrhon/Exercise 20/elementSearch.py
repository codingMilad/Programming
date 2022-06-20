def ordered(numbers, n):
    if n in numbers:
        return True
    else:
        False

print(ordered([1,2,3,4,5,6,7], int(input("Type in a number please: "))))