'''
Created on 26-Jan-2018

@author: Vijay
'''
string1 = input("Enter a string")
count = 0;
c = ''
for x in string1:
    if(x.isupper()):
        count += 1
        c = c + x
print(count)
print(c)