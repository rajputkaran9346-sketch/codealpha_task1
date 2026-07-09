import random

# List of words
words = ["python", "computer", "keyboard", "monitor", "program", "hangman"]

# Choose a random word
word = random.choice(words)

# Create a list of underscores
guessed_word = []
for letter in word:
    guessed_word.append("_")

# Store guessed letters
guessed_letters = []

# Number of chances
chances = 6

print("===== WELCOME TO HANGMAN GAME =====")

while chances > 0:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", guessed_letters)
    print("Chances Left:", chances)

    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1:
        print("Please enter only one letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)

        # Check if letter is in the word
        if guess in word:
            print("Correct Guess!")

            # Reveal the letter
            i = 0
            while i < len(word):
                if word[i] == guess:
                    guessed_word[i] = guess
                i += 1

        else:
            print("Wrong Guess!")
            chances -= 1

    # Check if player has won
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
        break

# If player loses
if "_" in guessed_word:
    print("\nGame Over!")
print("The correct word was:", word)