import numpy as np

def bin2array(str ) :
    ans = []
    for el in str:
        ans.append(int(el))
    return ans

def array2bin(array ) :
    ans = ''
    for el in array:
        ans += str(el)
    return ans

def array2numb(array , n ) :
    ans = 0
    while len(array) < n:
        np.insert(array,0,0)
    for i in range(len(array)):
        ans += pow(2, len(array) - 1 - i) * int(array[i])
    return ans

def numb2array(numb , n ) :
    ans = []
    pom = bin(numb)[2:].zfill(n)
    for el in pom:
        ans.append(int(el,10))
    return ans