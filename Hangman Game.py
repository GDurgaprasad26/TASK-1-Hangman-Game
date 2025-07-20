import random

# Predefined list of words
word_list = ['apple', 'chair', 'house', 'zebra', 'robot']

# Select a random word from the list
secret_word = random.choice(word_list)

# Game state variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Create a display version of the word with underscores
display_word = ['_'] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses. Good luck!\n")

# Game loop
while wrong_guesses < max_wrong_guesses and '_' in display_word:
    print("Word:", ' '.join(display_word))
    print("Guessed letters:", ' '.join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    # Validate input
    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for idx, letter in enumerate(secret_word):
            if letter == guess:
                display_word[idx] = guess
    else:
        print("❌ Wrong guess!\n")
        wrong_guesses += 1

# Game result
if '_' not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)

