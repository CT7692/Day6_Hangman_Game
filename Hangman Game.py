
import secrets

word_list = ["aardvark", "baboon", "camel"]

phase1 = '''+---+
  |   |
      |
      |
      |
      |
========='''

phase2 = '''+---+
  |   |
  O   |
      |
      |
      |
========='''

phase3 = '''+---+
  |   |
  O   |
  |   |
      |
      |
========='''

phase4 = '''+---+
  |   |
  O   |
 /|   |
      |
      |
========='''

phase5 = '''+---+
  |   |
  O   |
 /|\  |
      |
      |
========='''

phase6 = '''+---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''

you_lose = ''' +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''

phase_list = [phase1, phase2, phase3, phase4, phase5, phase6, you_lose]
chosen_word = secrets.SystemRandom().choice(word_list)
letter_list = list(chosen_word)

hidden_list = []
wrong_letters = []

for i in range(0, len(letter_list)):
  hidden_list.append('_')

phase_index = 0
phase = phase_list[phase_index]
game_finished = False

while game_finished == False:
  letter_found = False
  wrong_letter_found = False
  print(phase)
  print(hidden_list)
  print(f"Wrong letters: {wrong_letters}")
  guess_char = input("Guess a letter: ").lower()

  for i in range(0, len(letter_list)):
    if letter_list[i] == guess_char:
      hidden_list[i] = guess_char
      letter_found = True

  if len(wrong_letters) > 0:
    for i in range(0, len(wrong_letters)):
      if wrong_letters[i] == guess_char:
        wrong_letter_found = True
          
  if letter_found == True:
    print("\nYou guessed correctly.")
    if ''.join(hidden_list) == chosen_word:    
      game_finished = True
      print(f"\n\n{hidden_list}")
      print("YOU WIN!!! :D")    
  elif wrong_letter_found == True:
    print("\nYou already guessed this letter. Try again.")
  elif guess_char.isnumeric() or len(guess_char) > 1:
    print("\nInvalid input. Try again.")
  else:
    phase_index += 1
    phase = phase_list[phase_index]
    wrong_letters.append(guess_char)
    print(f"\nThe letter {guess_char} is not in the word.")
    if phase == you_lose:
      game_finished = True
      print(phase)
      print("\nYou lose. :(")
