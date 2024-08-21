import random
print("You have 500 points")
points = 500
gamble = int(input("Input a points to play or input -1 to Quit!"))
while gamble == -1:
    print("Thank you for playing! Goodbye!")
    break
while gamble != -1:
    if gamble < 1 or gamble > points:
        gamble = int(input("Input VALID points to play"))
    if gamble == -1:
        print("Thank you for playing! Goodbye!")
        break
    if gamble > 0 and gamble <= points:
        while points >= 0:
            player1 = random.randint(1,6)
            player2 = random.randint(1,6)
            computer1 = random.randint(1,6)
            computer2 = random.randint(1,6)
            print("you rolled", "[", player1, "]", "[", player2, "]")
            print("the computer rolled", "[", computer1, "]", "[", computer2, "]")
            player = player1 + player2
            computer = computer1 + computer2
            if player > computer:
                win = gamble*2
                points += win
                print("You win", win, "points!")
                print("you have", points, "points")
                gamble = int(input("Input points to play or input -1 to Quit!"))
                if gamble == -1:
                    print("Thank you for playing! Goodbye!")
                    break
                elif gamble < 1 or gamble > points:
                    gamble = int(input("Input VALID points to play"))
            elif player < computer:
                points -= gamble
                if points > 0:
                    print("You lose", gamble)
                    print("you have", points, "points left")
                    gamble = int(input("Input points to play or input -1 to Quit!"))
                    if gamble == -1:
                        print("Thank you for playing! Goodbye!")
                        break
                    elif gamble < 1 or gamble > points:
                        gamble = int(input("Input VALID points to play"))
                if points == 0:
                    print("game over, you have 0 points left")
                    again = input("would you like to play again? (Y/N)")
                    if again == "Y":
                        points = 500
                        print("You have 500 points")
                        gamble = int(input("Input points to play or input -1 to Quit!"))
                        if gamble < 1 or gamble > points:
                            gamble = int(input("Input a VALID points to play"))
                        if gamble == -1:
                            print("Thank you for playing! Goodbye!")
                            break
                        continue
                    elif again == "N":
                        print("Thank you for playing! Goodbye!")
                        break