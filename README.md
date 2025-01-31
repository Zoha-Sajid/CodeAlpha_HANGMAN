# **Hangman Game** 🎮🎀

## **Overview**
This is a cute and interactive **Hangman** game built using Python's **Tkinter** for the graphical user interface (GUI). The game allows players to guess a word by submitting one letter at a time. The player can also ask for hints, and the game offers three difficulty levels: Easy, Medium, and Hard. The game ends when the word is guessed correctly or the player runs out of attempts. 

## **Key Features**
1. **Word Selection**: A random word is chosen from a predefined list of words.
2. **Difficulty Levels**: The user can select from three difficulty levels: Easy, Medium, and Hard. Each level adjusts the number of allowed attempts:
   - **Easy**: 10 attempts
   - **Medium**: 7 attempts
   - **Hard**: 5 attempts
3. **Guessing**: Players can guess one letter at a time. If the guess is correct, the word is updated, and if it's wrong, the number of attempts decreases.
4. **Hints**: The user can ask for a hint (which reveals one letter), but it costs one attempt.
5. **Game Over**: The game ends when the player either guesses the word or runs out of attempts. 
6. **Visuals**: The game features a soft pink theme with smooth hover effects for buttons and user-friendly fonts, giving it a cute touch. 💖

## **Game Flow**
1. **Choose Difficulty**: The player selects a difficulty level (Easy, Medium, or Hard).
2. **Start Game**: The game starts, and the word is displayed as a series of underscores.
3. **Make Guesses**: The player enters guesses, and the game updates the word and the remaining attempts.
4. **End Game**: The game ends when the word is guessed correctly or when the player runs out of attempts.

## **Installation Instructions**
1. **Python 3.x**: Ensure you have Python 3.x installed on your system.
2. **Tkinter**: Tkinter is included by default in most Python installations. If it's missing, install it using:
   ```bash
   sudo apt-get install python3-tk
   ```
3. **Clone the Repository**: If this is a GitHub repository, clone it to your local machine:
   ```bash
   git clone <repository-url>
   ```

4. **Run the Program**: Navigate to the directory where the script is located and run the program using:
   ```bash
   python hangman_game.py
   ```

## **Gameplay Instructions**
1. **Start the Game**: Select a difficulty level and click **Start Game**.
2. **Guessing**: Enter a single letter in the input field and click **Submit Guess**.
   - If the guess is correct, the corresponding letter will appear in the word.
   - If the guess is wrong, your attempts will decrease.
3. **Hints**: Type "hint" to receive a letter hint (costs one attempt).
4. **End Game**: The game will end when you either guess the word or run out of attempts. 

## **Example Gameplay**
- **Choose Difficulty**: Medium
- **Word**: `__ __ __ __ __` (5-letter word)
- **Guesses**:
  - **You**: "e"
  - **Bot**: "Word: _ _ e _ _"
  - **You**: "t"
  - **Bot**: "Word: t _ e _ _"
  - **You**: "h"
  - **Bot**: "Congratulations! You guessed the word: **there**!" 

## **Customization**
- **Change Word List**: Modify the list of words in the `words` variable to suit your preference.
- **Modify Appearance**: You can change the color scheme, fonts, or button styles for a more personalized look. 🎀
- **Difficulty Levels**: Adjust the number of attempts for each difficulty level by modifying the conditions in the `start_game` function.
  
----------------------------------------------------------------------------------------------------------------------------------------------------------------

## **License**
This project is open-source and free to use. Feel free to contribute and customize the game as per your liking. 🎀💖

 
