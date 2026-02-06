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

def Main():
    print("Worlde Test Project")
    words = load_word_bank(word_file)
    sample = random.choice(words)
    
    print(f"First Sample test: {sample}")
        
    
if __name__ == "__main__":
    Main()
