# Create text file which contains all your friends names, display the count
# of each alphabet present in file
#
#                ex:        chaitanya
#
#                               c-1, h-1,a-3,i-1,t-1,n-1,y-1
f=open("lab_internal_2.txt","w")
f.write("Marepally Saiteja\nKumar teja\nNikhil Krishna")
f.close()
def count_letters(text):
    result={}
    for letter in text:

        if letter not in result:
            result[letter]=0
        result[letter]+=1
    return result

f=open("lab_internal_2.txt",'r')
for i in f:
    s=i[:len(i)+1]
    print(s,':',count_letters(s))
f.close()