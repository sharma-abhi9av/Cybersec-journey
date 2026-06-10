def decode(string):
    multiplier = ""
    decoded_string = ""
    for char in string:
        if char.isdigit():
            multiplier += char
        else:
            if multiplier == "":
                decoded_string += char * 1
            else :
                decoded_string += (char) * int(multiplier)
                multiplier = ""
    return decoded_string
            
        
        
    pass
    


def encode(string):
    if string == "":
        return ""
    empty_bucket = ""
    count = 1
    
    for n in range(0,len(string)-1):
        val1 = string[n]
        val2 = string[n+1]
        val3 = string[-1]

        
        if val1 == val2 :
            count += 1 
        else:
            if count == 1 :
                empty_bucket +=  val1 
                count = 1
            else:
                empty_bucket +=  str(count) + val1
                count = 1
    if count ==1:
        empty_bucket += string[-1]
    else: 
        empty_bucket += str(count) + string[-1]
    return empty_bucket 
        
        