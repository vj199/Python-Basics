'''
Created on 26-Jan-2018

@author: Vijay
'''
x= input("Enter a string:\n")
if(x[::-1] == x):
    print("This string is palindrome")
else:
    print("This string is not palindrome")