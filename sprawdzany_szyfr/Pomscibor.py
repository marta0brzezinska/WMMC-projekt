import hashlib
import hmac
from math import ceil
import math
import random
from pomocnicze import *

## Expand_Key
hash_len = 32
key_len = 16
rounds_numb = 16
  
def hmac_sha256(key, data):
    return hmac.new(key, data, hashlib.sha256).digest()

# zrodlo wikipedia podac tu link
def hkdf(length, ikm, salt, info):
    """Funkcja pozwalająca na wygenerowanie podklucza o danej długości"""
    if len(salt) == 0:
        salt = bytes([0] * hash_len)
    prk = hmac_sha256(salt, ikm)
    t = b""
    okm = b""
    for i in range(ceil(length / hash_len)):
        t = hmac_sha256(prk, t + info + bytes([i + 1]))
        okm += t
    return okm[:length]

def Expand_Key(key)  :
    ''' Funkcja uzywajaca HKDF do generowania odpowiedniej liczby podkluczy danej dlugosci z klucza wejsciowego'''
    keys = []
    salt = b''
    for i in range(rounds_numb):
        info = b'round_number_' + bytes(str(i+1), 'utf-8') 
        pom = numb2array(int.from_bytes(hkdf(key_len, ikm = key, salt = salt, info = info), byteorder = 'big'), 64)
        keys.append(pom)
    return keys

# key = b'Alakazam'.hex()
# key = 32 * [0,1]
# print(array2numb(key, 64))
# print(Expand_Key(int.to_bytes(array2numb(key, 64), 64, byteorder = 'big'), 16, 16))

## Sub_Sbox

def odwracalnosc(sbox ) :
    '''Bada odwracalność Sboxa'''
    s = sbox.copy()
    s.sort()
    for i in range(len(s)):
        if s[i] != i:
            return False
    return True 

def zupelnosc(s) :
    '''Bada zupełność Sboxa'''
    m = int(math.log(len(s),2))
    tablica_j = [0]*m
    for i in range(m):
        for el in range(len(s)):
            wynik = bin(s[el] ^ s[el ^ (2**i)])[2:].zfill(m)
            for j in range(m):
                if wynik[j] == '1':
                    tablica_j[j] = 1       
        if sum(tablica_j) != m:
            return False
        tablica_j = [0] * m
    return True

def generowaniesboxa(dlugosc) :
    '''Generuje Sboxa o odpowiednich własnościach'''
    s = list(range(dlugosc))
    wlasnosci = False
    while not wlasnosci:
        random.shuffle(s)
        if odwracalnosc(s) and zupelnosc(s):
            wlasnosci = True  
    return s

def inv_sbox(s) :
    '''Odwraca Sboxa'''
    inv = [0]*len(s)
    for i in range(len(s)):
        inv[s[i]] = i
    return inv

def parzyste(text) :
    '''Zwraca tekst złożony jedynie z elementów o parzystych indeksach'''
    parzyste = ''
    for i in range(len(text)):
        if i % 2 == 0: 
            parzyste += text[i]
    return parzyste

def nieparzyste(text) :
    '''Zwraca tekst złożony jedynie z elementów o nieparzystych indeksach'''
    nieparzyste = ''
    for i in range(len(text)):
        if i % 2 == 1: 
            nieparzyste += text[i]
    return nieparzyste

def laczenie(p , np) :
    '''Łączy teksty złożone z elementów o parzystych i nieparzystych indeksach w całość'''
    text = [0]*2*len(p)
    for i in range(len(p)):
        text[2*i] = p[i]
        text[2*i + 1] = np[i]
    text = ''.join([str(elem) for elem in text])
    return text

