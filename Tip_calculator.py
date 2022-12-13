print("Welcome to the tip calculator")
total_bill = float(input("what was the total bill? $"))
tip_to_give = int(input("what percentage tip would you like to give? 10, 12, or 15?"))
total_people = int(input("how many people to split the bill? "))

total_amount = total_bill + (total_bill * (tip_to_give / 100))

amount_to_pay = round(total_amount / total_people, 2)

print(f"Each person should pay: ${amount_to_pay}")


