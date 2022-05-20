#9/14/20
#Steve Christ
#Taxes
#Calculate total taxes given the total income.

#Declare Variables
TotalIncome = float()
TotalTax = float()
TaxRate = float()

#Get Input
TotalIncome = float(input("Enter total income: "))

#Calculate Total Tax
if TotalIncome < 20000:
    TaxRate = 0.0
elif TotalIncome < 100000:
    TaxRate = 0.25
elif TotalIncome < 250000:
    TaxRate = 0.35
else:
    TaxRate = 0.45
TotalTax = TotalIncome * TaxRate

#Display Total Tax
print("Total Tax: $", format(TotalTax, ',.2f'))
