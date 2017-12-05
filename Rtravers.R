# Clement TRAVERS Guillaume FORTIN Yannis LE BARS
# Groupe B Master ALMA
# Crible d'eratosthene - Langage R

# pas optimal
toast <- function(n) {
  if (n < 2) return(NULL)
  a <- rep(T, n)
  a[1] <- F
  for(i in seq(2, n)) {
    for(j in seq(2, i-1)) {
      if(i %% j == 0) {
        a[i] <-F
      }
    }
  }
  return(which(a))
}

toast(10^4)
