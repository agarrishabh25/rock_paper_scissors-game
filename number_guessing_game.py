import random

number = random.randint(1,100)
while True :
   a= int(input("Guess a number between 1 and 100 "))
   if(a>100 or a<1):
      print("Please enter a number in a given range")
   else:
      if(a> number):
        print("Too High!")
      elif (a<number):
        print("Too low!")
      elif(a== number):
        print("Congrulations! you guessed the number ")
        break  
      else:
        print("Please enter a valid number")
        