##! ********************************************************************
##! **                                                                **
##! **        "seedsMLCG.f" :                                         **
##! **                                                                **
##! **   This program calculates the future or past elements of the   **
##! **   sequence of a Multiplicative Linear Congruential Generator   **
##! **   (MLCG) of pseudo-random numbers (for example, one of the     **
##! **   two MLCG found in RANECU---the generator of PENELOPE).       **
##! **   The previous elements of the sequence are computed using     **
##! **   the multiplicative inverse of the MLCG multiplier, which     **
##! **   is calculated with the Extended Euclidean algorithm.         **
##! **                                                                **
##! **    Each calculated seed initiates a consecutive and disjoint   **
##! **   sequence of pseudo-random numbers with the length selected   **
##! **   by the user (Sequence Splitting method).                     **
##! **                                                                **
##! **    The basic equation behind the algorithm is                  **
##! **   S(i+j) = (a**j * S(i)) MOD m = [(a**j MOD m)*S(i)] MOD m     **
##! **   that is explained in                                         **
##! **     P. L'Ecuyer, Commun. ACM 31 (1988) p.742                   **
##! **                                                                **
##! **    The input parameters are read from the standard input       **
##! **   with the following format:                                   ***************
##! **                                                                             **
##! **  1            [Initial seed for the MLCG]                                   **
##! **  10           [Number of seeds to calculate]                                **
##! **  1            [Enter distance between seeds as a power of 10? (0=no/1=yes)] **
##! **  15           [Distance between seeds (negative for a backward jump)]       **
##! **  40014        [MLCG multiplier (for RANECU: 40014 and 40692)]               **
##! **  2147483563   [MLCG modulus (for RANECU 2147483563 and 2147483399)]         **
##! **                                                                             **
##! **                                                                ***************
##! **    Dependencies:                                               **
##! **      -integer*4 function abMODm(m,a1,a2)                       **
##! **      -integer*4 function expMOD(a,m,power,k)                   **
##! **      -subroutine euclid(a, b, x, y, gcd, a_invers)   


import math
import numpy as np


def abMODm(m, a1, a2):
    m = np.int32(m)
    a1 = np.int32(a1)
    a2 = np.int32(a2)
    H = np.int32(32768)

    a = np.int32(a1)
    s = np.int32(a2)
    p = -np.int32(m)

    first = False
    while a>H:
        #while first == False :
        if np.mod(a,2,dtype='int32')==1:
            p = np.int32(p +s)
            if p>0:
                p = np.int32(p - m)
        a = np.int32(a/2)
        s = np.int32((s-m) + s)
        if s<0:
            s = np.int32(s + m)

        #first = True

    q = np.int32(m//a)
    k = np.int32(s//q)
    s = np.int32(a*(s-k*q) - k*(m-q*a))
   

    while s<0:
        s = np.int32(s + m)

    p = np.int32(p + s)
    if p < 0 :
        p = np.int32(p + m)

    abMODm = p

    return abMODm

def expMOD(a, m, power, k):
    a = np.int32(a)
    m = np.int32(m)
    y = np.int32(1)
    z = np.int32(a)
    power = np.int32(power)
    k = np.int32(k)
    if power == True:
        if k <=9:
            flag = -1
            n = np.int32(10**k)

        else:
            flag = +1
            n = np.int32(10**9)

    else:
        flag = -1
        n = np.int32(k)

    first = False

    while True:
        t = np.int32(np.mod(n,2))
        n = np.int32(n/2)       
        if t!=0:
            y = np.int32(abMODm(m,z,y))
            if n == 0:
                break
        z = np.int32(abMODm(m,z,z))
        


    expMOD = y

    if flag>0:
        n = np.int32(10**(k-9))
        y = 1
        z = np.int32(expMOD)
        flag = - 1

        while True:

            t = np.int32(np.mod(n,2))
            n = np.int32(n/2)

            if t!=0:
                y = abMODm(m,z,y)
                if n == 0:
                    break
                
        
            z = abMODm(m,z,z)


        expMOD = y
        
    return expMOD,z,flag


def euclid(a, b):
    a = np.int32(a)
    b = np.int32(b)

    if a<0 or b<0:
        raise ValueError("a and b must be >=0")

    a_temp = a
    b_temp = b

    x = 1
    y = 0
    r = 0
    s = 1

    while b_temp!=0:
        module = np.mod(a_temp, b_temp, dtype='int32')
        quot = np.int(a_temp/b_temp)
        a_temp = b_temp
        b_temp = module
        new_r = x - quot * r
        new_s = y - quot * s
        x = r
        y = s
        r = new_r
        s = new_s

    gcd = a_temp

    if gcd!=1:
        a_invers = 0
    else:
        a_invers = x

    while a_invers<0:
        a_invers = a_invers + b


    return (x, y, gcd, a_invers)
        



def calc_seeds(s0, ns, power, ds, a, m):
    if a>m:
        raise ValueError("a must be less than m")
    if s0<0:
        raise ValueError("initial seed must be positive")
    if power==False:
        if abs(ds)<1E-18 or abs(ds)>1E18:
            raise ValueError("distance between seeds must be <1E18")
    else:
        if ds<-18 or ds>18:
            raise ValueError("distance between seeds must be <1E18")

##    if a == 40014 and m == 2147483563:
##        print('first generator')
##    elif a==40692 and m == 2147483399:
##        print('second generator')

    if a>m:
        raise ValueError("m must be > a")

    if ds<0:
        x, y, gcd, a_invers = euclid(a, m)
        #print(str(a)+'*'+str(x)+'+'+str(m)+'*'+str(y)+'='+str(gcd))
##        if gcd==1:
##            print('a^-1='+str(a_invers))
##        else:
##            raise ValueError("a and m not coprime")
        if gcd!=1:
            raise ValueError("a and m not coprime")
            

        a = a_invers

##    if power==True:
##        if ds>=0:
##            print('results: ' +str(ns+1) +' seeds, separated 10^'+str(ds)+' units')
##
##        else:
##            print('results: ' +str(ns+1) +' seeds, separated -10^'+str(abs(ds))+' units')
##
##    else:
##        print('results: ' +str(ns+1) +' seeds, separated '+str(ds)+' units')


    #print(str(s0))

    AjMODm = expMOD(a, m, power, abs(ds))[0]
    #print(AjMODm)

    seeds_vec = []
    for i in range(ns):
        s0 = abMODm(m, s0, AjMODm)
        seeds_vec.append(s0)

    return seeds_vec
        


def calc_seed1(s0):
    seed1 = calc_seeds(s0, 10, True, 15, 40014, 2147483563)

    return seed1

def calc_seed2(s0):
    seed2 = calc_seeds(s0, 10, True, 15, 40692, 2147483399)

    return seed2
    
    
    
    
        
            
        


    
        
            
        

            

        


    
        

        
