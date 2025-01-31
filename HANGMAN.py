"""
This is a simple Hangman game with a graphical user interface (GUI) built using Tkinter. The game allows the user to guess letters in a randomly chosen word, with the goal of guessing the word within a limited number of attempts.

### Key Features:
1. **Word Selection**: The program randomly selects a word from a predefined list of words.
2. **Difficulty Levels**: The user can choose from three difficulty levels: Easy, Medium, and Hard. Each level adjusts the number of attempts allowed.
3. **Guessing**: The player guesses one letter at a time. The program updates the word with the guessed letter if it’s correct, and decreases the number of attempts if it’s wrong.
4. **Hints**: The user can ask for a hint, which reveals one letter of the word. Hints cost one attempt.
5. **Game Over**: The game ends when the player either guesses the word or runs out of attempts. A message is displayed with the result.
6. **Visuals**: The game interface has a cute, soft pink theme with smooth hover effects for buttons and user-friendly fonts.

### Game Flow:
1. The user starts by choosing a difficulty level and clicking "Start Game."
2. The game begins, showing a word with underscores for unguessed letters.
3. The user submits guesses, and the program updates the word and the number of attempts remaining.
4. The game ends when the word is guessed or the user runs out of attempts.
"""

import random
import tkinter as tk
from tkinter import messagebox

def hangman():
    words = ["python", "programming", "hangman", "challenge", "developer"]
    word = random.choice(words)
    guessed_word = ["_" for _ in word]
    guessed_letters = []
    attempts = 6  # Max attempts for the game

    def start_game():
        nonlocal attempts
        difficulty = difficulty_var.get()

        # Set attempts based on difficulty
        if difficulty == "Easy":
            attempts = 10
        elif difficulty == "Medium":
            attempts = 7
        else:
            attempts = 5

        update_status()

    def update_status():
        # Update the word, guessed letters, and attempts
        word_label.config(text="Word: " + " ".join(guessed_word))
        guessed_label.config(text=f"Guessed letters: {', '.join(guessed_letters)}")
        attempts_label.config(text=f"Attempts remaining: {attempts}")

    def make_guess():
        nonlocal attempts
        guess = guess_entry.get().lower()
        guess_entry.delete(0, tk.END)

        if guess == "hint":
            if attempts > 1:
                hint_letter = random.choice([letter for letter in word if letter not in guessed_letters])
                messagebox.showinfo("Hint", f"The word contains the letter '{hint_letter}'.")
                attempts -= 1
                update_status()
            else:
                messagebox.showwarning("No Attempts Left", "Not enough attempts left for a hint.")
            return

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single valid letter.")
            return

        if guess in guessed_letters:
            messagebox.showwarning("Already Guessed", "You already guessed that letter.")
            return

        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
            if "_" not in guessed_word:
                messagebox.showinfo("Congratulations!", f"🎉 You guessed the word: {word}! 🎉")
                root.quit()
        else:
            attempts -= 1
            if attempts == 0:
                messagebox.showinfo("Game Over", f"😢 You ran out of attempts! The word was: {word}.")
                root.quit()

        update_status()

    # GUI Setup
    root = tk.Tk()
    root.title("Hangman Game")
    root.geometry("600x700")
    root.configure(bg="#F8BBD0")  # Soft pink background

    # Title Label with cute font
    title_label = tk.Label(root, text="Hangman Game", font=("Poppins", 30, "bold"), bg="#F8BBD0", fg="#D81B60")
    title_label.pack(pady=40)

    # Difficulty Selection
    difficulty_var = tk.StringVar(value="Medium")
    tk.Label(root, text="Choose Difficulty:", font=("Poppins", 16), bg="#F8BBD0", fg="#D81B60").pack()
    tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard").pack(pady=10)

    # Start Game Button with smooth hover effect
    start_button = tk.Button(root, text="Start Game", command=start_game, font=("Poppins", 16), bg="#D81B60", fg="white", relief="raised", width=15, height=2)
    start_button.pack(pady=30)

    # Word and Attempts Display with more elegant font
    word_label = tk.Label(root, text="Word: " + " ".join(guessed_word), font=("Poppins", 22), bg="#F8BBD0", fg="#D81B60")
    word_label.pack(pady=20)

    attempts_label = tk.Label(root, text=f"Attempts remaining: {attempts}", font=("Poppins", 16), bg="#F8BBD0", fg="#D81B60")
    attempts_label.pack(pady=5)

    guessed_label = tk.Label(root, text=f"Guessed letters: {', '.join(guessed_letters)}", font=("Poppins", 16), bg="#F8BBD0", fg="#D81B60")
    guessed_label.pack(pady=10)

    # User Guess Entry with a girly touch
    tk.Label(root, text="Enter your guess:", font=("Poppins", 16), bg="#F8BBD0", fg="#D81B60").pack(pady=10)
    guess_entry = tk.Entry(root, font=("Poppins", 16), width=10, justify="center", bd=2)
    guess_entry.pack()

    # Submit Guess Button with smooth hover effect
    def on_hover_in(event):
        event.widget.config(bg="#C2185B", fg="white")

    def on_hover_out(event):
        event.widget.config(bg="#D81B60", fg="white")

    guess_button = tk.Button(root, text="Submit Guess", command=make_guess, font=("Poppins", 16), bg="#D81B60", fg="white", relief="raised", width=15, height=2)
    guess_button.bind("<Enter>", on_hover_in)
    guess_button.bind("<Leave>", on_hover_out)
    guess_button.pack(pady=30)

    # Start the game
    root.mainloop()

# Start the game
hangman()

