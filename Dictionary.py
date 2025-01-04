# dictionary
people_ages = {"Jyothi": 18, "Chandana": 24, "Anjali": 22, "Anusha": 15, "Priya": 23}

# The Counting  above the people age of 18
count_above_18 = sum(1 for age in people_ages.values() if age > 18)

# Printing the result
print(f"The number of people above the age of 18 is: {count_above_18}")
