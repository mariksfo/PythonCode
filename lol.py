def divide(number1, number2):
    try:
        number1/number2
    except ZeroDivisionError as e:
        print("You can't devide a number by zero man!")
    except TypeError as error:
        print("go home bozo you suck LLL")





divide('0','1589')