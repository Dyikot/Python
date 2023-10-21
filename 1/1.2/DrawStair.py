import sys

stepAmount = int(sys.argv[1])
for sharpAmount in range(1, stepAmount + 1):
    spaceAmount = stepAmount - sharpAmount
    spaces = spaceAmount * " "
    sharps = sharpAmount * "#"
    print(f"{spaces}{sharps}")