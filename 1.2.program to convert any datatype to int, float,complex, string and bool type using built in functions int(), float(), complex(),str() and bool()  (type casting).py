print('''converting different data types into int''')
a=int(10.33)
print("float to int:",a)
print("str can't be converted into int data type")
a=int(True)
print('bool to int:',a)
print("complex can't be converted into int data type")
print('\n')
print('''converting different data types into float''')
a=float(10)
print("int to float:",a)
print("str can't be converted into float data type")
a=float(True)
print('bool to float:',a)
print("complex can't be converted into float data type")
print('\n')
print('''converting different data types into str''')
a=str(10)
print("int to str:",a)
a=str(10.33)
print('float to str:',a)
a=str(True)
print('bool to str:',a)
a=str(2+3j)
print('complex to str:',a)
print('\n')
print('''converting different data types into complex''')
a=complex(10)
print("int to complex:",a)
a=complex(10.33)
print('float to complex:',a)
a=complex(True)
print('bool to complex:',a)
print('str cant be converted to complex:')
print('\n')
print('''converting different data types into bool''')
a=bool(10)
print("int to bool:",a)
a=bool(10.33)
print('float to bool:',a)
a=bool(2+3j)
print('complex to bool:',a)
a=bool('CBIT')
print('str to bool:',a)
print('\n')

