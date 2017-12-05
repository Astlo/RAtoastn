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

import time
def mesureEra (taille, nbech) :
	t_avant = time.time()
	for ech in range(nbech) :
		s = eratosthene(taille)
	print( (time.time() - t_avant) / nbech)

