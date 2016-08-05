from E_comp import E
from I_comp import I

# Information Gain
# p_list and n_list are each size n where n is the number of distinct values for the specified attribute
# each ith item in p_list represents the number of positive records in value i for the specified attribute
def gain(p_list, n_list):
	print(sum(p_list))
	print(sum(n_list))
	print(I(sum(p_list), sum(n_list)))
	return I(sum(p_list), sum(n_list)) - E(p_list, n_list)
