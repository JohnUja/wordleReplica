import random
from termcolor import colored

print ("*-------------------Rules-----------------*")
print("You have 6 tries to guess a correct word")
print("Green letter  in word ie Hu" + colored('n', 'green') + "ts signifies a correct guess and positioning")
print("Yellow letter  in word ie M" + colored('u', 'yellow') + "sic signifies a correct guess and wrong positioning")
print("Red letter  in word ie o" + colored('c', 'red') + "ean signifies a wrong guess ")

def start_game():
    words = [
        "Apple", "Books", "Cream", "Dirty", "Eager", "Funds", "Froze", "Galop", "Green", "World",
        "Laugh", "Mirth", "Quick", "Brown", "Jumpy", "Zebra", "Table", "Chair", "Bread", "House",
        "Shine", "Sweet", "Short", "Heart", "Field", "Smile", "Bells", "Burst", "Candy", "Music",
        "Storm", "Beast", "Scare", "Brick", "Watch", "Flame", "Solar", "Cloud", "Space", "River",
        "Ghost", "Angel", "Sound", "Flash", "Toast", "Proud", "Honor", "Faith", "Round", "Pixel",
        "River", "Ghost", "Angel", "Sound", "Flash", "Toast", "Proud", "Honor", "Faith", "Round",
        "Pixel", "Juice", "Blank", "Brave", "Chase", "Crown", "Fresh", "Fruit", "Grain", "Hobby",
        "Honey", "Ivory", "Joint", "Lemon", "Maple", "Noble", "Onion", "Panda", "Quilt", "Razor",
        "Salad", "Shark", "Sunny", "Teeth", "Trust", "Unzip", "Vapor", "Whale", "Xerox", "Youth",
        "Zebra", "Civic", "Daisy", "Elbow", "Funky", "Globe", "Humor", "Igloo", "Joker", "Koala",
        "Llama", "Movie", "Ninja", "Opera", "Pizza", "Queen", "Robot", "Sofas", "Tiger", "Unify",
        "Vixen", "Witch", "Xylo", "Yacht", "Zeal"
    ]

    generatedword = random.choice(words).lower()
    generatedwordcopy = list(generatedword)
    tries = 6

    while tries > 0:
        userinput = input("Enter your word guess. You have " + str(tries) + " guesses remaining: ").lower()

        if not userinput.isalpha():
            print("Please enter a string")
            continue

        if len(userinput) != 5:
            print("Please enter a 5-letter word")
            continue

        tries -= 1

        # Convert word to array first
        userinput_arr = list(userinput)

        # Initialize a return array of len 5
        feedback = [""] * 5

        # Create a copy of the generated word to avoid counting a character twice
        temp_generatedwordcopy = list(generatedwordcopy)

        # Loop through user input
        for i in range(0, len(userinput_arr)):
            # Check user input for matching letter in the correct index position
            if userinput_arr[i] == temp_generatedwordcopy[i]:
                feedback[i] = colored(userinput_arr[i], 'green')
                temp_generatedwordcopy[i] = '*' # replace with * to avoid counting again
            elif userinput_arr[i] in temp_generatedwordcopy:
                feedback[i] = colored(userinput_arr[i], 'yellow')
                temp_generatedwordcopy[temp_generatedwordcopy.index(userinput_arr[i])] = '*' # replace with * to avoid counting again
            elif userinput_arr[i] not in temp_generatedwordcopy:
                feedback[i] = colored(userinput_arr[i], 'red')

        # Join the string to recreate the word
        feedbackstring = ''.join(feedback)

        # Checks that for all letters in userinput, when colored green, are present in the feedback list.
        if all(colored(letter, 'green') in feedback for letter in userinput):
            print("You have guessed the correct word in " + str(6-tries) + " tries. Congratulations!")
            print(feedbackstring)
            print("Click 'R' to play again.")
            break

        print(feedbackstring)

    print("Gameover" + " The correct word was " + generatedword)

# Call the startGame() function to begin the game
start_game()
