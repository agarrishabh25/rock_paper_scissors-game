import random

while True:
  a= input("If u want to roll the dice ? (y/n)")
  if(a=='y' or a=='Y'):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print((die1, die2))
  elif(a=='N' or a=='n'):
    print("Thank you for playing ")
    break
  else :
    print("Invalid choice try again ")
  