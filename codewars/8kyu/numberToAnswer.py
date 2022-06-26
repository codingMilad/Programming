def how_much_i_love_you(nb_petals):
    arr = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    if nb_petals%6==1:
        return "I love you"
    elif nb_petals%6==2:
        return "a little"
    elif nb_petals%6==3:
        return "a lot"
    elif nb_petals%6==4:
        return "passionately"
    elif nb_petals%6==5:
        return "madly"
    else:
        return "not at all"

# def how_much_i_love_you(nb_petals):
#     dict = {1:'I love you',
#             2:'a little',
#             3:'a lot',
#             4:'passionately',
#             5:'madly',
#             0:'not at all'}
#     return dict.get(nb_petals % 6)

print(how_much_i_love_you(4))
print(how_much_i_love_you(3))
print(how_much_i_love_you(1))