# Sboxy  
sbox1 = [8, 50, 74, 248, 123, 158, 17, 228, 181, 141, 59, 57, 169, 91, 31, 147, 117, 186, 63, 153, 216, 140, 226, 122, 185, 221, 130, 35, 23, 242, 199, 120, 66, 60, 101, 239, 100, 219, 121, 48, 148, 58, 233, 132, 51, 229, 188, 131, 76, 96, 133, 126, 37, 249, 32, 211, 172, 206, 171, 14, 94, 33, 207, 118, 30, 106, 253, 69, 220, 200, 251, 46, 215, 38, 39, 29, 88, 197, 222, 178, 159, 89, 19, 134, 61, 92, 6, 198, 108, 154, 129, 184, 146, 124, 164, 55, 152, 40, 80, 49, 41, 234, 54, 79, 183, 21, 81, 5, 16, 90, 182, 177, 43, 231, 236, 232, 142, 68, 47, 208, 53, 110, 210, 107, 115, 137, 26, 202, 56, 170, 34, 144, 179, 173, 87, 13, 189, 4, 99, 83, 145, 20, 70, 112, 254, 245, 3, 84, 109, 246, 243, 223, 252, 105, 86, 45, 250, 161, 238, 175, 163, 149, 12, 1, 139, 85, 174, 125, 143, 44, 150, 7, 209, 67, 10, 64, 167, 11, 213, 162, 191, 52, 73, 127, 15, 180, 75, 205, 71, 155, 247, 218, 24, 27, 28, 193, 168, 165, 93, 195, 102, 160, 166, 0, 104, 136, 78, 190, 98, 77, 65, 204, 201, 230, 82, 224, 255, 116, 97, 176, 196, 157, 95, 42, 25, 62, 240, 237, 128, 203, 135, 187, 9, 214, 225, 2, 114, 36, 194, 119, 241, 138, 103, 156, 244, 192, 151, 113, 235, 212, 72, 217, 111, 227, 18, 22]
sbox2 = [107, 48, 113, 90, 208, 147, 127, 234, 190, 5, 215, 53, 89, 198, 142, 228, 73, 140, 55, 104, 83, 33, 231, 239, 235, 154, 47, 52, 117, 79, 8, 254, 168, 159, 227, 97, 82, 32, 2, 46, 243, 151, 18, 210, 31, 203, 179, 184, 12, 133, 169, 124, 131, 244, 66, 205, 136, 122, 187, 191, 158, 153, 241, 123, 163, 135, 170, 13, 173, 102, 192, 217, 35, 30, 177, 120, 51, 34, 202, 165, 150, 226, 38, 41, 1, 139, 62, 77, 87, 194, 67, 105, 141, 193, 39, 253, 100, 138, 220, 129, 188, 78, 10, 145, 64, 238, 130, 44, 229, 240, 43, 126, 76, 245, 146, 197, 20, 101, 23, 219, 16, 60, 14, 167, 211, 207, 29, 134, 195, 110, 221, 251, 172, 255, 204, 40, 248, 199, 246, 4, 11, 45, 91, 92, 137, 15, 164, 85, 128, 232, 186, 109, 185, 98, 61, 176, 196, 144, 56, 157, 162, 206, 25, 181, 183, 21, 152, 224, 116, 249, 222, 63, 115, 161, 118, 149, 71, 0, 72, 54, 201, 3, 189, 7, 49, 132, 247, 114, 112, 68, 94, 36, 216, 148, 252, 37, 155, 236, 225, 213, 42, 108, 50, 84, 80, 182, 166, 57, 223, 160, 27, 143, 93, 233, 9, 28, 171, 237, 24, 214, 88, 19, 95, 180, 86, 26, 175, 70, 212, 119, 242, 121, 103, 96, 65, 6, 75, 74, 106, 218, 58, 81, 17, 22, 200, 178, 125, 111, 156, 230, 59, 250, 99, 209, 174, 69]

def Sub_Sbox(wektor) :
    '''Zwraca wartość Sboxa dla danego napisu 0 i 1''' 
    p = parzyste(wektor) 
    np = nieparzyste(wektor) 
    p1 = ''.join([bin(sbox1[int(p[8*i:(8*i+8)],2)])[2:].zfill(8) for i in range(4)])
    np1 = ''.join([bin(sbox2[int(np[8*i:(8*i+8)],2)])[2:].zfill(8) for i in range(4)])
    return laczenie(p1, np1)

def Inv_Sub_Sbox(wektor) :
    '''Zwraca wartość odwrotności Sboxa dla danego napisu 0 i 1''' 
    p = parzyste(wektor) 
    np = nieparzyste(wektor) 
    p1 = ''.join([bin(inv_sbox(sbox1)[int(p[8*i:(8*i+8)],2)])[2:].zfill(8) for i in range(4)])
    np1 = ''.join([bin(inv_sbox(sbox2)[int(np[8*i:(8*i+8)],2)])[2:].zfill(8) for i in range(4)])
    return laczenie(p1, np1)
    
