def patoi(err):
    test = int(1)
    test1 = float(1.1)
    test2 = str('a')
    if not int:
        return False
    elif type(err) == type(test):
        res = int(err)
        return res 
    elif type(err) == type(test1):
        res = int(err)
        return res
    elif type(err) == type(test2):
        try:
            res = int(err)
            return res 
        except ValueError:
            return False
    else:
        return False
