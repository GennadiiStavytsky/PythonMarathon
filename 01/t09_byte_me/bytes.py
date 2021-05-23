def convert_to_bytes(int1,boo,stri):
    try:
        print(f'''-- The int value is "{int1}"
bytes: "{bytes(int(int1))}"''')
    except ValueError:
        return False
    if boo == 'True':
        boo = True
    else:
        boo = False
    print(f'''-- The bool value is "{boo}"
bytes: "{bytes(boo)}"''')
    print(f'''-- The string value is "{stri}"
bytes: "{bytes(stri,encoding = 'utf-8')}"''')
