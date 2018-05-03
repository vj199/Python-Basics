'''
Created on 26-Jan-2018

@author: Vijay
'''
bill_id = input("Please Enter Bill id")
customer_id = input("\nPlease Enter customer id") 
bill_amount = input("\nPlease Enter bill Amount")
customer_name = input("\nPlease enter customer name")
if ((len(customer_name) >=3) and(len(customer_name) <= 20)) is True:
    print("Bill id:",bill_id)
    print("Customer Id:",customer_id)
    print("Bill Amount:Rs.",bill_amount)
    print("Customer Name:",customer_name)
else:
    print("Invalid customer name. Customer name must be between 3 and 20 characters");