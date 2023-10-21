import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = b ** 2 - 4 * a * c

x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a)

if (d == 0):
    print(f"Root:{x1}\n")
elif (d > 0):
    print(f"Root 1:{x1}\nRoot 2:{x2}")
else:
    print("Действительных корней нет")