## Shift
def Shift(c) :
    ''' Cykliczne przesuwa szyfr o 3 w lewo'''
    c = np.roll(c,-3)
    return c

def Inv_Shift(c) :
    ''' Cykliczne przesuwa szyfr o 3 w prawo'''
    c = np.roll(c,3)
    return c


## Add_RoundKey


def Add_RoundKey(c , key) :
    ''' Xoruje wektor stanu z kluczem '''
    xor = []
    
    for i in range(len(c)):
        xor.append(c[i] ^ key[i])

    return xor


## Lin_Transform


def Lin_Transform(state) :
    '''Wykonuje pseudotransformację Hadamarda na wektorze stanu'''
    k = 5
    a = 0
    b = 0
    r = 1
    for i in range(2**k):
        a += r*state[2**k-1-i]
        b += r*state[2**(k+1)-1-i]
        r *= 2
    a_1 = (a + b) % 2**(2**k)
    b_1 = (a + 2*b) % 2**(2**k)
    for i in range(2**k):
        state[2**k-1-i] = a_1 & 1
        state[2**(k+1)-1-i] = b_1 & 1
        a_1 >>= 1
        b_1 >>= 1
    return state

## Inv_Lin_Transform


def Inv_Lin_Transform(state)  :
    '''Wykonuje funkcję odwrotną do pseudotransformacji Hadamarda na wektorze stanu'''
    k = 5
    a = 0
    b = 0
    r = 1
    for i in range(2**k):
        a += r*state[2**k-1-i]
        b += r*state[2**(k+1)-1-i]
        r *= 2
    a_1 = (2*a - b) % 2**(2**k)
    b_1 = (b - a) % 2**(2**k)
    for i in range(2**k):
        state[2**k-1-i] = a_1 & 1
        state[2**(k+1)-1-i] = b_1 & 1
        a_1 >>= 1
        b_1 >>= 1
    return state


## Cipher


def Pomscibor_Encrypt(message, key) :
    ''' Funkcja szyfrująca naszego szyfru Pomścibor '''
    # Init
    message = numb2array(int.from_bytes( message, byteorder = 'big'), 64)
    keys = Expand_Key(key)

    # "Key whitening"
    c = Add_RoundKey(message,keys[0])

    for i in range(0,rounds_numb - 2): # do 15 rundy
        c = bin2array(Sub_Sbox(array2bin(c)))
        c = Shift(c)
        c = Lin_Transform(c)
        c = Add_RoundKey(c, keys[i+1])

    # Ostatnia runda
    c = bin2array(Sub_Sbox(array2bin(c)))
    c = Shift(c)
    c = Add_RoundKey(c, keys[rounds_numb - 1])

    # Zmiana typu
    c = int.to_bytes(array2numb(c, 64), 8, byteorder = 'big')
    return c


def Pomscibor_Decrypt(cipher, key):
    ''' Funkcja deszyfrująca naszego szyfru Pomścibor '''
    # Init
    cipher = numb2array(int.from_bytes( cipher, byteorder = 'big'), 64)
    keys = Expand_Key(key)

    # "Key whitening"
    m = Add_RoundKey(cipher,keys[rounds_numb - 1])

    for i in range(rounds_numb - 1, 1, -1): # do 15 rundy
        m = Inv_Shift(m)
        m = bin2array(Inv_Sub_Sbox(array2bin(m)))
        m = Add_RoundKey(m, keys[i-1])
        m = Inv_Lin_Transform(m)

    # Ostatnia runda
    
    m = Inv_Shift(m)
    m = bin2array(Inv_Sub_Sbox(array2bin(m)))
    m = Add_RoundKey(m, keys[0])

    # Zmiana typu
    m = int.to_bytes(array2numb(m, 64), 8, byteorder = 'big')
    return m


#Testy

def test(message, key):
    c = Pomscibor_Encrypt(message, key)
    ans = Pomscibor_Decrypt(c, key)
    return ans == message

def Main_Test():
    k = 0
    for i in range(10):
        key = random.randbytes(8)
        for j in range(100):
            k +=1
            print("Test",k)
            m = random.randbytes(8)
            ans = test(m, key)
            if not ans :
                print("Wiadomość ", m, " z kluczem ", key ," została odszyfrowana błędnie, test niezaliczony!") 
                break
        if j < 99:
            break
        if i == 9:
            print("Wszystkie testy zostały zaliczone, jest moc")

# Main_Test()