def to_rna(dna_strand):
    rna = ""
    translate = {
          "G": "C",
          "C": "G",
          "T": "A",
          "A": "U"        
    }

    for a in dna_strand:
        rna += translate[a]
    return rna
    pass
