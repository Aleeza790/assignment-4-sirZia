import random
from words import words

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set() 

    lives = 6

    print("Welcome to Hangman!")

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left. You used these letters:", ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct!")
            else:
                lives -= 1
                print("Wrong!")
        elif user_letter in used_letters:
            print("You already used that letter.")
        else:
            print("Invalid input.")

    if lives == 0:
        print("\nYou lost. The word was:", word)
    else:
        print("\nYay! You guessed the word:", word)

if __name__ == "__main__":
    hangman()