'''
Created on 23-Mar-2018

@author: Vijay
'''
string1 ="abcdg"
string2 = "bcsd"
string = string1 + string2
output = ""

for i in string:
    if i.isupper():
        output += i[0]
    string.split()
print("merged_string:",output)