a = float(input(" Informe o valor de a"))
b = float(input(" Informe o valor de b"))
c = float(input(" Informe o valor de c"))


def TemRaiz(a, b, c):
    delta = pow(b, 2) - 4 * a * c
    if (delta > 0):
        print('Se Δ > 0, a equação possui duas soluções reais.')
    elif (delta == 0):
        print('Se Δ = 0, a equação possui uma única solução real.')
    else:
        print('Se Δ < 0, a equação não possui solução real.')


TemRaiz(a, b, c)
