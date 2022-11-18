
def compute_hcf(a, b):
    '''
    This function computes HCF
    '''
    smaller = b if a > b else a

    hcf = 1
    for i in range(2, smaller+1):
        if (a % i == 0) and (b % i == 0):
            hcf = i

    return hcf

a = 123
b = 36
hcf = compute_hcf(a, b)
print('HCF of {}, {} is: {}'.format(a, b, hcf))