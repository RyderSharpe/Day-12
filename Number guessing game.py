import random

numbers = list(range(1, 101))
number = random.choice(numbers)

play = True
while play:

    def play_game():
        global play

        # Introduction to the game text
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print(f"Pssst, the correct answer is {number}")
        def easy():
            global play
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
                        if play_again.lower() == "yes":
                            play = True
                        else:
                            play = False
        def hard():
             global play
             print("Hard mode selected. You have 5 guesses.")
             for i in range (5):
                 guess = int(input("Make a guess: "))
                 if guess == number:
                     print("you won")
                     break
                 else:
                     print(f"incorrect you have {4 - i} guesses left")
                     if i == 4:
                         print("you lost")
                         play_again = input("Do you want to play again? Type 'yes' or 'no': ")
                         if play_again.lower() == "yes":
                             play = True
                         else:
                             play = False

        # Difficulty selection
        repeat = True
        while repeat:

            difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

            if difficulty.lower() == "easy":
                easy()
                repeat = False
            elif difficulty.lower() == "hard":
                hard()
                repeat = False
            else:
                print("Invalid input. Please choose 'easy' or 'hard'.")


    play_game()