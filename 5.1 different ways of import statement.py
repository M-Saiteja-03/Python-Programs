#1
import sumofprimesinalist
a=[1,2,3,4,5]
a=sumofprimesinalist.sum_of_primes(a)
print(a)

#2
import sumofprimesinalist,module2
a=[1,2,3,4,5]
a=sumofprimesinalist.sum_of_primes(a)
print(a)
module2.div(10,20)

#3
import sumofprimesinalist as sop
b=[2,4,6,7,8,9,10]
b=sop.sum_of_primes(b)
print(b)

#4
import sumofprimesinalist as sop,module2 as m2
b=[2,4,6,7,8,9,10]
b=sop.sum_of_primes(b)
print(b)
m2.add(100,200)

#5
from sumofprimesinalist import diffrence
c=[1,2,3,4,5,6,7,8,9]
diffrence(c)

#6
from module2 import add,sub,mul
add(10,20)
sub(10,20)
mul(10,20)


#7
from module2 import div as d
d(10,20)

#8
from sumofprimesinalist import *
c=[1,2,3,4,5,6,7,8,9]
diffrence(c)
