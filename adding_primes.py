import os
import psutil

def finding_primes(roof_num):
    bool_list = [True]*roof_num
    bool_list[0] = False
    for index, bool in enumerate(bool_list):
        index += 1
        if bool == True:
            for index_multiple in range(index*index, roof_num+1, index):
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
