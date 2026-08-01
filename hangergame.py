import random


word_bank = ["python", "programming", "developer", "computer", "algorithm", "jupyter"]

secret_word = random.choice(word_bank)


display_word = ["_"] * len(secret_word)


attempts_left = 6
guessed_letters = []  

print("--- Welcome to Python Hangman! ---")


while attempts_left > 0 and "_" in display_word:
    
    print("\nWord to guess: " + " ".join(display_word))
    print(f"Attempts remaining: {attempts_left}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    
    
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter exactly one alphabetical letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter. Try a different one!")
        continue
        
    guessed_letters.append(guess)
    
    if guess in secret_word:
        print(f"Good job! '{guess}' is in the word.")
        
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                display_word[index] = guess  
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        attempts_left -= 1  

if "_" not in display_word:
    print("\n🎉 Congratulations! You won!")
    print(f"The word was: {secret_word}")
else:
    print("\n💀 Game Over! You ran out of attempts.")
    print(f"The correct word was: {secret_word}")
