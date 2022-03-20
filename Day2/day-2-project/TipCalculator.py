print("Welcome to Tip Calculator.")

total_bill = float(input("What was the Total Bill ? $"))

percentage_to_pay = int(
    input("what percentage tip would you like to give? 10, 12 or 15 ?"))

percentage = (total_bill * percentage_to_pay)/100

number_of_people = int(input("How many people to split the bill?"))

pay = ((total_bill + (percentage)) / number_of_people)

print(f"Each person should Pay : ${pay}")
