import random
from datetime import datetime
random.seed(datetime.now())

M = 10
N = 10
wMap = [[0] * M] * N
print(wMap)
wMap[1][2] = 'a'
print('-----------')
print(wMap)