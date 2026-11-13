#!/usr/bin/env python3
"""Number Guessing Game - guess the secret number between 1 and 100."""
import argparse, random

def play(secret, low=1, high=100):
    print(f"I'm thinking of a number between {low} and {high}. Try to guess it!")
    attempts = 0
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number."); continue
        except EOFError:
            print("\nGoodbye!"); return attempts
        attempts += 1
        if guess < secret: print("Too low! Try again.")
        elif guess > secret: print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempt(s)."); return attempts

def main():
    p = argparse.ArgumentParser(description="Number Guessing Game")
    p.add_argument("--low", type=int, default=1); p.add_argument("--high", type=int, default=100)
    p.add_argument("--secret", type=int, default=None, help="Fix the secret number (for testing)")
    args = p.parse_args()
    secret = args.secret if args.secret is not None else random.randint(args.low, args.high)
    play(secret, args.low, args.high)

if __name__ == "__main__":
    main()
