import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
display = []
lives = 6
stages = stages

print(logo)

for letter in chosen_word:
  display.append("_")

while "_" in display:
  guess = input("Guess a letter: ").lower()
  
  if guess in display:
    print(f"You've already guessed {guess}.")
  
  else:
    for position in range(len(chosen_word)):
      letter = chosen_word[position] # We can assume that the letter is in the word.
      
      if letter == guess: # Then, we check if the letter is the same as the guess.
        display[position] = letter # If it is, we replace the underscore with the letter.
    
    if guess not in chosen_word: # Here's the logic when user guesses wrong.
      lives -= 1
      print(f"\nYou guessed {guess}, that's not in the word. You lose a life. \n")
    
      if lives == 0:
        print("You lose.")
        break

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
  print(f"\nYou have {lives} lives left.")
  print(stages[-lives - 1])
  
if "_" not in display:
  print("You win.")    