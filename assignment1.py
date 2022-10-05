# This programm should behave like this
# INPUT: What is the total bill?  $ 100
# INPUT: What percentage of bill you want to give as tip? 20
# OUTPUT: Total tip is $20.0


total_bill = input("What is the total bill?  $")
tipPercent = input("What percentage of bill you want to give as tip? ")

# STEPS TO BE TAKEN

# First convert the tipPercent & total_bill to an integer
# Declare a variable tip and write code to calculate the tip 
# Apply mathematical formula tipPercent divided by 100 and multiply by total_bill
# After calculating the tip display this message to the console "Total tip is $__"


# Write CODE Below

total_bill = int(total_bill)
tipPercent = int(tipPercent)

print(type(total_bill))
print(type(tipPercent))

tip = (tipPercent / 100) * total_bill
print("The total is is ${}".format(tip))






data = {
    'name':'alex',
    'age':12,
    'istall': True,
    }

data['isStudent'] = True


print(data)



