from TopDown import cut_rod
from BottomUp import cut_rod
import time


arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)

start = time.time()
result = cut_rod(arr, size)
time_top_down = time.time() - start
print('TopDown')
print('  Result: ' + str(result))
print('  Time: ' + str(time_top_down))

start = time.time()
result = cut_rod(arr, size)
time_bottom_up = time.time() - start
print('BottomUp')
print('  Result: ' + str(result))
print('  Time: ' + str(time_bottom_up))
