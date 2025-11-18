##process that run in parallel 
#CPU bound tasks-tasks that are heavy on CPU usage (eg.mathematical computations,data processing)
#parallel execution so that i can use multiple cores of my cpu

import multiprocessing

import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'square:{i**2}')

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f'cube:{i**3}')

if __name__ =="__main__":

    #create 2 process 
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)
    t=time.time()

    p1.start()
    p2.start()

    #wait for the process to complete
    p1.join()
    p1.join()

    finsihed_time=time.time()-t
    print(finsihed_time)
