import os
import psutil

def finding_primes(roof_num):
    """
    finds primes, return(?) as itarate
    """
    bool_list = [True]*roof_num #list of True, each boolian statement represents a number. So index+1=number
    bool_list[0] = False        # 1 is not a prime, so it is false
    for index, bool in enumerate(bool_list): 
        index += 1
        if bool == True:        #if it is True, the index will be a prime
            for index_multiple in range(index*index, roof_num+1, index):    #every multiple of that prime will turn into False
                bool_list[index_multiple-1] = False 
            yield (index) 
        else:
            pass

process = psutil.Process(os.getpid())

print(process.memory_info()[0] / float(2 ** 20))
a = 0
for prime in finding_primes(2000000):
    print(prime)
    a += prime
    #print(a)
print(a)
print(process.memory_info()[0] / float(2 ** 20))
