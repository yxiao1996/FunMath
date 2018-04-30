import os
import math
import numpy as np
import pyximport
pyximport.install()
from prime.primes import primes
from prime.primes_python import primes_python

# upper bound should be some ten to a even number's power
upper_bound = 10000
check_bound = math.sqrt(upper_bound)

# evaluate number of primes under this bound
num_prime = upper_bound / math.log(upper_bound)

# check if previous generated
if os.path.exists('./primes_'+str(upper_bound)+'.npy'):
    prime_list = np.load('./primes_'+str(upper_bound)+'.npy')
else:
    # generate prime list
    prime_list = primes_python(int(num_prime * 1.2))
    # save
    np.save('./primes_'+str(upper_bound)+'.npy', np.array(prime_list))
print prime_list[-1]

def checkPrime(p):
    for prime in prime_list:
        if prime >= math.sqrt(p):
            return True
        else:
            if p % prime == 0:
                return False
    raise Exception("can not check")

def checkConcate(p1, p2):
    concat_1 = int(str(p1) + str(p2))
    concat_2 = int(str(p2) + str(p1))
    if math.sqrt(concat_1) > prime_list[-1] or math.sqrt(concat_2) > prime_list[-1]:
        print concat_1, concat_2
        raise Exception("not enough primes, cannot check!")

    if checkPrime(concat_1) and checkPrime(concat_2):
        return True
    else:
        return False

def findConcatPairs(p):
    buddys = []
    for prime in prime_list:
        if prime >= upper_bound:
            break
        if prime <= p:
            continue
        if checkConcate(p, prime):
            buddys.append(prime)
    return buddys

for i, p in enumerate(prime_list):
    if p >= upper_bound:
        break
    print str(i)+'/'+str(num_prime)
    prime_1_list = findConcatPairs(p)
    for p_1 in prime_1_list:
        prime_2_list = findConcatPairs(p_1)
        for p_2 in prime_2_list:
            if p_2 in prime_1_list:
                #print [p, p_1, p_2]
                prime_3_list = findConcatPairs(p_2)
                for p_3 in prime_3_list:
                    if p_3 in prime_1_list and p_3 in prime_2_list:
                        print [p, p_1, p_2, p_3]
                        prime_4_list = findConcatPairs(p_3)
                        for p_4 in prime_4_list:
                            if p_4 in prime_1_list and p_4 in prime_2_list and p_4 in prime_3_list:
                                print [p, p_1, p_2, p_3, p_4]
                                print p + p_1 + p_2 + p_3 + p_4
                                break
print "not found"
# [13, 5197, 5701, 6733, 8389]
#findConcatPairs(7)