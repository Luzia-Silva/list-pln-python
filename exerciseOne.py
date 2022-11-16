number = int(input(" Insira um valor inteiro entre 1 e 5: "))

if number in range(1, 6): #valor a mais para realizar comparção
    print(number, " está no intervalo!")
else:
    print(number, "não consta no intervalo!")
