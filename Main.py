import sys
import time
import random
from TopDown import cut_rod as top_down_cut
from BottomUp import cut_rod as bottom_up_cut


time_top_down = 0
time_bottom_up = 0
result_top_down = 0
result_bottom_up = 0

r = 10
size = 10
sys.setrecursionlimit(size * 2)
for i in range(r):
    arr = []

    for j in range(size):
        arr.append(random.randint(1, 100))

    start1 = time.time()
    result_top_down = top_down_cut(arr, size)
    end1 = time.time()
    time_top_down += end1 - start1

    start2 = time.time()
    result_bottom_up = bottom_up_cut(arr, size)
    end2 = time.time()
    time_bottom_up += end2 - start2

time_top_down /= r
time_bottom_up /= r

print('TopDown : BottomUp')
print('Result: ')
print(str(result_top_down) + ' : ' + str(result_bottom_up))
print('Time: ')
print(str(time_top_down) + ' : ' + str(time_bottom_up))

if time_bottom_up > 0:
    average = time_top_down / time_bottom_up
else:
    average = 0
print('(time_top_down / time_bottom_up) => ' + str(average))
