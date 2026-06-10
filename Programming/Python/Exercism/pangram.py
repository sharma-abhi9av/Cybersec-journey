def is_pangram(sentence):
    sentence = sentence.lower()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for a in alphabets:
        if a not in sentence:
            return False 
    return True 