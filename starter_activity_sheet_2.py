# starter program week 2 - perhaps this could be a task

def conversation(): #defines a function called conversation
    print("Welcome to my conversation program")
    print()

    # combine the next two lines into one command.
    sport1 = input("Do you like cycling? Answer yes or no ") #asks the user a question and lets them input an answer
    sport1_lower = sport1.lower() #turns the users answer into all lowercases so that it can be used in an if == statement

    # chenge this so that the user can enter YES as well.
    if sport1_lower == "yes": #if the variable is exactly equal to yes, then print out this response
        print("That's good - you will get very fit")
    else: #otherwise, print this out
        print("Perhaps you like some other sport. ")
    print()
    sport2 = input("Do you like target shooting? ")
    sport2_lower = sport2.lower()
    if sport2_lower == "yes":
        print("I like target shooting too! It is my favourite sport.")
    else:
        print("A lot of people don't remember it as a sport so I can't blame you.")
    print()
    sport3 = input("Do you like badminton? ")
    sport3_lower = sport3.lower()
    if sport3_lower == "yes":
        print("Badminton is very fun aswell!")
    else:
        print("You should try it some time.")
    print()
    print("Goodbye")

# Add command here to run the function
conversation() #calls the function
print()
def cities():
    answer2 = int(input("How many cities are there in England? ")) #like input but instead of remembering strings it remembers integers
    if answer2 == 51:
        print("Correct!")
    else:
        print("That is incorrect. Better luck next time!")

cities()
print()
def grade():
    greater_than = int(input("Please input a number greater than 10: "))
    if greater_than > 10: #instead of finding if an input is directly equal to something, this finds if it is greater than something
        print("Great! Lets move onto the next question")
    else:
        print("That number was not greater than 10, or wasn't even a number at all. Moving on...")
    print()
    score = int(input("What score did you get in the test? (e.g., 86, 99, 32) "))
    if score < 50: #sees if input is less than something
        print("It seems you have failed the test. Try harder and next time you will succeed!")
    else:
        print("Congratulations! You have passed the test.")
    print()
    age = int(input("What is your age? "))
    if age >= 13: #sees if input is greater or equal to something
        print("You can have a paper round.")
    else:
        print("You cannot have a paper round.")
    print()  
    secret_number = int(input("Finally, enter a number: "))
    if secret_number != 99: #sees if input does not equal something
        print("You have passed the test.")
    else:
        print("You have entered the wrong number. You are either very unlucky or a cheater. Goodbye!")
        exit()
    
grade()