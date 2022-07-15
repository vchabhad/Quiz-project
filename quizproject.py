import json
import random

with open("questions.json","r+") as file:
    questions=json.load(file)




def verify_ans(questionid, ans, score):

    if questions[questionid]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"!!!Wrong Answer!!!\nTry again...")
        return False



def welcomescreen():

    print("\t*****Welcome to the Quiz*****")
    print("\tThere we will have 5 Questions picked randomly from a file with bunch of questions, To skip a question reply  'skip'")
    input("Press Enter to start Quiz => ")
    return True

intro = welcomescreen()
count=1
score=0
while count<6 :


    questionid=random.choice(list(questions))
    print("Question No:",count)
    print("\n",questions[str(questionid)]['question'])
    answer = input("Enter Answer => ")
    check = verify_ans(str(questionid), answer, score)
    if check:
        score += 1
    count+=1

    
print(f"Your final score is {score}!\n\n")
print("Thanks for playing! Come back again...")