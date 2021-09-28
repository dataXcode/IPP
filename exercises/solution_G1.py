num_list = [10,50,30,12,6,8,100]

def max_min_first_last(nlist):
    max_num = max(nlist) # Maximum number
    min_num = min(nlist) # Minimum number
    first_num = nlist[0] # First number
    last_num = nlist[-1] # Last number
    return max_num, min_num, first_num, last_num

max_min_first_last(num_list)
