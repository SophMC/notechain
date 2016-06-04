def distance(dna1, dna2):
	return sum(d1 != d2 for d1, d2 in zip(dna1, dna2))