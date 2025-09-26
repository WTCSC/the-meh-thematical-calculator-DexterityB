import time
import random

def type(phrase):
    for char in phrase:
        print(char, end = "", flush = True)
        time.sleep(0.02)
    print("")
    time.sleep(0.2)
    return None

banned = []
def response(answer):
    message = random.randint(1, 8)
    while any(number == message for number in banned):
        message = random.randint(1, 8)
    with open("messages.txt") as file:
        buffer = file.read().split(f"%{message}%")[1] + str(answer)
    with open("messages.txt") as file:
        buffer = buffer + file.read().split(f"%{message}.5%")[1]
    banned.append(message)
    if len(banned) == 4:
        del banned[0]
    return type(buffer)

def add(x, y):
    return type(f"{x} + {y}"), response(x + y)

def subtract(x, y):
    return type(f"{x} - {y}"), response(x - y)

def multiply(x, y):
    return type(f"{x} * {y}"), response(x * y)

def divide(x, y):
    return type(f"{x}/{y}"), response(x/y)

def exponent(x, y):
    if x == 0 and y == 0:
        return type("That's undefined, it's like you don't even understand math at all")
    else:
        return type(f"{x}^{y}"), response(x ** y)

type("So like, you wanted to do math or something? Fine")
while True:
    type("What operation are you doing? [+,-,*,/,^] ")
    operation = input("").replace(" ", "")
    while operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "^":
        type("Just put in one of the listed operations, I don't want to deal with this")
        operation = input("").replace(" ", "")
        print("")

    type("I hate that one\n")

    type("What's your first number?")
    x = input("")
    print("")
    while True:
        try:
            x = float(x)
            break
        except:
            type("That's not really a number")
            type("Just what's your first number?")
            x = input("")
            print("")

    type("What's your second number?")
    y = input("")
    print("")
    while True:
        try:
            y = float(y)
            if operation == "/" and y == 0:
                type("You can't really divide by zero. Maybe you should learn how to do math")
                type("What's your real second number?")
                y = input("")
                print("")
            else:
                break
        except:
            type("That's not really a number")
            type("What's your second number? I don't really want to do this anyway, so just hurry it up")
            y = input("")
            print("")

    match operation:
        case "+":
            add(x, y)
        case "-":
            subtract(x, y)
        case "*":
            multiply(x, y)
        case "/":
            divide(x, y)
        case "^":
            exponent(x, y)

    type("Now are you going to bother me with more math? [yes/no]")
    repeat = input("").lower().replace(" ", "")
    print("")
    while repeat != "yes" and repeat != "no":
        type("It's a simple yes or no question, it's not that complicated")
        type("Now, yes or no?")
        repeat = input("").lower().replace(" ", "")
        print("")

    if repeat == "no":
        break