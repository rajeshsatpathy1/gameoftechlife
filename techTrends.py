#Reference for probability of countries underdeveloped, developing and developed countries
#https://www.un.org/en/development/desa/policy/wesp/wesp_current/2014wesp_country_classification.pdf

import random
from datetime import datetime
random.seed(datetime.now())


#create matrix of a size MxN
M = 10
N = 10
wMap = [[0] * M] * N

#-----Country Types-----
#0 - No country present in the cell
#1 - Underdeveloped Country, LDC and heavily indebted poor countries - Count 88
#2 - Developing Country, Economies in transition - Count 159
#3 - Developed Country - Count 37


#Probability of filling the wMap with countries
sumP = 88 + 159 + 37
pf1 = 88/sumP
pf2 = 159/sumP
pf3 = 37/sumP

CStatus = [(1, pf1), (2, pf2), (3, pf3)]

#Under the consideration that the use of technologies is based on availability of monetary resources
#We will assign the probability of a technology getting getting implemented in a country as:
#Developed > Developing > UnderDeveloped
p1 = 8
p2 = 6
p3 = 4

k = 0
#print(random.random() + random.choice(CStatus)[1])
#Creating the base set for countries
for i in range(len(wMap)):
    for j in range(len(wMap[0])):
        k = (random.randint(0,100)%10)%2
        if(random.random() + CStatus[k][1] > 0.9):
            wMap[i][j] = CStatus[k][0]
        else:
            wMap[i][j] = 0

for i in range(len(wMap)):
    for j in range(len(wMap[0])):
        print(wMap[i][j]," ",end = "")
    print("")

#Main Logic
#Replace 1 random of the elements as k
#Track the spread by number of iterations
