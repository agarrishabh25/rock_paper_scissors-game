num =[1,2,3,4,5]
# menu ={
#     '1' : 200,
#     '2':150,
#     '3': 80,
#     '4' : 100,
#     '5' : 60
# }
print("Welcome to our restaurent .Here's the menu")
order_total =0 
while True:
    print("1 Pizza: Rs200\n2 Pasta: Rs150\n3 Burger: Rs80\n4 Sandwitch: Rs100\n5 Coffee: Rs60")
    choice = int(input("Enter your item number you want to order"))
    if(choice not in num ):
        print("Invalid Try again")
    elif (choice==1):
        print("Order of Pizza is added")
        order_total += 200 
    elif(choice==2):
        print("Order of pasta is added")
        order_total += 150
    elif(choice==3):
        print("Order of Burger is added")
        order_total += 80
    elif (choice==4):
        print("Order of Sandwitch is added")
        order_total += 100
    elif (choice==5):
        print("Order of Cofffee is added")
        order_total += 60
    ques = input("Do you want to order anything else?(y/n)").lower()
    if(ques =='y'):
        continue
    else :
        print("total price you have to pay = " ,order_total )
        break
