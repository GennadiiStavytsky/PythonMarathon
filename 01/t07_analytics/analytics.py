def print_str_analytics(str):
    printable = 0
    a_num = 0
    a_bet = 0
    dec = 0
    lower = 0
    upper = 0
    w_space = 0
    for i in str:
        if i.isprintable() == True:
            printable += 1
        if i.isalnum() == True:
            a_num += 1
        if i.isalpha() == True:
            a_bet += 1
        if i.isdecimal() == True:
            dec += 1
        if i.islower() == True:
            lower += 1
        if i.isupper() == True:
            upper += 1
        if i.isspace() == True:
            w_space += 1
    print(f"""|------------------------------------------------|
|                String analytics                |
|------------------------------------------------|
| '{str}'
|------------------------------------------------|
| Number of printable characters is: {printable}
| Number of alphanumeric characters is: {a_num}
| Number of alphabetic characters is: {a_bet}
| Number of decimal characters is: {dec}
| Number of lowercase letters is: {lower}
| Number of uppercase letters is: {upper}
| Number of whitespace characters is: {w_space}
|------------------------------------------------|""")

