# Guess-the-Number-using-Binary-Search

A simple Python number guessing game where the computer guesses your number using an efficient algorithm called Binary Search.

You think of a number, and the computer tries to guess it in as few attempts as possible!

---

 How the Game Works

1. You think of a number between 1 and 100 (you can change this range).


2. The computer makes a guess.


3. You tell the computer whether the guess is:

Too high → h

Too low → l

Correct → c



4. Based on your feedback, the computer narrows down the range and guesses again.


5. The game ends when the computer guesses correctly and shows the number of attempts.




---

 Features

Computer guesses intelligently using Binary Search

Very fast (max ~7 guesses for numbers 1–100)

Counts the number of attempts

Beginner-friendly Python code



---

 Algorithm Used

Binary Search

Instead of guessing randomly, the computer always guesses the middle of the current range, then eliminates half of the remaining possibilities each time.

This makes the game efficient and fast.
