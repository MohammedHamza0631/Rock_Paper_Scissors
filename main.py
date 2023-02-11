import random

rock = '''  
    ROCK
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    PAPER
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    SCISSORS
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
tools = [rock, paper, scissors]
print("-------------------------------------------------------")
print("\t\t\t\tWelcome to the game")
print("-------------------------------------------------------")
print()
user = int(
    input("""Enter your choice:
0 for Rock
1 for Paper
2 for Scissors
=>"""))
print()
print(f"Your choice:\n{tools[user]}")
computer = random.randint(0, 2)
print(f"Computer chose:\n{tools[computer]}")
# Case when user wins
# rock vs scissor
# scissors vs psper
# paper vs rock
if user == 0 and computer == 2:
    print("You Win")
elif user == 0 and computer == 1:
    print("You Lose ☠")
elif user == 1 and computer == 0:
    print("You win")
elif user == 1 and computer == 2:
    print("You Lose ☠")
elif user == 2 and computer == 0:
    print("You Lose ☠")
elif user == 2 and computer == 1:
    print("You win")
elif user == computer:
    print("It's a Draw")
