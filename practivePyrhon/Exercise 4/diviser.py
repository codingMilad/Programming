number = int(input("Pleae enter a number: "))
diviserList = []

for i in range(2,number+1):
    if number%i == 0:
        diviserList.append(i)
    else:
        continue
print(diviserList)