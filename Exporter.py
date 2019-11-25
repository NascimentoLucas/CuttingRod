from CutRod import cut_rod
from Methods.Data import Data


d = Data()
d.data_print_model()
ran = 1000000
time = 100
for i in range(ran):
    d.size = i + 1
    cut_rod(time, d)
    d.data_print()

