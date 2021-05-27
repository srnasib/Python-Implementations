import re
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
summation=0
handle = open(name)
fr= handle.read()
regex = '\d+'             
match = re.findall(regex, fr)     
print(match) 
for numbers in match :
 summation=summation+int(numbers)
print(summation) 
    
 


