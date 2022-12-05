lose=("the computer wins")
win=("you win")
lives=5
score=0
draw=0
comp_lives=7
while True:
    print("to begin fill in the above information")
    username=input("Please enter your username")
    password=input("please enter your password")
    search_file=("access.csw","r")
    for line in search_file:
        if username and password in line:
            print("access granted")
            print("lets begin rock paper scissors")
            print("RULES OF ROCK,PAPER ,SCISSORS")
            print("********************************")
            print("if computer wins you lose a life")
            print("if you win computer loses a life")
            print("if all lives get over,you lose and vice versa")
            while True:
                rps=input("rock paper or scissors")
                import random
                computer=("rock","paper","scissors")
                computer=random.choice(computer)
                #computer chose rock
                if computer="rock"and rps="scissors":
                    print("the computer chose",computer)
                    print(lose)
                    lives-=lives
                if computer="rock"and rps="paper":
                    print("the computer chose",computer)
                    print(win)
                    score+=score
                if computer="rock"and rps="rock":
                    print("the computer chose",computer)
                    print("match has drawed")
                    draw+=draw
                #computer chose paper 
                if computer="paper"and rps="scissors":
                    print("the computer chose",computer)
                    print(win)
                    score+=score
                if computer="paper"and rps="rock":
                    print("the computer chose",computer)
                    print(lose)
                    lives-=lives
                if computer="paper"and rps="paper":
                    print("the computer chose",computer)
                    print("match has drawed")
                    draw+=draw
                #computer chose scissors 
                if computer="scissors"and rps="rock":
                    print("the computer chose",computer)
                    print(win)
                    score+=score
                if computer="scissors"and rps="paper":
                    print("the computer chose",computer)
                    print(lose)
                    lives-=lives
                if computer="scissors"and rps="scissors":
                    print("the computer chose",computer)
                    print("match has drawed")
                    draw+=draw
                             
                               
                     
                    
                    
                    
                    




