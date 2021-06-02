#Python 3.8.5
import math
def repeat():
    print("y = YES\nn = NO")
    repeatvariable = input("Wanna repeat (y/n) : ")
    if repeatvariable == "y":
        calculator(float(input("Enter First Number : ")), float(input("Enter Second Number (If gonna use factorial enter random num) : ")))
    elif repeatvariable == "n":
        print("Good Bye <3")
    else:
        print("Please check your i")
def calculator(a,b):
    def plus(a,b):
        return a + b
    def minus(a,b):
        return a - b
    def multiply(a,b):
        return a * b
    def divide(a,b):
        return a / b
    def modulo(a,b):
        return a % b
    def power(a,b):
        return math.pow(a,b)
    def logarithm(a,b):
        return math.log(a,b)
    def root(a,b):
        if 0<=a: return round(a**(1./b))
        return round(-(-a)**(1./b))
    def factorial(a):
        return math.factorial(a)
    print("Plus = +\nMinus = -\nMultiply = *\nDivide = /\nModulo = %\nPower = **\nRoot = rt\nFactorial = !\nLogarithm = log")
    operator = input("Enter the operator : ")
    if operator == "+":
        answer = plus(a,b)
        result = answer
        print("Answer : {} ".format(answer))
    elif operator == "-":
        answer = minus(a,b)
        result = answer
        print("Answer : {} ".format(answer))
    elif operator == "*":
        answer = multiply(a,b)
        result = answer
        print("Answer : {} ".format(answer))
    elif operator == "/":
        answer = divide(a,b)
        result = answer
        print("Answer : {} ".format(answer))
    elif operator == "%":
        answer = modulo(a,b)
        result = answer
        print("Answer : {} ".format(answer))
    elif operator == "**":
        answer = power(a,b)
        result = answer
        print("Answer : {} ".format(answer))
    elif operator.lower() == "rt":
        answer = root(a,b)
        result = answer
        print("Answer : {} ".format(answer))
    elif operator == "!":
        answer = factorial(a)
        result = answer
        print("Answer : {} ".format(answer))
    elif operator.lower() == "log":
        answer = logarithm(a,b)
        result = answer
        print("Answer : {} ".format(answer))
    repeat()

calculator(float(input("Enter First Number : ")), float(input("Enter Second Number (If gonna use factorial enter random num) : ")))