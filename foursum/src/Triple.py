from __future__ import print_function
import sys,random

def _main():
    N=int(10)
    if len(sys.argv) > 1:
        N=int(int(sys.argv[1])/2)
        
    M=int(10*N)

    L = triples(N,M)

    print(len(L))
    print(len(L),file=sys.stderr)
    #print(L)
    print('\n'.join(str(i) for i in L))

def triples(N,M, seed=None, shuffled=True,result=False):
    if seed != None:
        random.seed(seed)
    L=list(range(int(-M/2),int(-M/2+1))) + list( range(1,N)) + list(range(M-N,M-1))
    if result:
        i=random.randint(3,len(L)-1)
        j=random.randint(2,i-1)
        k=random.randint(1,j-1)
        l=random.randint(0,k-1)
        print(i,j,k,l)
        L[j] = - (L[i]+L[k]+L[l])
        
    if shuffled:
        random.shuffle(L)
    return L


if __name__ == '__main__':
    _main()

