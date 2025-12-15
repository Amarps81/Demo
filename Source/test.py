#!/usr/bin/env python3
"""
guess_number.py

Interactive program where the computer guesses a number you chose from 0-99.
Reply to each guess with one of:
  - "higher"  (your number is higher than the guess)
  - "lower"   (your number is lower than the guess)
  - "correct" (the guess is correct)

Accepted short inputs: h, l, c (case-insensitive).
"""

def get_response(prompt: str) -> str:
    while True:
        resp = input(prompt).strip().lower()
        if not resp:
            continue
        if resp[0] in ("h", "l", "c"):
            return resp[0]  # 'h', 'l', or 'c'
        print("Please answer 'higher', 'lower', or 'correct' (or h/l/c).")

def main():
    print("Think of a number from 0 to 99 (inclusive). I will try to guess it.")
    low, high = 0, 99
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        resp = get_response(f"Is your number {guess}? (higher / lower / correct): ")

        if resp == "c":
            print(f"I've got it! Your number is {guess}. Guessed in {attempts} attempts.")
            return
        elif resp == "h":
            # your number is higher than guess
            low = guess + 1
        elif resp == "l":
            # your number is lower than guess
            high = guess - 1

    # If we exit the loop, the user's answers were inconsistent
    print("There seems to be a contradiction in the answers. Are you sure you answered consistently?")

if __name__ == "__main__":
    main()
