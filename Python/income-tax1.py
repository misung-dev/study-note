def tax1(income):
  taxrates = [(300000000, 0.38), (88000000, 0.35), (46000000, 0.24),
              (12000000, 0.15), (0, 0.06)]
  sortedTaxrates = sorted(taxrates)
  baseTax = {0: 0}

  [prevBaseIncome, prevTaxrate] = sortedTaxrates[0]

  for (baseIncome, taxrate) in sortedTaxrates:
    baseTax[baseIncome] = int(baseTax[prevBaseIncome] +
                              (baseIncome - prevBaseIncome) * prevTaxrate)
    prevBaseIncome = baseIncome
    prevTaxrate = taxrate

  for (baseIncome, taxrate) in taxrates:
    if income > baseIncome:
      return baseTax[baseIncome] + (income - baseIncome) * taxrate


incomes = [5000000, 12000000, 30000000, 46000000, 60000000, 88000000, 200000000,
  300000000, 400000000
]

for income in incomes:
  print("소득: %d \t 세금: %d" % (income, tax1(income)))
