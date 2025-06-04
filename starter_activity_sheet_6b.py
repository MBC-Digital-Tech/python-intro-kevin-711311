def exercise1():
    number = 0
    while number < 100:
        print("Today is Monday")
        number = number + 1

def exercise2():
    storm = input("What is the name of the recent storm? ")
    while storm != "Doris":
        storm = input("Incorrect storm name. Please try again: ")
    
    print("That is the right storm name")

def exercise3():
    nine_nine = int(input("Enter a number... "))
    while nine_nine != 99:
        nine_nine = int(input("Enter a number... "))

def bored():
    bored = input("Are you bored yet? ")
    while bored != "y":
        bored = input("Are you bored yet? ")

    print("Got to you in the end!!")

def exercise5():
    num = 1
    while num <= 10:
        print(num)
        num += 1

def exercise6():
    num = 10
    while num >= 1:
        print(num)
        num -= 1

def logging_in():
    count = 0
    password = input("Enter your password: ")
    while password != "secret":
        print("That password is not the one stored\nTry again!")
        count += 1
        password = input()
    print("Yes that's the correct password!")
    print(f"You inputted the wrong password {count} times")

#def england_quiz():

def england_quiz():
    print("How many cities are there in England")
    answer = int(input())
    while answer != 51:
        print("No, that's not correct\nTry again!")
        answer = int(input())
    print("That's correct!")

def my_quiz():
        print("What is the capital of New Zealand?")
        print("a. Christchurch\nb. Auckland\nc. Wellington")
        question1 = input("Answer: ").lower()
        while question1 != "c":
            print("Incorrect. Try Again!")
            question1 = input()
        print("Correct!")

function = input("What exercise do you want to see? (exercise1/exercise2/exercise3/bored/exercise5/exercise6/logging in/england quiz/my quiz) ").strip().lower()
if function == "exercise1":
    exercise1()
elif function == "exercise2":
    exercise2()
elif function == "exercise3":
    exercise3()
elif function == "bored":
    bored()
elif function == "exercise5":
    exercise5()
elif function == "exercise6":
    exercise6()
elif function == "logging in":
    logging_in()
elif function == "england quiz":
    england_quiz()
elif function == "my quiz":
    my_quiz()
else:
    print("This input is not on the drawing list!")