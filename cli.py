import random

def getRange(operador):
    global modificator
    if operador == "somar" or operador == "subtrair" or operador == "multiplicar":
        a = random.randint(0, 10 + modificator)
        b = random.randint(0, 10 + modificator)
    elif operador == "dividir":
        a = random.randint(1, 10 + modificator)
        b = random.randrange(0 * a, (10 + modificator) * a, a)
    else:
        return 0, 0
    return a, b

running = 1
operador = input()
certas = 0
total = 0
modificator = 0
k = 0
while running:
    a, b = getRange(operador)
    #print(a, b)
    if operador == "somar":
        print("{} {} {}".format(b, "+", a))
        result = int(input())
        resultReal = b + a

        if result == resultReal:
            print("Certo")
            certas += 1
            total += 1
        else:
            print("Errado")

    elif operador == "subtrair":
        print("{} {} {}".format(b, "-", a))
        result = int(input())
        resultReal = b - a

        if result == resultReal:
            print("Certo")
            certas += 1
            total += 1
        else:
            print("Errado")

    elif operador == "multiplicar":
        print("{} {} {}".format(b, "*", a))
        result = int(input())
        resultReal = b * a

        if result == resultReal:
            print("Certo")
            certas += 1
            total += 1
        else:
            print("Errado")

    elif operador == "dividir":
        print("{} {} {}".format(b, "/", a))
        result = int(input())
        resultReal = b // a

        if result == resultReal:
            print("Certo")
            certas += 1
            total += 1
        else:
            print("Errado")

    if certas % 3 == 0 and certas:
        print("Increment!")
        modificator += 1 + k
        k += 1
