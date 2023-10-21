import sys

numberString = sys.argv[1]
numberStringSum = 0
for symbol in numberString:
    numberStringSum = numberStringSum + int(symbol)

print(numberStringSum)