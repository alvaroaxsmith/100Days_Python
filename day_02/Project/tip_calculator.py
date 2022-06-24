#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill?")
total_bill = float(total_bill)
print(f"${total_bill}")
tip_gave = input("How much tip would like to give? 10, 12, or 15?")
tip_gave = int(tip_gave)
print(f"${tip_gave}")
splited_bill = input("How many people to split the bill?")
splited_bill = int(splited_bill)
print(f"{splited_bill} people")

each_person_should_pay = (total_bill / splited_bill) * (tip_gave * 0.01 + 1)

print(f"Each person should pay: ${each_person_should_pay}")

