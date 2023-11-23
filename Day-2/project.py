# Tip Calculator

"""Instructions
  If the bill was $150.00, split between 5 people, with 12% tip.
  Each person should pay (150.00 / 5) * 1.12 = 33.6
  Format the result to 2 decimal places = 33.60
  Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
  
  Hint
  1. Try to find out the data type of the result of the input function.
  2. Google how to convert a string into a float.
  3. Experiment with different ways of rounding.
"""

# Solution
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

tip = bill * (tip_percentage / 100)
bill += tip
bill_per_person = bill / number_of_people

print(f"Each person should pay: ${bill_per_person:.2f}")