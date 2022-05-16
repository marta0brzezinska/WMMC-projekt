import random
from math import *
import scipy.special as sc
import itertools as it
import numpy.linalg as np
from scipy.stats import norm

# Test 1
def frequency_test(sequence):
    """
    The focus of the test is the proportion of zeroes and ones for the entire sequence.

    :param sequence: sequence to be tested.
    :return: whether the the number of ones and zeroes in a sequence is about the same.
    """
    print("Frequency test:")

    n = len(sequence)
    print("n = " + str(n))
    S = 0

    for e in sequence:
        S += 2 * e - 1
    print("S_n = " + str(S))

    S_obs = abs(S) / (sqrt(n))
    print("S_obs = " + str(S_obs))

    p = erfc(S_obs / sqrt(2))
    print("p-value = " + str(p))
    if p < 0.01:
        return False
    else:
        return True


#print(frequency_test([1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0]))


# Test 2
def frequency_test_within_a_block(sequence, M):
    """
    The focus of the test is the proportion of ones within M-bit blocks

    :param sequence: sequence to be tested.
    :param M: the length of each block.
    :return: whether the frequency of ones in an M-bit block is approximately M/2.
    """
    print("Frequency test within a block:")

    n = len(sequence)
    print("n = " + str(n))

    N = floor(n / M)
    print("N = " + str(N))

    pi = [0] * N
    chi = 0

    for i in range(N):
        S = 0
        for j in range(M):
            S += sequence[i * M + j]

        pi[i] = S / M
        chi += (pi[i] - 0.5) ** 2

    chi = 4 * M * chi
    print("Chi^2 = " + str(chi))

    p = 1 - sc.gammainc(N / 2, chi / 2)
    print("p-value = " + str(p))

    if p < 0.01:
        return False
    else:
        return True


#print(frequency_test_within_a_block( [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0], 10))


# Test 3
def runs_test(sequence):
    """
    The focus of this test is the total number of runs in the sequence, where a run is an uninterrupted sequence of
    identical bits.

    :param sequence: sequence to be tested.
    :return: whether the number of runs of ones and zeros of various lengths is as expected for a random sequence.
    """
    print("Runs test:")

    n = len(sequence)
    print("n = " + str(n))

    pi = 0
    V = 0

    for e in sequence:
        pi += e
    pi = pi / n

    print("pi = " + str(pi))

    if frequency_test(sequence):
        for k in range(n - 1):
            if sequence[k] == sequence[k + 1]:
                V += 0
            else:
                V += 1
        V += 1
        print("V = " + str(V))

        p = erfc(abs(V - 2 * n * pi * (1 - pi)) / (2 * sqrt(2 * n) * pi * (1 - pi)))
    else:
        p = 0

    print("p = " + str(p))

    if p < 0.01:
        return False
    else:
        return True


#print(runs_test([1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0]))


