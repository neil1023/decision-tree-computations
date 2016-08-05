from math import log

def I(p,n):
	pos = p / (p + n)
	neg = n / (p + n)
	return (-pos * log(pos, 2)) + (-neg * log(neg, 2))
