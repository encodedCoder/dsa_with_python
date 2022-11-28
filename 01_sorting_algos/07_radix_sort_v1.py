class KeyData:
    def __init__(self, numm, keyy = 0):
        self.numm = numm
        self.keyy = numm % 10
    
    def update_keyy(self, place_of_keyy):
        i = place_of_keyy
        numm = self.numm
        while i > 0:
            numm = numm // 10
            i -= 1
        self.keyy = numm % 10


def num_of_digits(num):
    num_of_digitss = 0
    while num > 0:
        num = num // 10
        num_of_digitss += 1
    return num_of_digitss


def radix_sort(arr):
    arr_length = len(arr)
    max_ele = max(arr)
    num_of_digitss = num_of_digits(max_ele)
    key_data_arr = [[0,0]]*arr_length
    
    for i in range(arr_length):
        data = arr[i]
        key_dataa = KeyData(data)
        key_data_arr[i] = key_dataa
        
    counting_sort(key_data_arr)
    for i in range(1, num_of_digitss):
        for j in range(arr_length):
            key_data_arr[j].update_keyy(i)
        counting_sort(key_data_arr)
    
    for i in range(arr_length):
        arr[i] = key_data_arr[i].numm


def counting_sort(key_data_arr):
    arr_length = len(key_data_arr)
    count_arr = [0]*10
    a = [0]*arr_length #keys array
    B = [0]*arr_length #output key-data pair array

    #extract keys
    for i in range(arr_length):
        a[i] = key_data_arr[i].keyy

    #1 - count the keys
    for i in range(arr_length):
        count_arr[a[i]] += 1

    #2 - find the commulative count of keys
    for i in range(1, 10):
        count_arr[i] += count_arr[i-1]

    #3 - find the sorted output
    i = arr_length - 1
    while i >= 0:
        B[count_arr[a[i]]-1] = key_data_arr[i]
        count_arr[a[i]] = count_arr[a[i]] - 1
        i = i - 1
    
    for i in range(arr_length):
        key_data_arr[i] = B[i]


arr = [329, 457, 657, 389, 436, 720, 355]
print(arr)
radix_sort(arr)
print(arr, end='\n\n')

arr = [121, 432, 564, 23, 1, 45, 788]
print(arr)
radix_sort(arr)
print(arr)
