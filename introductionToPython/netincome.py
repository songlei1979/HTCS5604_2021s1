import PAYE

gross_income = input("Please input your salary: ")
print(PAYE.totalTax(float(gross_income)))
try:
    if float(gross_income) > 0:
        tax = PAYE.totalTax(float(gross_income))
        print(float(gross_income)-tax)
    else:
        print("Wrong input")
except:
    print("Wrong input")
