a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

if len(a) >= len(b):
    for i in a:
        for j in b:
            if i == j and i not in c:
                c.append(i)
else:
    for i in b:
        for j in a:
            if i == j and j not in c:
                c.append(j)

print(c)