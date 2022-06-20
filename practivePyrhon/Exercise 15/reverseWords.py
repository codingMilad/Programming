a = input("Type a sentence: ")
def reverseWords(a):
    x = a.split()
    x = x[::-1]
    return " ".join(x)

print(reverseWords(a))