# Test 4
def longest_runs_of_ones_in_a_block(sequence):
    """
    The focus of the test is the longest run of ones within M-bit blocks.

    :param sequence: sequence to be tested.
    :return: whether the length of the longest run of ones within the tested
    sequence is consistent with the length of the longest run of ones that would be expected in a random sequence.
    """
    print("Test for the longest runs of ones in a block:")

    n = len(sequence)
    print("n = " + str(n))

    if n >= 750000:
        M = pow(10, 4)
        K = 6
    elif n >= 6272:
        M = 128
        K = 5
    elif n >= 128:
        M = 8
        K = 3
    else:
        print("Sequence too short.")
        return False

    print("M = " + str(M))
    print("K = " + str(K))

    N = floor(n / M)
    m_max = [0] * N
    pi = [0] * N

    for i in range(N):
        m = 1
        print("(", end="")

        for j in range(M - 1):
            print(sequence[i * M + j], end="")
            if sequence[i * M + j] == 1 and sequence[(i * M + j) + 1] == 1:
                m += 1
            else:
                m = 1
            if m > m_max[i]:
                m_max[i] = m

        print(str(sequence[(i * M + j) + 1]) + ")")
        print("max_run = " + str(m_max[i]))

    v = [0] * (K + 1)
    pi = [0] * (K + 1)

    if M == 8:
        pi[0] = 0.2148
        pi[1] = 0.3672
        pi[2] = 0.2305
        pi[3] = 0.1875
        for m in m_max:
            if m >= 4:
                v[3] += 1
            elif m == 3:
                v[2] += 1
            elif m == 2:
                v[1] += 1
            else:
                v[0] += 1
    elif M == 128:
        pi[0] = 0.1174
        pi[1] = 0.2430
        pi[2] = 0.2493
        pi[3] = 0.1752
        pi[4] = 0.1027
        pi[5] = 0.1124
        for m in m_max:
            if m >= 9:
                v[5] += 1
            elif m == 8:
                v[4] += 1
            elif m == 7:
                v[3] += 1
            elif m == 6:
                v[2] += 1
            elif m == 5:
                v[1] += 1
            else:
                v[0] += 1
    elif M == pow(10, 4):
        pi[0] = 0.0882
        pi[1] = 0.2092
        pi[2] = 0.2483
        pi[3] = 0.1933
        pi[4] = 0.1208
        pi[5] = 0.0675
        pi[6] = 0.0727
        for m in m_max:
            if m >= 16:
                v[6] += 1
            elif m == 15:
                v[5] += 1
            elif m == 14:
                v[4] += 1
            elif m == 13:
                v[3] += 1
            elif m == 12:
                v[2] += 1
            elif m == 11:
                v[1] += 1
            else:
                v[0] += 1

    for i in range(K + 1):
        print("v[" + str(i) + "] = " + str(v[i]))

    chi = 0

    for i in range(K + 1):
        chi += ((v[i] - N * pi[i]) ** 2) / (N * pi[i])

    p = 1 - sc.gammainc(K / 2, chi / 2)
    print("p = " + str(p))

    if p < 0.01:
        return False
    else:
        return True


#print(longest_runs_of_ones_in_a_block([1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0]))


def how_many(big_list, small_list):
    cnt = 0
    big_list_len = len(big_list)
    small_list_len = len(small_list)

    for i in range(big_list_len):
        czy = 0
        if big_list_len - i < small_list_len:
            break
        for j in range(small_list_len):
            if big_list[i + j] != small_list[j]:
                czy = 1
        if czy == 0:
            cnt += 1
    return cnt


# Test 5
def serial_test(sequence, m):
    """
    The focus of this test is the frequency of all possible overlapping m-bit patterns across the entire sequence.

    :param sequence: sequence to be tested.
    :param m: the length in bits of a block.
    :return:  whether the number of occurrences of the 2m m-bit overlapping patterns is approximately the same as would
    be expected for a random sequence.
    """
    print("Serial test:")

    n = len(sequence)
    print("n = " + str(n))

    iters = []

    for l in range(3):
        iters.append(
            [list(set(i)) for i in [it.permutations(list(i)) for i in it.combinations_with_replacement([0, 1], m - l)]])

    itersm = []
    itersm_1 = []
    itersm_2 = []

    for i in iters[0]:
        for ii in i:
            itersm.append(list(ii))
    for i in iters[1]:
        for ii in i:
            itersm_1.append(list(ii))
    for i in iters[2]:
        for ii in i:
            itersm_2.append(list(ii))

    n_m = len(itersm)
    n_m_1 = len(itersm_1)
    n_m_2 = len(itersm_2)

    v_m = [0] * n_m
    v_m_1 = [0] * n_m_1
    v_m_2 = [0] * n_m_2

    for i in range(n_m):
        v_m[i] = how_many(sequence + sequence[:m - 1], itersm[i])
    for i in range(n_m_1):
        v_m_1[i] = how_many(sequence + sequence[:m - 2], itersm_1[i])
    for i in range(n_m_2):
        v_m_2[i] = how_many(sequence + sequence[:m - 3], itersm_2[i])

    print(sequence)
    print(itersm)
    print(v_m)
    print(itersm_1)
    print(v_m_1)
    print(itersm_2)
    print(v_m_2)

    psi_m = 0
    psi_m_1 = 0
    psi_m_2 = 0

    for i in range(n_m):
        psi_m += pow(v_m[i], 2)
    psi_m = round(pow(2, m) / n * psi_m - n, 2)

    for i in range(n_m_1):
        psi_m_1 += pow(v_m_1[i], 2)
    psi_m_1 = round(pow(2, m - 1) / n * psi_m_1 - n, 2)

    for i in range(n_m_2):
        psi_m_2 += pow(v_m_2[i], 2)
    psi_m_2 = round(pow(2, m - 2) / n * psi_m_2 - n, 2)

    print("Psi_m = " + str(psi_m))
    print("Psi_m-1 = " + str(psi_m_1))
    print("Psi_m-2 = " + str(psi_m_2))

    delta_psi_m = round(psi_m - psi_m_1, 2)
    delta_2_psi_m = round(psi_m - 2 * psi_m_1 + psi_m_2, 2)

    print("delta Psi_m = " + str(delta_psi_m))
    print("delta^2 Psi_m-1 = " + str(delta_2_psi_m))

    p_1 = 1 - sc.gammainc(pow(2, m - 2), delta_psi_m / 2)
    print("p-value_1 = " + str(p_1))

    p_2 = 1 - sc.gammainc(pow(2, m - 3), delta_2_psi_m / 2)
    print("p-value_2 = " + str(p_2))

    if p_1 < 0.01 or p_2 < 0.01:
        return False
    else:
        return True


