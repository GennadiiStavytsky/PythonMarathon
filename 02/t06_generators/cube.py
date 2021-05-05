def cube(arg):
    if arg > 0:
        while arg != 0:
            yield arg ** 3
            arg -=1

if __name__ == '__main__':
    n = 3
    print(f'***Passed parameter - {n}***')
    for i in cube(n):
        print(i)
    print('***')

    n = 8
    print(f'***Passed parameter - {n}***')
    for i in cube(n):
        print(i)
    print('***')

    n = 10
    print(f'***Passed parameter - {n}***')
    for i in cube(n):
        print(i)
    print('***')

    n = 0
    print(f'***Passed parameter - {n}***')
    for i in cube(n):
        print(i)
    print('***')

    n = -5
    print(f'***Passed parameter - {n}***')
    for i in cube(n):
        print(i)
    print('***')
