#Asking user's info, convert number answers to floats / int
name = input("What is your name? ")
destination = input("What is your destination? ")
distance = float(input("What is the one way distance in miles? "))
MPG = float(input("What is your vehicle's MPG? "))
PPG = float(input("What is the gas price per gallon? "))
amount_of_people = int(input("How many travellers? "))
#Calculations, unprinted
total_miles = (2 * distance)
gallons_gas_needed = (distance/MPG)
Gas_cost_approx = (gallons_gas_needed*PPG)
Approx_cost_per_traveller = (Gas_cost_approx/amount_of_people)
#Printing a readable trip summary, convert floats / int back to string in order to print?
print("road trip planner".upper())
print(name)
print("The road to " + destination.upper())
print(f"Estimated Cost: {Gas_cost_approx} dollars")
print(f"Approximate cost per person: {Approx_cost_per_traveller} dollars")