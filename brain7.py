
import random
arr=[]
frr=open("score.txt","w")
for i in range(128):
    arr.append(i)
def func1(lst):
    score=0
    name=input("enter your name: ")
    while True:
        answer=random.choice(arr) 
        guess=int(input("enter your guess number between 0-128: "))
        if answer is guess:
            print("right guess\ncongratulations.....")
            print("the answer was: "+str(answer))
            score+=1
            break
        elif guess < answer-20:
            print("you guessed too low....\ntry again")
            print("the answer was: "+str(answer))
        elif guess > answer+20:
            print("you guessed too high....\ntry again")
            print("the answer was: "+str(answer))
        else:
            print("incorrect guess\ntry again")
            print("the answer was: "+str(answer))
        ext=int(input("press 0 to exit:\npress 1 to continue: "))
        if ext is 0:
            break
        
    return "{} {}".format(name,score)

num=int(input("how many users will be taking part: "))
for i in range(num):
    frr.write("{}\n".format(func1(arr)))
frr.close()

frr1=open("score.txt","r")
line=frr1.readline()
while line:
    print(line)
    line=frr1.readline()









frr1.close()


    
