import re


def check_address(dict):
    tpl = r'^Ukraine,[ ]*[A-Za-z-[ ]*]*,[ ]*[A-Za-z-[ ]*]*[ ]*\d{1,6},[ ]*\d{5}$'
    res = []
    for it in dict:
        if re.match(tpl, dict[it]) is not None:
            res.append(f'The address of {it} is valid.')
        else:
            res.append(f'The address of {it} is invalid.')
    return res