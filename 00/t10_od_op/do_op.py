print("---- Simple calculator ----")
print("Let's add some numbers")
value1 = int(input('Input your first value: '))
operator = str(input('Input your operator: '))

if operator == '+':
    value2 = int(input('Input your second value: '))
    result = value1 + value2
    print("{} {} {} = {}".format(value1, operator, value2, result))

elif operator == '-':
    value2 = int(input('Input your second value: '))
    result = value1 - value2
    print("{} {} {} = {}".format(value1, operator, value2, result))

elif operator == '*':
    value2 = int(input('Input your second value: '))
    result = value1 * value2
    print("{} {} {} = {}".format(value1, operator, value2, result))

elif operator == '/':
    value2 = int(input('Input your second value: '))
    result = value1 / value2
    print("{} {} {} = {}".format(value1, operator, value2, result))

else:
    print("usage: operator must be '*' or '+' or '-' or '/'")

print("---- Simple calculator ----")
