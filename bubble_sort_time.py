import time
import random

our_list = random.sample(range(0,100000),99999)
msg = "Total time require for the function {:.3f}"

def bubble_sort(our_list):
    for i in range(len(our_list)):
        for j in range(len(our_list)-1):
            if our_list[j] > our_list[j+1]:
                our_list[j], our_list[j+1] = our_list[j+1],our_list[j] 
    print(our_list) 

def bubble_sort_1(our_list):
    swap = True
    while(swap):
        swap = False
        for i in range(len(our_list)-1):
            if our_list[i] > our_list[i+1]:
                our_list[i], our_list[i+1] = our_list[i+1],our_list[i]
                swap = True  

start_time = time.time()
bubble_sort(our_list)
end_time = time.time()
total = end_time-start_time

print(msg.format(total))