def removeDuplicate(a):
    second = []
    for i in a:
        if i not in second:
            second.append(i)
    return second

print(removeDuplicate([1,1,2,3,4,4]))

