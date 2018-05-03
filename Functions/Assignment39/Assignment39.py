'''
Created on 14-Apr-2018

@author: Vijay
'''
def check_baggage(baggage_amount):
    if baggage_amount in range(0,40):
        return True
    else:
        return False
    
def check_immigration(year):
    if year in range(20001,2025):
        return True
    else:
        return False
    

def check_security(noc):
    return noc

def traveler():
    traveler_id = 1001
    traveler_name = "Jim"
    baggage_amount = 35
    year = 2019
    noc = True
    if check_baggage(baggage_amount) is True & check_immigration(year) is True & check_security(noc) is True:
        print(traveler_id,traveler_name,"\nAllowed to fly!\n")
    else:
        print(traveler_id,traveler_name,"\nDetain traveler for re-checking!\n")