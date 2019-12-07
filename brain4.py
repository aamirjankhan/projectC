'''
BlockPy: #38.2) While Input Use a while loop to repeatedly take input
from the user and print whatever they type in.
When the user enters the empty string (""),
then your program should stop. Note that if your program
accidentally loops forever, your browser may become
unresponsive for up to 15 seconds.
Be very careful while writing while loops!
'''
strr=input("please enter something: ")
while strr is not "":
    print(strr)
    strr=input("please enter something: ")
