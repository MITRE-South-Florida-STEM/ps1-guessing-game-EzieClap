This assignment is open to collaboration with your fellow students.

As with all assignments there is no grading tracked. However, the instructors/TAs will review solutions to give guidance. 

# PS1: Number Guessing Game
The goal of this assignment is to recreate a number guessing game. The game will randomly select a number between 1 and 100. Then prompt the user to guess the number. The computer will then respond with `Too High`, `Too Low` or `You Win`. If the user has not won, they will be given another opportunity to guess.

Please make your code changes only in `main.py`. You can test your code by clicking on the `Run` button.

# RULES
1. Use random number generator to choose a number between 1 and 100. Below is code for choosing the random number (note it is in starter code already).
   ```Python
   import random
   answer = random.randint(1, 100)
   ```
2. Request `Player`'s guess. (Bonus: verify player guess is valid)
3. Check the guess and respond with `Too High`, `Too Low` or `Win`.
4. Repeat loop if player guessed wrong. Otherwise, exit with a congratulatory message.

# TIPS
- You need external loop to check if guess correct
- Use proper logic to respond with `Too High`, `Too Low` or `Win`