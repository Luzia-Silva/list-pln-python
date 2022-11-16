num = int(input("Digite um número:"))


def dec2bin(decimal):
    binary = ''
    while decimal > 0:
        binary += str(decimal % 2)
        decimal //= 2
    print("O em binário é: " + binary[::-1])


dec2bin(num)
