# starter program week 3 - perhaps this could be a task
def cooking():
    print("Meal planner")
    print()

    # change these to your favourite meals
    print("1. Grilled Cheese")
    print("2. Lambchops")
    print("3. Burger and fries")
    # add one more meal here
    print("4. Spaghetti bolognese")
    # adapt the next line to add in the 4.
    favourite = int(input("Which of these meals is your favourite? (1, 2, 3 or 4) "))
    # combine the line above and below into one command that accepts an integer instead of a string.

    # adapt the if else block to include the fourth meal and compares integers instead of strings.
    if favourite == 1:
        print("Grilled Cheese coming up!")
    elif favourite == 2:
        print("Lambchops coming up!")
    elif favourite == 3:
        print("Burger and fries coming up!")
    elif favourite == 4:
        print("Spaghetti bolognese coming up!")
    else:
        print("Sorry, but that is not an acceptable answer, which means I cannot take your order.")

    print("Enjoy!")
    
# add a command to run the function above.
cooking()

def quiz():
    score = 0

    print("\nWelcome To My New Zealand Geography Quiz!")
    print("I will present to you 5 questions. Each question will have 3 possible answers, but only 1 will be correct.")
    print("Respond to each question with either a, b or c")
    print()
    print("Without further ado, lets begin!")
    print()
    print("What is the capital of New Zealand?")
    print("a. Christchurch\nb. Auckland\nc. Wellington")
    question1 = input("Answer: ").lower()
    if question1 == "c":
        print("\nCorrect!")
        score = score + 1
    else:
        print("Incorrect. The answer is Wellington")
    print()
    print("What is the highest mountain in New Zealand?")
    print("a. Mount Taranaki\nb. Mount Cook\nc. Mount Ruapehu")
    question2 = input("Answer: ").lower()
    if question2 == "b":
        print("\nCorrect!")
        score = score + 1
    else:
        print("Incorrect. The answer is Mount Cook")
    print()
    print("What are the names of the two main islands of New Zealand?")
    print("a. Stewart Island and Chatham Island\nb. North Island and South Island\nc. Stewart Island and Waiheke Island")
    question3 = input("Answer: ").lower()
    if question3 == "b":
        print("\nCorrect!")
        score = score + 1
    else:
        print("Incorrect. The answer is North Island and South Island")
    print()
    print("What is the name of strait that seperates the North and South island?")
    print("a. Foveaux Strait\nb. Bass Strait\nc. Cook Strait")
    question4 = input("Answer: ").lower()
    if question4 == "c":
        print("\nCorrect!")
        score = score + 1
    else:
        print("Incorrect. The answerr is Cook Strait")
    print()
    print("What is the largest lake in New Zealand?")
    print("a. Lake Taupo\nb. Lake Wakatipu\nc. Lake Rotorua")
    question5 = input("Answer: ").lower()
    if question5 == "a":
        print("\nCorrect!")
        score = score + 1
    else:
        print("Incorrect. The answer is Lake Taupo")
    
    print(f"Your final score is {score}/5.")
    if score == 5:
        print("Amazing! You aced the test")
    elif score == 0:
        print("Better luck next time")
    else:
        print("Congratulations!")

quiz()