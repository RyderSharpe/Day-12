import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
           40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
           60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
           80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

number = random.choice(numbers)

# Introduction to the game text
print("Welcome to the Number Guessing Game!")
# play = True
# while play:


print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {number}")
def easy():

    print("Easy mode selected. You have 10 guesses.")
    for i in range (10):
        guess = int(input("Make a guess: "))
        if guess == number:
            print("you won")
            break
        else:
            print(f"incorrect you have {9 - i} guesses left")
            if i == 9:
                print("you lost")
                play_again = input("Do you want to play again? Type 'yes' or 'no': ")
                if play_again == "yes":
                    play = True

                else:
                    play = False


    def hard():
         print("Hard mode selected. You have 5 guesses.")


# Difficulty selection
repeat = True
while repeat:

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        easy()
        repeat = False
    elif difficulty == "hard":
        hard()
        repeat = False
    else:
        print("Invalid input. Please choose 'easy' or 'hard'.")



