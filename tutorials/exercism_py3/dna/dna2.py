DNA_TO_RNA = str.maketrans("GCTA", "CGAU")

def to_rna(dna):
    return dna.translate(DNA_TO_RNA)