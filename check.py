a = [[1,2,3,4], [5,6,7,8]]
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], '---', a[(i+1)%len(a)][j], 
                a[i][(j+1)%len(a[0])],
                a[(i+1)%len(a)][(j+1)%len(a[0])], 
                a[i-1][j], 
                a[i][j-1],
                a[i-1][j-1], 
                a[i-1][(j+1)%len(a[0])], 
                a[(i+1)%len(a)][j-1])