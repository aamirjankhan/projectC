'''
Define a function CoordTransform() that transforms its first
two input parameters xVal and yVal into two output parameters
xValNew and yValNew. The function returns void.
The transformation is new = (old + 1) * 2. Ex: If xVal = 3 and yVal = 4,
then xValNew is 8 and yValNew is 10.



question number 2:
Implement the GuessNumber game. In this game,
the computer Think of a random number in the range 0-50.
(Hint: use the random module.)
Repeatedly prompt the user to guess the mystery number.
If the guess is correct, congratulate the user for winning.
If the guess is incorrect,
let the user know if the guess is too high or too low.
After 5 incorrect guesses,
tell the user the right answer.
'''
import random
arr=[]
for i in range(100):
    arr.append(i)
while True:
    answer=random.choice(arr)
    guess=int(input("enter your guess number between 0-100: "))
    if answer is guess:
        print("right guess\ncongratulations.....")
        print("the answer was: "+str(answer))
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
