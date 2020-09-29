import random

name = input("Player Name : ")

PlayerScore = 0
ComputerScore = 0
choices = ["Rock","Paper","Scissor"]

play=True
count = 0
while play:
    playerChoice = input("your choice : ")
    computerChoice = random.choice(choices)
    print("Computer's choice : ",computerChoice)
    if playerChoice=="Rock" and computerChoice=="Scissor":
        PlayerScore+=1
        print("You won !")
    elif playerChoice=="Rock" and computerChoice=="Paper":
        ComputerScore+=1
        print("You lost !")
    elif playerChoice=="Paper" and computerChoice=="Rock":
        PlayerScore+=1
        print("You won !")
    elif playerChoice=="Paper" and computerChoice=="Scissor":
        ComputerScore+=1
        print("You lost !")
    elif playerChoice=="Scissor" and computerChoice=="Paper":
        PlayerScore+=1
        print("You won !")
    elif playerChoice=="Scissor" and computerChoice=="Rock":
        ComputerScore+=1
        print("You lost !")
    else:
        print("Draw !")
    count+=1
    print("Do you want to play again ? (yes or no)")
    res=input()
    if res=="no":
        play=False
        print(name,end=" ")
        print("'s Score is : ",PlayerScore)
        print("Computer's Score is : ",ComputerScore)
    

