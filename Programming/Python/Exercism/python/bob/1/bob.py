def response(hey_bob):
    uppr_string = hey_bob.isupper()
    question_mark = '?'
    l = len(hey_bob)
    zero = '0'
    stripped = hey_bob.strip()
    l2 = len(stripped)
    if l2 == 0 :
        return ("Fine. Be that way!")
    elif uppr_string == True and stripped[-1] != question_mark:
        return ("Whoa, chill out!")
    elif uppr_string == True and stripped[-1] == question_mark:
        return ("Calm down, I know what I'm doing!")
    elif stripped[-1] == question_mark and hey_bob != uppr_string: 
        return ("Sure.")
    else :
        return ("Whatever.")
    pass
