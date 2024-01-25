from numba import jit,cuda
import numpy as np
from timeit import default_timer as timer

def cpufunction(a):
    for i in range(150_000_000):
        a[i]+=1

@jit(target_backend='cuda')
def gpufunction(a):
    for i in range(150_000_000):
        a[i]+=1

if __name__ == '__main__':
    n = 150_000_000
    a = np.ones(n,dtype=np.float64)

    start = timer()
    cpufunction(a)
    print(f'czas wyskonania funkcji na CPU: {timer()-start} s')

    start = timer()
    gpufunction(a)
    print(f'czas wyskonania funkcji na GPU: {timer() - start} s')
