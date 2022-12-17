dup_list=[1,1,22,24,5,22]
print(f'the duplicate list is {dup_list}')
uniqe_list=[]
for x in dup_list:
    if x not in uniqe_list:
        uniqe_list.append(x)

print(f' unique list is : {uniqe_list}')

#OR

'''l=[1,1,22,24,5,22]
print(list(set(l)))'''


        
    
