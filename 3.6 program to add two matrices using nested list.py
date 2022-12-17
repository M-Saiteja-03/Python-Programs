l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]]
l3=[[0,0,0],[0,0,0],[0,0,0]]


for x in range(len(l1)):
    for i in range(len(l1[0])):
        l3[x][i]=l1[x][i]+l2[x][i]

for x in l3:
    print(x)


