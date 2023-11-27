# Lists

states_of_indonesia = ["Jakarta", "Bali", "Aceh", "Papua", "Sulawesi", "Kalimantan", "Sumatera", "Jawa"] # Here's how you make a list. We use square brackets to make a list.

print(states_of_indonesia) # This will print the whole list.
print(states_of_indonesia[0]) # This will print the first item in the list. Remember that the first item in a list is at index 0.
print(states_of_indonesia[-1]) # This will print the last item in the list. Remember that the last item in a list is at index -1.

states_of_indonesia[0] = "Jakarta Special Capital Region" # This will change the first item in the list to "Jakarta Special Capital Region".
states_of_indonesia.append("Maluku") # This will add "Maluku" to the end of the list.
states_of_indonesia.extend(["Riau", "Lampung"]) # This will add "Riau" and "Lampung" to the end of the list.

fruits = ["Apple", "Orange", "Pear"]
vegetables = ["Carrot", "Tomato", "Broccoli"]

dirty_dozen = [fruits, vegetables] # This will make a list of lists (nested lists).
