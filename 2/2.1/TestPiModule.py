import PiNumber
from PiNumber import GetPi

rectangleAmount = input("Введите число прямогульников для определения числа пи: ")
print(f"Функция:\t{PiNumber.Get(rectangleAmount)}\nЛямбда: \t{GetPi(int(rectangleAmount))}")