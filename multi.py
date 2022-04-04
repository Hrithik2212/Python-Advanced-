
from multiprocessing import Process
import os 
import time

def sqaure_numbers():
    for i in range(100):
        print(i*i,end=" ")
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()
# print(num_processes)

#create processes
for i in range(num_processes):
    p=Process(target=sqaure_numbers)
    processes.append(p)

if __name__=='__main__':
#start 
    for p in processes:
        p.start()

#join
    for p in processes:
        p.join()

    print("end main")    