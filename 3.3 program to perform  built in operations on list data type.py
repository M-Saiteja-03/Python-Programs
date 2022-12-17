list=[1,23.556,'hello',22,3]#-->list is acontainer to store a set of values of any datatype
print(list)
list.append(33)#-->two values can't be appended at one time.They have to be appended using one more append function
#list.sort()#-->sorts the list in ascending order,It is not compatible if both string and real numbers are present
list.reverse()#-->reverses the order of the list
list.insert(3,'world')#inserts the value that we want at the particular index of the list
list.pop(2)#-->pops out the value at the particular index mentioned(here 2nd index)
list.remove(23.556)#-->removes the particular value entered in the list
x=list.count(23.556)#-->counts the no.of times the element is repeated in the list and returns the value
print(x)
#list.clear()#-->clears the entire list
print(list)

