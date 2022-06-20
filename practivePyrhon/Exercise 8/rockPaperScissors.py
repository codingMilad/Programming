start = True

while start:
    player1 = input("Pick rock, paper or scissors: ")
    player2 = input("Pick rock, paper or scissors: ")
    
    if player1 == player2:
        print("Equal, no one wins")
        start = input("Type False if you want to stop")

    elif player1 == "rock":
        if player2 == "scissors":
            print("Player 1 wins!!!")
            start = input("Type False if you want to stop")
        else:
            print("Player 2 wins!!!")
            start = input("Type False if you want to stop")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins!!!")
            start = input("Type False if you want to stop")
        else:
            print("Player 2 wins!!!")
            start = input("Type False if you want to stop")

    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 wins!!!")
            start = input("Type False if you want to stop")
        else:
            print("Player 2 wins!!!")
            start = input("Type False if you want to stop")