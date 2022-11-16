word = input("Informe uma frase: ")


def isInt(value):
    try:
        int(value)
        return True
    except:
        return False


def accountCharacters(sentence):
    isIntSentence = isInt(sentence)
    countSentence = len(sentence)
    if (isIntSentence or countSentence == 0):
        print("Você não informou nenhuma frase 😫, então não existe cadeia para você de palavras ")
        print("0")
    else:
        print("Essa é a quantidade de palavras na sua frase",
              countSentence, "palvras ❤️ ❤️ \n")
        print("Essa é a sua cadeia de palavras 😁\n")
        for words in sentence:
            print(words)


accountCharacters(word)
