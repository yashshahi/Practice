#multithreading 
#when to use 
#I/O -bound task:tasks that spend mpore time waiting for I/O operations 
#concurent execution

import threading 
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'Number:{i}')

def print_letter():
    for letter in 'abcde':
        time.sleep(2) #makes the function sleep for 2 secs before its runs again 
        print(f'Letter: {letter}')

#creating 2 thread(part 2 "you can remove the code in this section and still run fine ")
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)


t=time.time()
#start the thread 
t1.start()
t2.start()
''' when one of thread sleeps other thread will concurrently will be executed'''
#wait for the threads to complete
t1.join() #.join() waits for the thread to complete
t2.join()
# print_numbers()
# print_letter() these 2 lines wwill be used when the 2 threads for not created
finished_time=time.time()-t
print(finished_time)

#the time taken in this operation will be half as we are using 2 threads
