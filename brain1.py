'''
Write a program that reads a sequence of up to 20 pairs of employee names
and IDs. Store the data in an object designed to store a first name (string),
last name (string), and an employee ID (integer).
Assume each line of input will contain two strings followed by an integer value, each separated by a tab character.
Then, after the input has been read in,
print the list in an appropriate format to the screen.
'''
class Solution:
    def __init__(self):
        self.firstName=""
        self.lastName=""
        self.employeeID=0
    def getData(self):
        self.firstName=input("please enter your first name: ")
        self.lastName=input("please enter your last name: ")
        self.employeeID=input("please enter your ID: ")
    def showData(self):
        p="{}\t{}\t{}".format(self.firstName,self.lastName,self.employeeID)
        return p

num=int(input("please enter the number of employee data you want to enter: "))
data=[]
for i in range(num):
    t1=Solution()
    t1.getData()
    data.append(t1.showData())
for i in data:
    print(i)
        
        
        