#print(serial_test([0, 0, 1, 1, 0, 1, 1, 1, 0, 1], 3))


# Test 6
def non_overlapping_template_matching(sequence, template, M):
    """
    The focus of this test is the number of occurrences of pre-specified target strings.

    :param sequence: sequence to be tested.
    :param template: the binary template to be matched
    :param M: the length in bits of the substring of sequence to be tested.
    :return: wether the generator produces too many occurrences of a given non-periodic (aperiodic) pattern.
    """
    print("Non-overlapping template matching test:")

    n = len(sequence)
    print("n = " + str(n))

    m = len(template)
    print("m = " + str(m))

    N = floor(n / M)
    print("N = " + str(N))

    W = [0] * N

    for i in range(N):
        k = 0
        for j in range(M - m):
            if k == 0:
                if how_many(sequence[i * M + j:i * M + j + m], template) == 1:
                    W[i] += 1
                    k = m - 1
            else:
                k -= 1
    print("W: \n" + str(W))

    mi = (M - m + 1) / pow(2, m)
    print("mi = " + str(mi))

    sigma_2 = M * (1 / pow(2, m) - (2 * m - 1) / pow(2, 2 * m))
    print("sigma^2 = " + str(sigma_2))

    chi = 0
    for i in range(N):
        chi += pow(W[i] - mi, 2) / sigma_2

    print("chi^2 = " + str(chi))

    p = 1 - sc.gammainc(N / 2, chi / 2)
    print("p-value = " + str(p))

    if p < 0.01:
        return False
    else:
        return True


#print(non_overlapping_template_matching([1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0], [0, 0, 1], 10))


# Test 7
def overlapping_template_test(sequence, template, M):
    """
    The focus of the Overlapping Template Matching test is the number of occurrences of pre-specified target strings.

    :param sequence: sequence to be tested.
    :param template: the binary template to be matched
    :param K: the number of degrees of freedom.
    :param M: the length in bits of the substring of sequence to be tested.
    :return: wether the generator produces too many occurrences of a given non-periodic (aperiodic) pattern.
    """
    print("Overlapping template matching test:")

    n = len(sequence)
    print("n = " + str(n))

    m = len(template)
    print("m = " + str(m))

    N = floor(n / M)
    print("N = " + str(N))

    W = [0] * N
    v = [0] * 6

    for i in range(N):
        print("next block")
        for j in range(M - m + 1):
            print(sequence[i * M + j:i * M + j + m])
            if how_many(sequence[i * M + j:i * M + j + m], template) == 1:
                W[i] += 1
        if W[i] > 5:
            W[i] = 5
        v[W[i]] += 1

    print("W: \n" + str(W))
    print("v: \n" + str(v))

    lmbd = (M - m + 1) / pow(2, m)
    print("lambda = " + str(lmbd))

    eta = lmbd / 2
    print("eta = " + str(eta))

    pi = [0.364091, 0.185659, 0.139381, 0.100571, 0.070432, 0.139865]

    chi = 0
    for i in range(6):
        chi += pow(v[i] - N * pi[i], 2) / (N * pi[i])

    print("chi^2 = " + str(chi))

    p = 1 - sc.gammainc(5 / 2, chi / 2)
    print("p-value = " + str(p))

    if p < 0.01:
        return False
    else:
        return True


