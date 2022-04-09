'''
  Starter Code for number guessing game
  4/2/22
  Please enter your team members names here:
  Sheperad: Ryan 
  Ezie: Frank
  Kaibo-Asaph: Michael

Pseudo Code:
-Generate random # and assign as answer

-Ask user for input

-Use condition to compare input to random number "RN" our random number/answer
  -If less than "RN", return         output "Too Low"
  -If greater than "RN", return      output "Too High"
  -repeat until /, then return      output "You Win"
'''

#Begin your code here

import random

answer = random.randint(1, 100)

x = int(input("Enter Guess: "))

while x != answer:

  if x > answer:
    print("Too High")
    x = int(input("Take Another Guess: "))

  elif x < answer:
    print("Too low")
    x = int(input("Take Another Guess: "))
    
  else:
    break
    
print("Correct!")