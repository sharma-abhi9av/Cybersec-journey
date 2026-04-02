def is_paired(input_string):
    empty_bucket = []
    dict = {
           ")" : "(",
           "]" : "[",
           "}" : "{"
           }
    for bracket in input_string:
        if bracket in "([{" :
            empty_bucket.append(bracket)
        elif bracket in ")]}" :
            if len(empty_bucket) == 0:
                return False
            last_open_bracket = empty_bucket.pop()
            correct_bracket = dict[bracket]
            if last_open_bracket != correct_bracket:
                return False
             
    if len(empty_bucket) != 0:
        return False
    return True 

    pass
