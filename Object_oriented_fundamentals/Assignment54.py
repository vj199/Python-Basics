'''
Created on 19-Apr-2018

@author: Vijay
'''
class PrintDetails:
    def printheader(self, c='*', no=1):
        print(c * no) 
        
obj = PrintDetails()    
obj.printheader('#', 10)
obj.printheader("Report")
obj.printheader('#' ,10)
obj.printheader()