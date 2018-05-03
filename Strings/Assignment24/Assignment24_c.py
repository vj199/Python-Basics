'''
Created on 26-Jan-2018

@author: Vijay
'''
x = ['a','e','i','o','u']
y =input("Enter a string")
count = 0
for i in y:
    for j in x:
        if(i == j):
            count += 1
print(count)
        