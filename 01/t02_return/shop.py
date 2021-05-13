def buy_milk(money = None):
    milk = '[milk]'
    g = int(0)
    if not money:
        money = 0
        return None
    elif money < 25:
        return None
    elif money == 25:
        return milk
    else:
        for i in range(100):
            money = money - 25
            g = g + 1
            if money - 25 == 0:
                return milk * (g + 1)
            elif money < 25:
                return milk * g


def buy_bread(money = None):
    bread = '[bread]'
    n = int(0)
    if not money:
        money = 0
        return None
    elif money < 19:
        return None
    elif money > 57:
        return bread * 3
    elif money == 19:
        return bread
    else:
        for i in range(3):
            money = money - 19
            n = n + 1
            if money - 19 == 0:
                return bread * (n + 1)
            elif money < 19:
                return bread * n
