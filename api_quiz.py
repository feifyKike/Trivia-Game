import requests
from pprint import pprint
import random

# Ask the user for settings
print("Settings:")
print("\tPress 'q' to quit")
diff_choice = input("\tChoose a difficulty (easy, medium, hard): ")
ques = input("\tHow many questions would you like? ")

# Open the file with all the available topics
counter = 8
with open("topics_questionaire.txt") as f:
    lines = f.readlines()
    for line in lines:
        counter += 1
        print("\t" + str(counter) + "- " + line)
        
topic = input("\nChoose a topic id: ")    

url = 'https://opentdb.com/api.php?amount=' + ques
url += '&category=' + topic + '&difficulty=' + diff_choice

r = requests.get(url)

# Store the API response in a dictionary
response_dict = r.json()

# A function to loop through the questions and display them
def display_ques(response_dict):
    """Show the questions to the user"""
    global points
    print("----Trivia Starts Here----")
    points = 0
    choices_lst = []
    for key, value in response_dict.items():
        if key != 'response_code':
            for question in value:
                for key2, value2 in question.items():
                    if key2 == 'question':
                        print("Q: " + value2 + "\n")
                    elif key2 == 'correct_answer':
                        choices_lst.append(value2)
                        correct_answer = value2
                    elif key2 == 'incorrect_answers':
                        for item in value2:
                            choices_lst.append(item)

                    random.shuffle(choices_lst)

                for choice in choices_lst:
                    print(choice)
                        
                answer = input("-> ")
                
                if answer == correct_answer:
                    points += 1
                    print("Correct!\n")
                    choices_lst.clear()
                # Allowing User to leave
                elif answer == 'q':
                    break
                else:
                    print("Incorrect. The Correct answer is: " + correct_answer + "\n")
                    choices_lst.clear()                   

display_ques(response_dict)

# Add user score and exit
print("Your Score: " + str(points) + "/" + str(ques))
print("Thanks for playing!")
                    
