def rotate(text, key):
    rot = ""
    for letter in text:
        if letter.isalpha():

            
            if letter.islower():
              numbers = ord(letter) - 97
              numbers1 = numbers + key  
              rotted_number = numbers1 % 26 
              rotted_number = rotted_number + 97
              chracter = chr(rotted_number)
              rot += chracter

        
            if letter.isupper():
             numbers = ord(letter) - 65
             numbers1 = numbers + key  
             rotted_number = numbers1 % 26 
             rotted_number = rotted_number + 65
             chracter = chr(rotted_number)
             rot += chracter

        else:
            rot += letter
    return rot
    pass
