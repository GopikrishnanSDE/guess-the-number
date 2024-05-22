#GUESS THE NUMBER
import random
import math
lower=int(input("enter the lowest number"))
upper=int(input("enter the highest number"))
x=random.randint(lower, upper)
print("you have got",round(math.log(upper-lower+1,2)),"chance to win")
count=0
while(count< round(math.log(upper-lower+1,2))):
      guess=int(input("guess the number"))
      if(guess==x):
          print("congratulation you got the number")
          break
      elif(guess<x):
          print("guess higher")
          count+=1
      elif(guess>x):
          print("guess lower")
          count+=1
if count>math.log(upper-lower+1,2):
    print("better luck next time")
    
