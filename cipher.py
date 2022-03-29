""""
Implementacja szyfru blokowego zaprojektownego w ramach projektu z przedmiotu WMMC.

Marta Brzezińska
Kinga Kawczyńska
"""
from type_transformations import *

def S(input, i):
    #TODO: poddanie int input przekształceniu S_i w zależności od numeru rundy i
    return None

def P(input):
    tab = int_to_list(input)

    P=[ 8, 15, 22, 29, 36, 43, 50, 57,
        1, 16, 23, 30, 37, 44, 51, 58,
        2, 9, 24, 31, 38, 45, 52, 59,
        3, 10, 17, 32, 39, 46, 53, 60,
        4, 11, 18, 25, 40, 47, 54, 61,
        5, 12, 19, 26, 33, 48, 55, 62,
        6, 13, 20, 27, 34, 41, 56, 63,
        7, 14, 21, 28, 35, 42, 49, 64]

    #TODO: podstawienie

    output = list_to_int(tab)
    return output


def key_schedule(key):

    #TODO: schemat wyłaniania podkluczy

    return None

def encrypt(plaintext, key):

    #TODO: kod szyfrujący

    return None

def decrypt(ciphertext, key):

    #TODO: kod deszyfrujący

    return None
