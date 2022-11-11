number = int(
    input(" Insira um valor inteiro para verificar se o valor é par: "))


def ePar(value):
    if (value % 2 == 0):
        print(True)
    else:
        print(False)


ePar(number)
