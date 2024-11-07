import random
import string

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    with open("words.txt", 'r') as inFile:
        line = inFile.readline()
        wordlist = line.split()
    print(f"{len(wordlist)} words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist: list of words (strings)
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, the guessed word with underscores for unguessed letters
    """
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_ "
    return guessed_word

def get_available_letters(letters_guessed):
    """
    letters_guessed: list, what letters have been guessed so far
    returns: string, available letters that haven't been guessed
    """
    available_letters = string.ascii_lowercase
    return ''.join([letter for letter in available_letters if letter not in letters_guessed])

def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    """
    guesses_remaining = 8
    letters_guessed = []
    
    print("Welcome to the game, Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    while guesses_remaining > 0:
        print("-------------")
        print(f"You have {guesses_remaining} guesses left.")
        print("Available letters: ", get_available_letters(letters_guessed))
        
        guess = input("Please guess a letter: ").lower()
        
        if guess in letters_guessed:
            print("Oops! You've already guessed that letter: ", get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            guesses_remaining -= 1
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
        
        if "_" not in get_guessed_word(secret_word, letters_guessed):
            print("-------------")
            print("Congratulations, you won!")
            return
    
    print("-------------")
    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

if __name__ == "__main__":
    wordlist = load_words()
    secret_word = choose_word(wordlist).lower()
    hangman(secret_word)
