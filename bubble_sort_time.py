import time
import random
from tqdm import tqdm
import inspect
from cProfile import Profile
from pstats import Stats
from sys import stdout as STDOUT

our_list = random.sample(range(0,1000),999)
msg = "Total time require {} for the function {:.3f}"

def bubble_sort(our_list):
    func_name = inspect.currentframe().f_code.co_name
    for i in tqdm(range(len(our_list))):
        for j in tqdm(range(len(our_list)-1)):
            if our_list[j] > our_list[j+1]:
                our_list[j], our_list[j+1] = our_list[j+1],our_list[j]
    print(func_name)
    
def bubble_sort_1(our_list):
    func_name = inspect.currentframe().f_code.co_name
    swap = True
    while(swap):
        swap = False
        for i in range(len(our_list)-1):
            if our_list[i] > our_list[i+1]:
                our_list[i], our_list[i+1] = our_list[i+1],our_list[i]
                swap = True  
    print(func_name)

# start_time = time.time()
# bubble_sort(our_list)
# end_time = time.time()
# total = end_time-start_time

start_time = time.time()
bubble_sort_1(our_list)
end_time = time.time()
total = end_time-start_time

# print(msg.format(bubble_sort.__name__,total))
print(msg.format(bubble_sort_1.__name__,total))

def call():
    return bubble_sort_1(our_list)

profiler = Profile()
profiler.runcall(call)
stats = Stats(profiler, stream=STDOUT)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
