#list of dog breeds available for selection
DOG_BREEDS = ["Labrador", "German Shepherd", "Beagle", "Bulldog", "Poodle"]
#maximum dog age (15 years)
MAX_AGE = 15

#defines function for greeting the user and presenting information about the dog breeds, which can be used elsewhere
def greeting():
    print("Welcome to the Dog Breed Selector!")
    while True:
        #gets the user's name, removes spaces, capitilises the first letter and makes all others lowercase
        name = input("What is your first name? (remove any hyphens or spaces present) ").strip().title()
        #makes sure if the input is only comprised of letters from the alphabet
        if name.isalpha():
            break
        else:
            print("Please enter a valid name following the set specifications") #prints this and repeats the input for the user if it is not within the range
    #prints each breed in the DOG_BREEDS list and a number that goes before it (e.g., 1. Labrador)
    bullet_point = 1
    for breed in DOG_BREEDS: 
        print(f"{bullet_point}. {breed}")
        bullet_point += 1 #adds one to the numbered list and redefines it as this larger value. This adds one to the number on the left as the dog breeds are listed (e.g., 1. Labrador, 2. German Shepherd)
    return name

#defines function for finding the user's preffered dog breed
def pref_breed():
    while True:
        try:
            #gets preffered dog breed
            pref_breed_num = int(input("Enter the number of your preferred breed: "))
            #makes sure that the integer inputed is within the range of DOG_BREEDS (in this case 1 - 5)
            if 1 <= pref_breed_num <= len(DOG_BREEDS): #len finds the amount of items in the list, acting as the maximum number that can be inputted before it goes over the dog breeds
                return pref_breed_num
            else:
                print("Ensure that this number is from 1 to 5") #prints this and repeats the input for the user if it is not within the range
        except ValueError:
            print("Please enter a valid number") #prints this if the input is not an integer

#defines function for finding the user's preffered dog age
def pref_age():
    while True:
        try:
            #gets preffered age
            pref_age_num = int(input("Enter preferred age of dog (1 - 15): "))
            #makes sure if the user's input fits in the age range (1 - 15)
            if 1 <= pref_age_num <= MAX_AGE:
                return pref_age_num
            else:
                print("Ensure this age is within the range of 1 to 15")
        except ValueError:
            print("Please enter a valid number")

#main function that runs all other functions for the program and dismisses the user
def main():
    name_final = greeting() #gets user name
    pref_breed_final = pref_breed() #gets preferred breed
    pref_age_final = pref_age() #gets preffered age
    #ends the program with a goodbye message that recites user preferences back to the user
    print(f"\nThank you, {name_final}!\nYou prefer a {DOG_BREEDS[pref_breed_final - 1]} that is about {pref_age_final} years old.\nGood luck finding your perfect furry friend!")

#standard Python entry point for running the program
if __name__ == "__main__":
    main()