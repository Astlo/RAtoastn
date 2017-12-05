
# Clement TRAVERS Guillaume FORTIN Yannis LE BARS
# Groupe B Master ALMA
# Crible d'eratosthene - Langage Julia

function RA_toast(n)
	T = [true for i in 1:n];
	for i = 2:n
		if T[i] == true
			j=2*i;
			while j<=n
				T[j] = false;
				j=j+i;
			end
		end
	end
	return [i for i in 2:n if T[i]==true];
end