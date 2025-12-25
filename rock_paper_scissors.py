import random

choices =('r' ,'p','s')
while True:
    user_choice= input("Select Rock,paper,scissors(r/p/s)")
    computer_choice = random.choice(choices)
    if (user_choice not in choices):
        print("Invalid choice!")
        continue

    if (user_choice =='r'):
        print("you chose= ",'👊')
    elif(user_choice =='s'):
        print("you chose",'✂️')
    elif(user_choice =='p'):
        print("you chose",'📃')

    if (computer_choice =='r'):
        print("computer chose= ",'👊')
    elif(computer_choice =='s'):
        print("computer chose",'✂️')
    elif(computer_choice =='p'):
        print("computer chose",'📃')

    if(user_choice==computer_choice):
        print("Tie!")
    elif((user_choice=='r'and computer_choice=='s')or
        (user_choice=='p'and computer_choice=='r')or
        (user_choice=='s'and computer_choice=='p')):
        print("You win !")
    else:
        print("You lose !")
    
    cont = input("Do u want to continue (y/n)")
    if(cont=='n'):
        break