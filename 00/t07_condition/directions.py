sign = input('There are 3 signs in front of you. Which one would you like to read? ')

if sign == 'right':
    print(f'The {sign} sign says: "DEAD PEOPLE ONLY"')
elif sign == 'left':
    print(f'The {sign} sign says: "BEWARE!"')
elif sign == 'middle':
    print(f'The {sign} sign says: "CERTAIN DEATH"')
else:
    print(f'There is no {sign} sign')