# This program is a caesar cipher encoder/decoder
from art import logo
from project_business import caesar

print(logo)

continue_program = True

while continue_program:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26
  caesar(text, shift, direction)
  
  feedback = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  
  if feedback == "no":
    continue_program = False
    print("Goodbye!")