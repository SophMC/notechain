
def to_rna(dna):
    
    d={'G':'C','C':'G','T':'A','A':'U'}
    
    p = list(dna)
    return ''.join([d[m] for m in p])
        
    