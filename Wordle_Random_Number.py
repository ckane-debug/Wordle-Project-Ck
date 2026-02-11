from pathlib import Path
import random

word_file = Path ("Words.txt")

def Find_Word_File():
    if word_file.exists():
        return word_file
    else:
        print("Didnt find")
    
def load_word_bank(filename = "Words.txt"):
    with open(filename, "r") as file:
        return [line.strip().lower() for line in file if len(line.strip()) == 5]

word_bank = load_word_bank()

def user_word():
    guess = input("Enter a 5 letter word").strip().lower()
    if (len(guess) != 5 ):
        print("Word must be 5 letters")
    elif (guess not in word_bank):
        print("Please submit a correctly spelled word")
    else:
        return guess
def Main():
    print("Worlde Test Project")
    words = load_word_bank(word_file)
    sample = random.choice(words)
    
    print(f"Debugging test: Selected word it {sample}")
    attempts = 0
    while attempts <= 6:
         guess = user_word(words)
         print(f"Your guess: {guess}")
         print(f"Comparing {guess} to {sample}")
         attempts += 1
         if sample == guess:
            print("Congratulations, u got it!")
         else:
             print(f"Your guess was {guess}, the word was {sample}, atmmepts {attempts}")
             
if __name__ == "__main__":
    Main()
