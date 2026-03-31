def encode(plain_text):
    blocks = []
    empty_string = ""
    plain_text = plain_text.lower()
    normal = "abcdefghijklmnopqrstuvwxyz"
    reverse = "zyxwvutsrqponmlkjihgfedcba"
    cipher = str.maketrans(normal , reverse)
    
    for letter in plain_text:
        if letter.isalnum():        
                empty_string += letter.translate(cipher) 
            
    
    
    for a in range(0, len(empty_string), 5):
           xd = empty_string[a: a+5]
           blocks.append(xd)
    return " ".join(blocks)
def decode(ciphered_text):
    decoded_string = ""
    normal = "abcdefghijklmnopqrstuvwxyz"
    reverse = "zyxwvutsrqponmlkjihgfedcba"
    decoded_cipher = str.maketrans(normal , reverse)
    
    for letter in ciphered_text:
        if letter.isalnum():        
                decoded_string += letter.translate(decoded_cipher)
    return decoded_string
    pass
