#Reference for probability of countries underdeveloped, developing and developed countries
#https://www.un.org/en/development/desa/policy/wesp/wesp_current/2014wesp_country_classification.pdf

import random
from datetime import datetime
random.seed(datetime.now())


#create matrix of a size MxN
M = 10
N = 10
wMap = []
for i in range(M):
    wMap.append([0] * N)

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

print(pf1, pf2, pf3)

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
        if(random.random()*0.75 + CStatus[k][1] >= 1):
            wMap[i][j] = CStatus[k][0]
        else:
            wMap[i][j] = 0


print("The w Map of countries according to their status")
for i in range(len(wMap)):
    for j in range(len(wMap[0])):
        print(wMap[i][j]," ",end = "")
    print("")

#Main Logic
#Replace 1 random of the elements as k - where the technology starts
#Track the spread by number of iterations
timeUnit = int(input('Enter the number of iterations: '))

#Initiate technology in a random country 
def initiateTechnology():
    iRand = random.randint(0,9)
    jRand = random.randint(0,9)
    #print(iRand, jRand)
    while(wMap[iRand][jRand] == 0):
        iRand = random.randint(0,9)
        jRand = random.randint(0,9)

    #Initialise the technology
    print('The technology starts at cell: ',iRand, jRand)
    wMap[iRand][jRand] = 'k'

def printStatus():
    for i in range(len(wMap)):
        for j in range(len(wMap[0])):
            print(wMap[i][j]," ",end = "")
        print("")

#Start the game of technological trends spread
'''Rules:
    1. If the country is surrounded by a country that follows the technology 
    it has a probability pn to adopt that technology - Popularity. With every passing year of contact 
    with a technology the acception rate increases
    2. If the technology is in a country with no neighboring countries, it suffers from starvation of
    resources and technology stops getting adopted
    3. Every 5 time units a new technology starts in a random country
    Note: After a technology is in a country the coutry type is not under consideration
'''
initTechUnit = 0  #Time for a new Technology start
wMapTemp = wMap
randInt = 0

print('----Before----')
initiateTechnology()
printStatus()

for h in range(timeUnit):
    for i in range(M):
        for j in range(N):
            randInt = random.randint(2, 6)
            #Rule1:
            if(str(wMap[(i+1)%M][j]) == 'k' or str(wMap[i][(j+1)%N]) == 'k' or str(wMap[(i+1)%M][(j+1)%N]) == 'k' or str(wMap[i][j-1]) == 'k' or str(wMap[i-1][j]) == 'k' or str(wMap[i-1][j-1]) == 'k' or str(wMap[i-1][(j+1)%N]) == 'k' or str(wMap[(i+1)%M][j-1]) == 'k'):
                ele = wMap[i][j]
                if(ele == 1):
                    if(p1 + randInt >= 10):
                        wMap[i][j] = 'k'
                elif(ele == 2):
                    if(p2 + randInt >= 10):
                        wMap[i][j] = 'k'
                elif(ele == 3):
                    if(p3 + randInt >= 10):
                        wMap[i][j] = 'k'

            #Rule2:
            if(wMap[i][j] == 'k'):
                if(wMap[(i+1)%M][j] == 0 and wMap[i][(j+1)%N] == 0 and wMap[(i+1)%M][(j+1)%N] and wMap[i][j-1] == 0 and wMap[i-1][j] == 0 and wMap[i-1][(j+1)%N] == 0 and wMap[(i+1)%M][j-1] == 0):
                    wMap[i][j] == wMapTemp[i][j]

    #Rule3:
    if(initTechUnit < 5):
        initTechUnit +=1
    else:
        initiateTechnology()
        initTechUnit = 0
        print('Entered here')
    #print('----------------------------------------')
    #printStatus()
      
print('----After----')      
printStatus()


