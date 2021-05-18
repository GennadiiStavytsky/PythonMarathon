def add_to_bookshelf(book_to_add,bookshelf):
    i = int(0)
    g = len(bookshelf)
    while i  < g:    
        if bookshelf[i] == ('---'):
            bookshelf[i] = book_to_add
            return True 
        i = i + 1   
    else:
        return False
