attempts = 0
while True:
    number = int(input("Digite um valor dentro no range 1 ao 10: "))
    attempts = attempts + 1
    if number in range(0, 11):
        print(number, " está no intervalo!")
        break
    elif (attempts == 3):
        print("none")
        break
    else:
        print("Tente novamente! \n\n")
