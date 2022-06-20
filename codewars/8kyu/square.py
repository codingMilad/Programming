# square all numbers in an array and add them

def square(array):
    return sum(i**2 for i in array)

print(square([1,2,6,9,3]))