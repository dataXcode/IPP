savings = 100.0
#1 Convert savings to integer
savings = int(savings)

factor = "1.1"
#2 Convert factor to float
factor = float(factor)

years = "9"
#3 Convert years to integer
years = int(years)

#4 Calculate the result
result = savings * factor **years

#5 Print out the result
print("I started with $" + str(savings) + " and now after " + str(years) + " years I have $" + str(result))