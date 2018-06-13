Number = str(2 ** 1000)
DigitSum = 0


for i in range(len(Number)):
    DigitSum += int(Number[i])

print(DigitSum)
