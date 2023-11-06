'''
CS 415
Project 1
By Obinna Kalu & Jacob Franco
'''

import random

"""
Problem 1a
Rewrite the function hsum that takes as input a positive integer n and returns
the smallest j such that 1 + 1/2 +1/3 +1/5 + · · ·1/j > n.
"""

#Possible fix: Written in the style of HSUM from the paper. 
def Problem1a(n):
    j = 1
    sum = 0
    while( sum < n):  # was origionally sum <= n
        sum = sum + 1/j   # was sum += 1/j
        j += 1
    return j # was j-1

"""
Problem 1b
Write a function Fibonacci that takes as input a positive integer n and returns
the Fn. We define Fn in the usual way, namely Fm = Fm-1 + Fm-2 with one change: The first
two values of the sequence are F0 =1/2 and F2 =1/3.
"""
def Fibonacci(n):
    if( n == 0):
        return (1/2)
    elif( n == 1):
        return (1/3)
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

"""
Problem 2
The goal of this problem is to implement a modified primality test primality3: Given as
input an integer N and confidence parameter k, first test if N is divisible by 3, 5, 7 or 11. If it
is divisible by any of these numbers output(”no”); else call primality2 with N and k as inputs.
(This in turn calls primality algorithm that randomly chooses a (where 1 < a < N) and tests
if a^N-1 ≡ 1(mod N) and repeats it k times to reduce the probability of error to 2^-k.)
"""
def primality2(n,k):
    if (n == 1):
        return "No"

    for i in range(2, n): 

        if n % i == 0:
            return "No"

    for i in range(k):  #Test confidence parameter

        a = random.randint(2, n - 1)  #Set to N-1 to satisfy 1 < a < N, 2 and N-1 are included 

        if pow(a, n - 1, n) != 1:  #tests a^n-1 mod n
            return "No"

    return "Yes"


def primality3(n,k):

    if (n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0):
       return ("No")

    else:
        return primality2(n,k)


"""
Problem 3
Given integer k, generate a random prime number with n bits. Implement a solution as
follows: generate a random k - 2 binary string and add 1 as the first and the last bit to create
a k bit integer and convert it to decimal. (The reason for the first bit to be 1 is that we want
the number to be odd. The last bit should be 1 since we want no leading 0's.) Then, call
primality3 algorithm you in implemented in Problem 1 with n and k as inputs. (k is the second
parameter in primality2 which is the number of times the Fermat's test is repeated.) Repeat
calling primaility3 until it outputs 'yes'. At this point, you have found a prime number (with
a high probability if k is large enough).
"""

def findRandom():

    # Generate random number
    num = random.randint(0,1)
    
    #return generated number
    return num
    
def generateBinaryString(N):
     
    # Stores the empty string
    S = "1"
 
    # Iterate over the range [0, N - 1]
    for i in range(N-2):
         
        # Store the random number
        x = findRandom()
 
        # Append it to the string
        S += str(x)
    S += "1"
    
    return S
    
def binaryToDecimal(n):

    num = n
    dec_value = 0
      
    # Initializing base
    # value to 1, i.e 2 ^ 0
    base1 = 1
      
    len1 = len(num)
    for i in range(len1 - 1, -1, -1):
        if (num[i] == '1'):
            dec_value += base1
        base1 = base1 * 2
      
    return dec_value

def primeGen(n, k):

    # Generate n-bit number
    NbitNum = generateBinaryString(n)
    numDecimal = binaryToDecimal(NbitNum)
    
    #do {primality3(numDecimal,k)} while (primality3(numDecimal,k) != "Yes")
    
    counter = 0
    
    while True:
        done = primality3(numDecimal,k)
        counter += 1
        if done == "Yes":
            break
            

"""
Problem 4
Given integers n and k, call the algorithm for Problem 3 (with n and k as inputs) to generate
two primes p and q with n bits each, and use them to generate the encryption keys E and the
decryption key D. After computing p and q, compute N = pq. Then, find a random 10 bit
integer E such that gcd (E, (p - 1)(q - 1)) = 1. Next, find D such that DE ≡ 1 (mod N)
using extended Euclid's algorithm. Output N, E and D.
"""

def gcd(a, b):
    if a == 0:
        return b
 
    return gcd(b % a, a)
    
def gcdExtended(a, b):
 
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = gcdExtended(b, a % b)
        return gcd, y, x - (a // b) * y

def genKeys(n,k):
    p = primeGen(n,k)
    q = primeGen(n,k)
    
    if p == q:
        q = primeGen(n,k)
    
    N = p*q
    
    while (gcd(E, (p-1)*(q-1)) != 1):
        randomBinInt = generateBinaryString(10)
        randomDecInt = binaryToDecimal(randomBinInt)
        E = randomDecInt
        
    randomBinInt2 = generateBinaryString(10)
    randomDecInt2 = binaryToDecimal(randomBinInt2)
    
    _, D, _ = gcdExtended(E, (p-1)*(q-1))

    return (N,E,D)
        
        

"""
Problem 5
Given integers N, E, D and M where (E , D) form the RSA encyrption and the decryption
keys, write a function that encrypts the plain-text message M, then decrypts it and prints both
the encrypted and the decrypted messages. (If everything works fine, the decrypted message
must be the same as the plain-text M.)
"""
# (x^e)^d == x mod N
def RSA(m, key):
    N, E, D = key
    enc = pow(m, E, N)
    dec = pow(enc, D, N)
    return enc, dec


def main():
    print("\t----Questions----\n  1A\t 1B\t 2\t 3\t 4\t 5\t 6 (To Quit)\t")
    quest = ""

    while (quest != "6"):
        quest = str(input("Enter the problem you would like to answer: "))

        match quest:
            case "1A":
                n = int(input("Enter a positive integer: "))
                print(Problem1a(n))
                
            case "1B":
                n = int(input("Enter a positive integer: "))
                print(Fibonacci(n))

            case "2":
                n = int(input("Enter an integer: "))
                k = int(input("Enter a confidence parameter: "))
                print(primality3(n,k))

            case "5":
                N = int(input("Enter N: "))
                E = int(input("Enter E: "))
                D = int(input("Enter D: "))
                M = int(input("Enter the plain-text message: "))

                key = (N, E, D)
                enc, dec = RSA(M, key)

                print("Encrypted message:", enc)
                print("Decrypted message:", dec)

            case "6":
                print("Goodbye")

if __name__=='__main__':
    main()

"""
    Case 1 and 2 are done. Unless they fail ravi tests.

    Case 5 input needs to be fixed and rethought before calling
    Need to figure out what probelem to call either 4 or 5
    What parameters do we take for probelm 5
        1. Number to encode
        2. Length (n) for 2 prime numbers
        




"""