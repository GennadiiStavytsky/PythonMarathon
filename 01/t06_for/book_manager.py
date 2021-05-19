def get_anonymous(books):
    result = []
    for i in books: 
        if " by " in i :
           i = i
        else:
            result = result + [i]
    return result
