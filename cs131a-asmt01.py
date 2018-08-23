import math

print("Amount borrowed (programmer input) = $")
mortgage = int(input()) #mortgage = amount borrowed typecasted as int type

print("Annual interest rate (programmer input) =")
interest = float(input()) #interest = annual interest rate as float type
newinterest = interest / 100

print("Payback period (programmer input) =")
period = int(input()) #period = amount of time till repayment in years as int type

#number of months in the period specified
months = period * 12

monInterest = newinterest / 12

#Math Equation
monPay = (mortgage * ( monInterest *( math.pow(1 + monInterest , months )) ) )/ ((math.pow(1 + monInterest, months) - 1))

print("Monthly payment (calculated output) = $ %.2f" % monPay)
    #Amount to be paid monthly (calculated output)
