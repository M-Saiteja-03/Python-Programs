d={}
for i in range(97,123):
    d[chr(i)]=0
for i in range(65,91):
    d[chr(i)]=0
d['\n']=0
print(d)
with open ("friends.txt","w") as f:
    f.write("Nikhil\nSai\nTeja")
with open ("friends.txt","r") as f:
    data=f.read()
    for i in data:
        d[i]+=1
    for k,v in d.items():
        if v==0:
            continue
        else:
            print(f"{str([k])}:{v}")

'''ALTERNATIVE METHOD
f=open("abc1.txt","r")
d=f.read()
print(d,end='')
f=open("abc1.txt","r")
k=f.read().split()
m=[]
for x in range(len(k)):
    for y in range(len((k[x]))):
         m.append(k[x][y])
mylist=[]
for x in m:
    if x not in mylist:
        mylist.append(x)
#print(mylist)
for x in mylist:
    num=d.count(x)
    print('character {} is {}'.format(x,num))'''



