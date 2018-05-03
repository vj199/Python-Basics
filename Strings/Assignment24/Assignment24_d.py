'''
Created on 26-Jan-2018

@author: Vijay
'''
x = ['!','(',')','@','#','$','%','^','&','*','<','>','?','/',':','_','[',']','{','}']
y = input("Enter a String")
#To take input from the user #
#remove punctuation#
a = ""
for z in y:
    if z not in x:
        a = a +z 
# display the unpunctuated string#
print(a)
