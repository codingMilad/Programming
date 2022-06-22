def minimum(arr):
    mini = arr[0]
    for i in arr:
        if i < mini:
            mini = i
    return mini
    

def maximum(arr):
    maxi = arr[0]
    for i in arr:
        if i > maxi:
            maxi = i
    return maxi

print(minimum([-62, 56, 40, 39, -54, 0, -110]))
print(maximum([42, 54, 65, 87, 0]))