alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  result = ""
  
  for letter in text:
    position = alphabet.index(letter)
    
    if direction == "encode":
      new_position = position + shift
    elif direction == "decode":
      new_position = position - shift
      
    if new_position > 25:
      new_position -= 26 # 26 is the length of the alphabet. So, if the new_position is greater than 25, we need to subtract 26 to get the correct position
    elif new_position < 0:
      new_position += 26 # 26 is the length of the alphabet. So, if the new_position is less than 0, we need to add 26 to get the correct position
    
    new_letter = alphabet[new_position]
    result += new_letter
  
  print(f"The {direction}d text is {result}")