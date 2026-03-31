def to_rna(dna_strand):
    rna = ""
    for a in dna_strand:
        if a == "G":
            rna += "C" 
        if a == "C":
            rna += "G"
        if a == "T":
            rna += "A" 
        if a == "A":
            rna += "U"
    return rna
    pass
