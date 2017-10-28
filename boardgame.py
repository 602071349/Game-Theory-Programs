#Jiazhou Liu ljzhou@bu.edu
#This programme is baseed on text. When I try to create a GUI by python,
#I encouter some difficulty, as I need to use "multi-threads" to update
#the GUI. I sent a email to Professor Chin, and he told a text-based one
#is okay.
import random


        
def gen_game():
    list1=list(range(random.randint(3,8)))
    for i in range(len(list1)):
        list1[i]=random.randint(1,7)
    return list1

def start_game():
    game=gen_game()
    turn=0
    while end_game(game)==False:
        print(game)
        if turn==0:
            pile_choice=int(input("Enter the pile number(start from 0): "))
            chip_choice=int(input("Enter the chip number(at least 1): "))
            game[pile_choice]-=chip_choice
            turn=1
        else:
            robot_answer=robot(game)
            pile_choice=robot_answer[0]
            chip_choice=robot_answer[1]
            game[pile_choice]-=chip_choice
            print("Robot removes",chip_choice,"chips form pile",pile_choice) 
            turn=0
    print(game)
    if turn==0:
        print("Robot wins!")
    else:
        print("You win!")
    

def end_game(game):
    for i in range(len(game)):
        if game[i]!=0:
            return False
    return True

def robot(game):
    nimsum=get_nimsum(game)
    if nimsum==0:
        pile_choice=random.randint(0,len(game)-1)
        while game[pile_choice]==0:
            pile_choice=random.randint(0,len(game)-1)
        chip_choice=random.randint(1,game[pile_choice])
        return (pile_choice,chip_choice)
    else:
        binary_nimsum=bin(nimsum)[2:]
        k=len(binary_nimsum)
        for i in range(len(game)):
            binary=(bin(game[i]))[2:]
            if len(binary)>=k:
                if binary[-k]=="1":
                    x=i
                    break
        pile_choice=x
        chip_choice=game[x]-get_nimsum([nimsum,game[x]])
        return (pile_choice,chip_choice)
        
                              
        
def get_nimsum(game):
    nimsum=0
    for i in game:
        nimsum=nimsum^i
    return nimsum
    
        
start_game()

        
        
    
    
