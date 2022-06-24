def remove_every_other(my_list):
    newArray = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            newArray.append(my_list[i])
    
    return newArray

print(remove_every_other(['Bing', 'Bong', 'Bing']))
print(remove_every_other(['One', 'Two', 'Three', 'Four', 'five']))