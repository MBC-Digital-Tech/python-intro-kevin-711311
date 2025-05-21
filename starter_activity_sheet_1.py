# starter program lesson 1

# change to your name.
name = input("What is your name? ")
breakfast = input("What did you have for breakfast? ")
colour = input("What is your favourite colour? ")
breakfast_lower = breakfast.lower()
colour_lower = colour.lower()
print()
print(f"I like {breakfast_lower} and the colour {colour_lower} too!")
print()
print("We want to know if you like progamming!")
# combine the next 2 lines into one commeand
answer = input(f"Do you like programming {name}? ")

# change to an f string
print()
print(f"Great! You said {answer}!")
print("Let's learn some Python today.")