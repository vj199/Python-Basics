'''
Created on 23-Mar-2018

@author: Vijay
'''
def Compare(phoenix_to_slc,phoenix_to_tapma):
    if phoenix_to_slc > phoenix_to_tapma:
        print("SLC is far from phoenix compare to tapma, florida")
    elif(phoenix_to_slc<phoenix_to_tapma):
        print("tapma, florida is far from phoenix compared to slc")
    else:
        print("Both locations are equi distance from phoenix")
        

Compare(1790,506)