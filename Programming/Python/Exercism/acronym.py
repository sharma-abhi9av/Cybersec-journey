def abbreviate(words):
    abbrev = ""
    cdict = {
        "-": " ",
        "?": "",
        "!": "",
        ".": ""
           }
    words_cleaned = words.replace("-", " ").replace("_", " ")
    words2 = words_cleaned.split()
    for a in words2: # now we are on the words, our task it to take the first letter of each word
        abbrev += a[0]
    return abbrev.upper()
    pass
