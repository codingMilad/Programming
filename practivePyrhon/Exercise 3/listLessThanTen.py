randomNumber = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lessThanTen = []

for i in randomNumber:
    if i < 10:
        lessThanTen.append(i)
    else:
        continue

print(lessThanTen)