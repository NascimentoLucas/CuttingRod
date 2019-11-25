import sys
import time
import random
from Methods.TopDown import cut_rod as top_down_cut
from Methods.BottomUp import cut_rod as bottom_up_cut


def test_methods(data):
    arr = []

    for j in range(data.size):
        arr.append(random.randint(1, 100))

    if data.debug:
        print('Size array: ' + str(data.size))
        print('Using array: ' + str(arr))

    start1 = time.time()
    top_down_cut(arr, data.size)
    end1 = time.time()
    data.time_top_down += end1 - start1

    start2 = time.time()
    bottom_up_cut(arr, data.size)
    end2 = time.time()
    data.time_bottom_up += end2 - start2


def cut_rod(times, data):
    data.time_top_down = 0
    data.time_bottom_up = 0

    if data.size < 100:
        sys.setrecursionlimit(100)
    else:
        sys.setrecursionlimit(data.size * 2)

    for i in range(times):
        test_methods(data)

    data.time_top_down /= times
    data.time_bottom_up /= times
