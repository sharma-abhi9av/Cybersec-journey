def is_isogram(string):
    string = string.lower()
    llist = list(string)
    for a in string:
        if a.isalpha():
            if llist.count(a) > 1:
                return False
            
    return True
        
    pass
