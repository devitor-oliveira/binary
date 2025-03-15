
numberToBinary: int = int(input("Digite um número inteiro: "))

def findMinor(n):
    num: int = 1
    while num < n:
        if num * 2 >= n:
            return num
        num = num * 2

def transformToBinary(number):
    fuckingList: list[int] = []
    while number > 0:
        rest = number % 2
        number = number//2
        fuckingList.append(rest)
    fuckingList.reverse()
    print(fuckingList)
    binaryToDecimal(fuckingList)


def binaryToDecimal(binaryList):
    pot = len(binaryList) - 1
    somatorio = []
    for n in binaryList:
        if n != 0:
            somatorio.append(n * (2 ** pot))
        pot -= 1
    total = sum(somatorio)
    print("resultado: " + str(total))

transformToBinary(numberToBinary)
