'''
Write a function that takes a string and splits it up to an array of strings.
The split will be length-based:
the function will also take an integer n and will split the given string up into strings of length n.
It is possible that the last string will not be of length n. You will not need to communicate how large the resulting
array is as the calling function knows the string length and n.
'''
def func1(S , num):
    arr=[]
    i,j=0,num
    for k in range(int(len(S)/num)):
        arr.append(S[i:j])
        i+=num
        j+=num
    return arr
strr=input("please enter any string: ")
num=int(input("please enter the split number: "))
a=func1(strr,num)
print(a)        
