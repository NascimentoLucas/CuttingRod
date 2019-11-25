from CutRod import cut_rod
from Methods.Data import Data
import random


d = Data()
d.debug = True
d.size = random.randint(10, 30)

cut_rod(1, d)

print('TopDown')
print('  Time: ' + str(d.time_top_down))

print('BottomUp')
print('  Time: ' + str(d.time_bottom_up))
