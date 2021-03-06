from algs4.stdlib.stdrandom import uniformInt,shuffle
from algs4.stdlib.stdstats import mean,stddev
#from algs4.stdlib.stdio import eprint
from random import randint 

import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class RandomQueue:
    q = []
    q_size = 0

    def __init__(self):
        None

    def isEmpty(self):
        return (not bool(self.q_size))
        
    def size(self):
        return self.q_size
        
    def __len__(self):
        return self.size()
        
    def enqueue(self,item):
        
        # Below block handles resizing of the 'array', by implementing the dynamic array 
        # data structure. If the array is full before an enqueue, an array of double the 
        # size is initialized and populated with the items of the current queue.  

        if self.q_size == len(self.q):
            if self.size() != 0: temporaryQueue = [None for x in range(self.size()*2)]
            else: temporaryQueue = [None]

            for i in range(self.size()):
                temporaryQueue[i], self.q[i] = self.q[i], temporaryQueue[i]
            temporaryQueue, self.q = self.q, temporaryQueue

        self.q[self.size()] = item
        self.q_size += 1 
        
    def sample(self):
        if self.isEmpty():
            return NotImplementedError 

        return(self.q[randint(0, self.q_size-1)]) 

    def dequeue(self):
        if self.isEmpty():
            return NotImplementedError 

        # The below block handle the down-sizing of the dynamic array.
        # If the number of items in the queue falls below 1/4 the size
        # of the array, the size of the array is halved. 

        if self.q_size <= len(self.q)*0.25:
            temporaryQueue = [None for x in range(int(len(self.q)*0.5))]

            for i in range(self.size()):
                temporaryQueue[i] = self.q[i]
            self.q = temporaryQueue

        # When a random element is dequeued (and thus removed), the
        # last item in the queue 'fills its spot' in the array, such
        # that all items in the queue are positioned in the first 
        # part of the array. 

        random_idx = randint(0, self.q_size-1)
        return_value = self.q[random_idx]
        self.q[random_idx] = self.q[self.q_size-1]
        self.q[self.q_size-1] = None
        self.q_size -= 1
        return return_value

    def __iter__(self):
        # Init array of size of queue
        # O(N)
        mine = [None for i in range(self.size())]

        # Populate array with values of queue
        # O(N)
        for i in range(self.size()):
            mine[i] = self.q[i]
        
        # Knuth shuffle 
        # O(N)
        for i in range(self.size()-2):
            j = i + randint(0,self.size()-(i+1))
            mine[i], mine[j] = mine[j], mine[i] 

        for x in mine:  
            yield x


# This  "main method" tests your implementation. Do not change it.
if __name__ == '__main__':
    Q = RandomQueue()
    # build a randomQueue with 1,2,..,6
    for i in range(1,7):
        Q.enqueue(i)
        
    # print 30 die rolls
    eprint( ' '.join([str(Q.sample()) for i in range(30) ] ) )

    # Let's be more serious: do they really behave like die rolls?
    rolls = [ Q.sample() for i in range(1000) ]
    eprint("Mean (should be around 3.5): {:5.4f}".format(mean(rolls)))
    eprint("Standard deviation (should be around 1.7): {:5.4f}".format(stddev(rolls)))

    # removing 3 random values
    eprint( "Removing {}".format(' '.join( [str(Q.dequeue()) for i in range(3) ] ) ) )
    
    #Add 7,8,9
    for i in range(7,10):
        Q.enqueue(i); 
    # Empty the queue in random order
    while not Q.isEmpty():
        eprint(Q.dequeue(),end=' ');
    eprint()

    # Let s look at the iterator. First, we make a queue of colours:
    C= RandomQueue()
    C.enqueue("red"); C.enqueue("blue"); C.enqueue("green"); C.enqueue("yellow"); 

    I = iter(C)
    J = iter(C)

    eprint("Two colours from first shuffle: {} {}".format(next(I),next(I)))
    
    eprint("Entire second shuffle: {}".format(' '.join([i for i in J])));

    eprint("Remaining two colours from first shuffle: {} {}".format(next(I),next(I)))

    # for i in range(3):
    #     eprint(list( Q))
    # for i in range(6):
    #     eprint(Q.dequeue())
    

