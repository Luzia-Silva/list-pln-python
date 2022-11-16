number = int(input(" Insira um valor inteiro para soma: "))
def eSomar(value):
    counter = 1
    sumValues = 0
    while counter < value:
        sumValues = sumValues + counter
        print(sumValues)
        counter += 1
    print("Essa é a soma do valor digitado: ", sumValues)


eSomar(number)
