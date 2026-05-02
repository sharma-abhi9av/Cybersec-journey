def distance(strand_a, strand_b):
    differnce = 0
    if len(strand_a) != len(strand_b): 
        raise ValueError("Strands must be of equal length.")
    for a in range(len(strand_a)):
        if strand_a[a] != strand_b[a]:
          differnce += 1
    return differnce  
    pass
