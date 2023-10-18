import random

options=("rock","paper","scissor")
running=True


while running:

    player=None
    computer=random.choice(options)

    while player not in options:
        player=input("enter a choice(rock,paper,scissor):")



    print(f"player:{player}")
    print(f"computer:{computer}")

    if player==computer:
     print("you win!")
    elif   player=="rock" and computer =="scissor":
        print("you win!")
    elif   player=="scissor" and computer =="paper":
        print("you win!")
    elif   player=="paper" and computer =="rock":
        print("you win!")
    else:
        print("you lose!")  
    play_again=input("play again?(y/n)").lower()
    if not  play_again=="y":
        running =False
        print("thnaks for playing!")
