#Nesse TDE o Grupo irá desenvolver uma Calculadora para diferentes bases numéricas.

#1) A aplicação deverá ser feita em Linguagem Python

#2) As bases a serem usadas serão a base 10 (decimal), a 2 (binário), a 8 (octal e a 16 (hexadecimal)

#3) A aplicação deve permitir a seleção de uma base de referência e permitir a conversão para as demais

#4) A aplicação deverá permitir a operação de Soma, Subtração nas diferentes bases.

def decimalSum(a, b):

    return a + b

def decimalSubtraction(a, b):

    return a - b

def binarySum(a, b):

    return 0

def allSum(a, b, base):

  aDecimal = int(a, base)
  bDecimal = int(b, base)

  result = aDecimal + bDecimal

  return result

def allSubtract(a, b, base):

  aDecimal = int(a, base)
  bDecimal = int(b, base)

  result = aDecimal - bDecimal

  return result

def sumOrSubtract():

    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Nenhum")
    print("Gostaria de somar ou subtrair?")

def funcao(num):
    convertedNumber = bin(num)

    print('{} convertido para binário é {}.'.format(num, bin(num)))

    return convertedNumber

def funcao_octal(num):
    convertedNumber = oct(num)

    print('{} convertido para octal é {}'.format(num, convertedNumber))

    return convertedNumber

def funcao_hexadecimal(num):
    convertedNumber = hex(num)

    print('{} convertido para hexadecimal é {}'.format(num, convertedNumber))

    return convertedNumber

menu = ''
num = 0
sumOrSubtractOption = 0
base = 0

while menu != '4':

  num = int(input("digite o número: "))

  while (sumOrSubtractOption != 3):

    sumOrSubtract()
    sumOrSubtractOption = int(input(": "))

    if (sumOrSubtractOption <= 2):
        num2 = int(input("digite o número b: "))

        if (sumOrSubtractOption == 1):
            sum = decimalSum(num, num2)
            print("A soma de {} e {} é {}.".format(num, num2, sum))
            num = sum

        elif (sumOrSubtractOption == 2):
            subtraction = decimalSubtraction(num, num2)
            print("A subtração de {} e {} é {}.".format(num, num2, decimalSubtraction(num, num2)))
            num = subtraction

  sumOrSubtractOption = 0

  print("digite a opção desejada")
  print("1 - para binario")
  print("2 - para octal")
  print("3 - para hexadecimal")
  print("4 - sair")

  menu = input(": ")

  if menu == '1':
    base = 2
    num = funcao(num)

  elif menu == '2':
    base = 8
    num = funcao_octal(num)


  elif menu == '3':
        base = 16
        num = funcao_hexadecimal(num)

  elif(menu == '4'):
    ("sair")

  while (sumOrSubtractOption != 3):

    sumOrSubtract()
    sumOrSubtractOption = int(input(": "))

    if (sumOrSubtractOption <= 2):
        num2 = int(input("digite o número b: "))
        if (base == 2):
            num2 = bin(num2)
        elif (base == 8):
            num2 = oct(num2)
        elif (base == 16):
            num2 = hex(num2)

        if (sumOrSubtractOption == 1):
            sum = allSum(num, num2, base)

            if(base == 2):
                sum = bin(sum)
            elif(base == 8):
                sum = oct(sum)
            elif(base == 16):
                sum = hex(sum)

            print("A soma de {} e {} é {}.".format(num, num2, sum))

            num = sum

        elif (sumOrSubtractOption == 2):
            subtraction = allSubtract(num, num2, base)
            if (base == 2):
                subtraction = bin(subtraction)
            elif (base == 8):
                subtraction = oct(subtraction)
            elif (base == 16):
                subtraction = hex(subtraction)

            print("A subtração de {} e {} é {}.".format(num, num2, subtraction))

            num = subtraction