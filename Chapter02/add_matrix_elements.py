x = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
y = [[10, 11, 12],[13, 14, 15],[16, 17, 18]]
z = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for i in range(len(x)):
    for j in range (len(x[i])):
        z[i][j]=x[i][j]+y[i][j]
        print(z[i][j],end=' ')