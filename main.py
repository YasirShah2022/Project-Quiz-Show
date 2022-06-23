print(r"""________        .__           _________.__                   
\_____  \  __ __|__|_______  /   _____/|  |__   ______  _  __
 /  / \  \|  |  \  \___   /  \_____  \ |  |  \ /  _ \ \/ \/ /
/   \_/.  \  |  /  |/    /   /        \|   Y  (  <_> )     / 
\_____\ \_/____/|__/_____ \ /_______  /|___|  /\____/ \/\_/  
       \__>              \/         \/      \/               """)

# Create two tupels for the quiz data one for questions, and the second for answers indexed to match the questions tupel
questions = ("Q1. Cows have two legs: ", "Q2. Sun is 100 light-years away from earth: ", "Q3. Pink Panther is blue: ", "Q4. Lance Armstrong was the first person to walk on the moon: ")

answers = ("F", "F", "F", "F")

# Create a blank variable to hold user's response for the current quesiton
userInput = ""
# Create a counting variable to count number of correct answers
correctCnt = 0
# Variable to count the total items in the questions tupel
numOfQ = len(questions)

# Message for the user defining a valid response
print('Please enter "T" or "F" for your response.')

# Prompt the user with a question and option to enter a "T" or "F" response
for index in range(numOfQ):
  # If the response is not "T" or "F" keep repeating the question
  while (userInput != "T" and userInput != "F"):
    userInput = input(questions[index])
    # Check if the response match the correct answer
    if userInput == answers[index]:
      # Track number of correct count
      correctCnt += 1
  userInput = ""
  
# Once all the quesitons have been answered provide a message with the score 
print(f"You completed the game, your score is {correctCnt}/{len(questions)})")
  


