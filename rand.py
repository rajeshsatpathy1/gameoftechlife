import random
from datetime import datetime
random.seed(datetime.now())

for i in range(10):
    k = random.randint(0,2)
    print(k)