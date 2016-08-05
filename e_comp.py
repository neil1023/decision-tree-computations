from i_comp import I

# Entropy computation
# example for parameters: [1,4,5], [2,1,4]
def E(p_list, n_list):
	if len(p_list) != len(n_list):
		print("Error: each parameter should be a list of size n")
		return

	total = sum(p_list) + sum(n_list)
	result = 0
	for p, n in zip(p_list, n_list):
		result += ((p + n) / total) * I(p,n)

	return result
