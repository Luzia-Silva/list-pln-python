number = int(
    input(" Insira um valor inteiro para verificação se o valor é par ou primo:  "))


def ePrimo(value):
    if (number > 0 and value % 2 == 0):
        print(True)
    elif (number > 2 and value / value == 1):
        print(False)
    else:
        print(None)


ePrimo(number)
