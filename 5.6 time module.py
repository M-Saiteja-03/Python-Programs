#1
import time
currenttime=time.asctime(time.localtime(time.time()))
print(currenttime)

'''seconds = time.time()
print("Seconds since epoch =", seconds)'''

#2
print(time.ctime(time.time()))

#3
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%d-%m-%Y, %H:%M:%S", named_tuple)
print(time_string)

'''print("next statment will print after 10 secs")
print('your time starts now')
time.sleep(10)
print("10 secs over")
print("your time is completed")'''

