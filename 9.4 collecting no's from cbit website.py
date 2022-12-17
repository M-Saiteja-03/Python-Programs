import re
import urllib.request
u=urllib.request.urlopen("https://www.cbit.ac.in/")
text=u.read()
numbers=re.findall("[0-9*]{8}[0-9]+",str(text),re.I)
for n in numbers:
    print(n)