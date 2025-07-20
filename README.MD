A simple command-line Hangman game implemented in Python. This game selects a random word from a predefined list, and the player attempts to guess the word one letter at a time.

Features ✨
Random word selection from a predefined list

Input validation for guesses

Tracks correct and incorrect guesses

Displays current progress of the word

Game ends on win or after 6 incorrect guesses

How to Run ▶️
Ensure you have Python 3 installed on your system.

Save the game code in a file named hangman.py.

Open your terminal or command prompt.

Navigate to the directory containing hangman.py.

Run the script using:

bash
కాపీ చేయి
సవరించు
python hangman.py
Sample Word List 🧠
python
కాపీ చేయి
సవరించు
word_list = ['apple', 'chair', 'house', 'zebra', 'robot']
Feel free to customize this list with more words as you like!

Game Screenshot 📸
less
కాపీ చేయి
సవరించు
🎮 Welcome to Hangman!
Guess the word, one letter at a time.
You have 6 incorrect guesses. Good luck!

Word: _ _ _ _ _
Guessed letters:
Enter a letter: a
✅ Good guess!
Word: a _ _ _ _
Guessed letters: a
Enter a letter:
To-Do / Improvements 📌
Add difficulty levels

Use a larger dictionary file

Add ASCII art for the hangman figure

Develop a web or GUI version using Tkinter or Flask