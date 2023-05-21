def tax1(income):
    if income <= 12000000:
        tax1 = income * 0.06
    elif income <= 46000000:
        tax1 = 720000 + ((income-12000000) * 0.15)
    elif income <= 88000000:
        tax1 = 5820000 + ((income-46000000) * 0.24)
    elif income <= 300000000:
        tax1 = 15900000 + ((income-88000000) * 0.35)
    else:
        tax1 = 90100000 + ((income-300000000) * 0.38)
    return tax1

incomes = [5000000, 12000000, 30000000, 46000000, 60000000, 88000000, 200000000, 300000000, 400000000]
for income in incomes:
    print("소득: %d \t 세금: %d" % (income, tax1(income)))
