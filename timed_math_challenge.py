import random
import time
operators = ["+" ,"-","*"]
total_problem= 10

input("Press enter to start")
start_time = time.time()

for i in range(total_problem):
    left =random.randint(1,12)
    right =random.randint(1,12)
    operator = random.choice(operators)
    total = str(left) +operator +str(right)
    ans =eval(total)
    while True:
        guess = input("Problem #" + str(i+1)+ ":"+ total+"=")
        if guess == str(ans):
            break

end_time = time.time()
total_time = round(end_time - start_time,2)

print("You finished in =", total_time,"seconds!!")