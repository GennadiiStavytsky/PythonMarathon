mainstring = input("Enter your first string: ")
substring = input("Enter your second string: ")

if mainstring == "" or substring == "":
    print("One of the strings is empty.")

else:
    com = input("Enter your command: ")
    if com != "concat" and com != "find" and com != "beatbox":
        print("usage: command find | concat | beatbox")

    elif com == "concat":
        print(f"Your strings is: {mainstring + ' ' + substring}")

    elif com == "find":
        if substring in mainstring:
            print(True)
        else:
            print(False)

    elif com == "beatbox":
        beat1 = int(input("Enter your first beatbox number: "))
        beat2 = int(input("Enter your second beatbox number: "))

        newstring = mainstring * beat1
        newsub = substring * beat2
        print(newstring + newsub)