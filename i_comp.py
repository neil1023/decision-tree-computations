from math import log

def I(p,n):
	pos = p / (p + n)
	neg = n / (p + n)
	
	if pos == 0 and neg == 0:
		return 0
	elif pos == 0:
		return -neg * log(neg, 2)
	elif neg == 0:
		return -pos * log(pos, 2)
	else:
		return (-pos * log(pos, 2)) + (-neg * log(neg, 2))
