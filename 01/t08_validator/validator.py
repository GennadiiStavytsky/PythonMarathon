def validator(args):
    ar_args = args.split(' ')
    oper = ar_args[1]
    #a = ar_args[0]
    #b = ar_args[2]
    
    if oper == '':
        return False
    try:
        a = float(ar_args[0])
        b = float(ar_args[2])
    except Exception as e:
        return False
    
    if oper == '>':
        if a > b:
            return True
        if a == b:
            return f'{a} == {b}'
        else:
            return f'{a} < {b}'
    elif oper == '<':
        if a < b:
            return True
        if a == b:
            return f'{a} == {b}'
        else:
            return f'{a} > {b}'
    elif oper == '>=':
        if a == b:
            return f'{a} == {b}'
        elif a <= b:
            return f'{a} <= {b}'
        else:
            return True
    elif oper == '<=':
        if a == b:
            return f'{a} == {b}'
        elif a >= b:
            return f'{a} >= {b}'
        else:
            return True
    elif oper == '==':
        if a == b:
            return True
        elif a >= b:
            return f'{a} >= {b}'
        elif a <= b:
            return f'{a} <= {b}'
    else:
        return False
