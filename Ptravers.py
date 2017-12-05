# Clement TRAVERS Guillaume FORTIN Yannis LE BARS
# Groupe B Master ALMA
# Crible d'eratosthene - Langage Python

def eratosthene (n) :
	boolTab = [True for i in range(1, n+1)]
	for cpt in range(2, n) :
		if boolTab[cpt] :
			for cpt2 in xrange(cpt*2, n, cpt) :
				boolTab[cpt2] = False
	result = [j for j in range(2, n) if boolTab[j] == True]
	return result

# version bonus non optimale
def RA_toast (n) :
	nombres = {i for i in range(2,n+1)}
	nonP = {i+i*m for i in range(2,n+1) if True for m in range(1,n+1) if i+i*m <= n}
	premiers = nombres-nonP
	return premiers

