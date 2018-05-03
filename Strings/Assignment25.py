'''
Created on 28-Jan-2018

@author: Vijay
'''
str = input("Enter a String:")
index = 0
y = ""
for x in str:
    if(index%2 == 0):
        y += x
    index += 1
print(y[::-1])