# Write your code below this line 👇
def prime_checker(number):
  is_prime = True

  for index in range(2, number): # 2 is the first prime number
    if number % index == 0: # So, we can assume that if the number is divisible by any number between 2 and the number itself, it's not a prime number
      is_prime = False

  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)