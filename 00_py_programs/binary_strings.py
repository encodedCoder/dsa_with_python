'''
This program prints the binary strings of length 'n' which do not conatain two consecutive ones
'''

def binary_strings(length):
    if length <= 0:
        print("Invalid length"); return False
    elif length == 1:
        return ['0', '1']
    elif length == 2:
        return ['00', '01', '10']
    elif length > 2:
        a = binary_strings(length-1)
        a = ['0'+ele for ele in a]

        b = binary_strings(length-2)
        b = [ele+'01' for ele in b]

        return a.extend(b)


a = binary_strings(3)
print(a)  