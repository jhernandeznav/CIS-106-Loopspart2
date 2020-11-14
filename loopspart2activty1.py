principle = float(input("Enter the principle: "))
rate = float(input("Enter the interest rate: "))
year = int(input("Enter the term in years: "))
x = 1
print("Principle:$ ", principle)
print("Interest rateL ", rate, "%")
print("Term in years: ", year)

for i in range(year):
    print("Year", x, ":")
    print("Starting amount: ", principle)
    interest = principle * rate / 100
    print("Interest: ", interest)
    principle = principle+interest
    print("End year balance: ", principle)
    x = x + 1
    year = year - 1
