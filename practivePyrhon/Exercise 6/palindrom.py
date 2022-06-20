word = input("Please type in a word: ")

if word[::-1] == word:
    print("Its a palindrom")
else:
    print("Its not a palindrom")