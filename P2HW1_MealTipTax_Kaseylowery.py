# A brief description of the Project
# 9/21/20
# CTI-110 P2HW1 Meal Tip Tax Calculator
# Kasey Lowery
'''
#Input the charge of food,tip percent and tax percent from user
calculate_tax = price*taxPercent
calculate_tip = (price+tax)*tipPercent
calculate_total_price = price+tax+tip
display_tip, tax and total_price
'''
#input the charge of food
cost = float(input('Enter the price for food : '))
#input the tip as percent value
tipPercent =float(input('Enter the tip for the server : '))
#input the tax as percent value
taxPercent = float(input('Enter the tax amount :'))

#calculate the total tax on the food
tax = cost * taxPercent
#calculate total cost as cost + tax
totalCost = cost + tax
#calculate the tip on total amount
tip = totalCost * tipPercent
#add tip to total cost
totalCost += tip

#print the tip, tax and total charge of meal
print('Calculated_tip : $%.2f' %(tip))
print('Calculated_tax : $%.2f' %(tax))
print('Display total cost of meal : $%.2f' %(totalCost))