#print(overlapping_template_test([1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1], [1, 1], 2, 10))


# Test 8
def cusum_test(sequence, mode=0):
    """
    The focus of this test is the maximal excursion (from zero) of the random walk defined by the cumulative sum of
    adjusted (-1, +1) digits in the sequence.

    :param sequence: sequence ot be tested.
    :param mode: a switch for applying the test either forward through the
    input sequence or backward through the sequence.
    :return: whether the cumulative sum of the partial sequences
    occurring in the tested sequence is too large or too small relative to the expected behavior of that cumulative
    sum for random sequences.
    """
    if mode == 1:
        sequence = sequence.reverse()

    print("Cumulative sums test:")

    n = len(sequence)
    print("n = " + str(n))

    X = [2*e-1 for e in sequence]
    print("X: \n" + str(X))

    S=[]
    s = 0

    for i in range(len(X)):
        s += X[i]
        S.append(s)

    print("S: \n" + str(S))

    z = max(S)
    print("z = " + str(z))

    p = 1
    print((-n/z+1)/4)
    for k in range(int((-n/z+1)/4),int((n/z-1)/4+1)):
        p -= norm.cdf(((4*k+1)*z)/sqrt(n)) - norm.cdf(((4*k-1)*z)/sqrt(n))

    for k in range(int((-n/z-3)/4),int((n/z-1)/4+1)):
        p -= norm.cdf(((4*k+3)*z)/sqrt(n)) - norm.cdf(((4*k+1)*z)/sqrt(n))

    print("p-value = " + str(p))

    if p < 0.01:
        return False
    else:
        return True

#print(cusum_test([1,0,1,1,0,1,0,1,1,1]))
#print(cusum_test([1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,1,1,1,0,0,0]))

#Zadanie 2
from nasz_szyfr.cipher import encrypt
from nasz_szyfr.type_transformations import *
import sys
import math

Ps = [14872567809001621032, 6954498729039138283, 16756254131960853230, 446323061891062079, 4830264684336155645]
Ks = [429318306482130432744, 763415601749759243227, 50031453910405071545, 2888037541585809814759, 4008659556570591896234]

def test1():
    results = []

    for j in range(5):
        P = Ps[j]
        K = Ks[j]
        C = []
        tmp_results = []
        for i in range(100):
            C += int_to_list(encrypt(P,K))
            r = random.randrange(64)
            e = 1 << r
            P = e ^ P
        print(C)
        tmp_results.append(frequency_test(C))
        tmp_results.append(frequency_test_within_a_block(C,8))
        tmp_results.append(runs_test(C))
        tmp_results.append(longest_runs_of_ones_in_a_block(C))
        tmp_results.append(serial_test(C,8))
        tmp_results.append(non_overlapping_template_matching(C,[1,0,1],8))
        results.append(tmp_results)
    print(results)
#test1()

def test2():
    results = []
    for j in range(5):
        P = Ps[j]
        K = Ks[j]
        C = int_to_list(P)
        tmp_results = []
        for i in range(100):
            tmp = encrypt(P,K)
            C += int_to_list(tmp)
            P = tmp
        print(C)
        tmp_results.append(frequency_test(C))
        tmp_results.append(frequency_test_within_a_block(C,8))
        tmp_results.append(runs_test(C))
        tmp_results.append(longest_runs_of_ones_in_a_block(C))
        tmp_results.append(serial_test(C,8))
        tmp_results.append(non_overlapping_template_matching(C,[1,0,1],8))
        results.append(tmp_results)
    print(results)

#test2()

def test3():
    results = []

    for j in range(5):
        P = Ps[j]
        K = Ks[j]
        C = []
        tmp_results = []
        for i in range(100):
            C += int_to_list(encrypt(P,K))
            r = random.randrange(64)
            e = 1 << r
            K = e ^ K
        print(C)
        tmp_results.append(frequency_test(C))
        tmp_results.append(frequency_test_within_a_block(C,8))
        tmp_results.append(runs_test(C))
        tmp_results.append(longest_runs_of_ones_in_a_block(C))
        tmp_results.append(serial_test(C,8))
        tmp_results.append(non_overlapping_template_matching(C,[1,0,1],8))
        results.append(tmp_results)
    print(results)

test3()