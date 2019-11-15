
def gcd_iter(u, v):
    """Iterative Euclidean algorithm"""
	z = u+v
	while z>0:
		if u%z==0 and v%z==0:
			return z
		z-=1
    return 1