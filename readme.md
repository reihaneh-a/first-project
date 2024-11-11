# Number Guessing Game

This is a simple Python console game where the user has to guess a random number between 1 and 100. The program will provide feedback to help the user guess correctly within a limited number of attempts.

## How It Works

1. The program generates a random number between 1 and 100.
2. The user has up to 6 attempts to guess the correct number.
3. For each incorrect guess, the program provides feedback:
   - If the guess is too low, it displays "low number from guess number."
   - If the guess is too high, it displays "high number from guess number."
4. If the user guesses correctly, a congratulatory message is displayed along with the number of attempts taken.
5. If the user doesn't guess correctly within the 6 attempts, the correct answer is revealed.

## Getting Started

### Prerequisites
- Python 3

### Running the Program
1. Clone this repository.
2. Run `guessNumber.py` in a terminal:
   ```bash
   python guessNumber.py
