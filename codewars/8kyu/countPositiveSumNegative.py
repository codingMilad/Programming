def count_positives_sum_negatives(arr):
    positive = 0
    negative = 0
    if len(arr) == 0:
        return []
    for i in arr:
        if i > 0:
            positive += 1
        else:
            negative -= -i
    return [positive, negative]

print(count_positives_sum_negatives([]))
print(count_positives_sum_negatives([1,3,5,2,6,-5,-9,-3,-5,-7]))
