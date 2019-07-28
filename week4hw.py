#!/usr/bin/python

##CEBD1160 week4 homework by Zele Yu

###Basic:
##1. 

def removeduplicates(l):
    rel = []
    for k in l:
        if k not in rel:
            rel.append(k)
    return rel


l = [2,4,4,5,7,7,7,7,3,1,5]
print(removeduplicates(l))

##2. 

def insidelist(l,n):
    if n in l :
        return True
    else:
        return False


l = [1,4,5,7,8,9,23,34,45]
n1 = 9
n2 = 11

print(insidelist(l,n1))
print(insidelist(l,n2))

##3. 

a = [1,4,9,16,25,36,49,64,81,100]
b = [i for i in a if i%2 == 0]
print(b)

###Advanced:
##1. 
import random

r = int(input("Enter the range, larger than 0: "))

number = random.randrange(r)

guess = -1

def bingo(number,guess):
    if number == guess:
        return "bingo"
    elif (number-5)<=guess<=(number+5):
        return "close"
    elif (guess+50)<number:
        return "way lower"
    elif guess<number:
        return "lower"
    elif (guess-50)>number:
        return "way upper"
    elif guess>number:
        return "upper"

def untillbingo(number,guess):
    count = 0
    while number != guess :
        count = count + 1
        print("The guess No.",count)
        guess = int(input("Enter your guess: "))
        print(bingo(number,guess))

untillbingo(number,guess)

##2.

my = int(input("Enter a number between 0 to 200: "))

def guessmy(my):
    ng = 100
    while (ng != my) and (ng in range(0,201)):
        print("the program's guess is ",ng)
        resp = input("Enter your response (way upper, upper,lower, way lower or bingo): ")
        if resp == "bingo":
            return "the game is finished."
        elif resp == "way lower":
            ng = ng + 10
        elif resp == "lower":
            ng = ng + 1
        elif resp == "upper":
            ng = ng - 1
        elif resp == "way upper":
            ng = ng - 10
    
    return "Bingo! The program's guess is "+str(ng)

guessmy(my)

##3.

import random

r = int(input("Enter the range, larger than 0: "))

number = random.randrange(r)

guess = -1

def trybingo(number,guess):
    if number == guess:
        return "bingo"
    elif (number-5)<=guess<=(number+5):
        print("close")
    elif (guess+50)<number:
        print("way lower")
    elif guess<number:
        print("lower")
    elif (guess-50)>number:
        print("way upper")
    elif guess>number:
        print("upper")

    if number%2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
    if number%3 == 0:
        print("The number is divisible by 3.")
    else:
        print("The number is not divisible by 3.")
    return

def lessbingo(number,guess):
    count = 0
    while number != guess :
        count = count + 1
        print("The guess No.",count)
        guess = int(input("Enter your guess: "))
        trybingo(number,guess)
    return "bingo"

lessbingo(number,guess)

##4.

me = int(input("Enter a number between 0 to 200: "))

def guessme(me):
    check = input("Is the number odd or even? ")
    ng = 0
    if check == "even":
        ng = 100
    elif check == "odd":
        ng = 101

    while (ng != me) and (ng in range(0,201)):
        print("the program's guess is ",ng)
        resp = input("Enter your response (way upper, upper,lower, way lower or bingo): ")
        if resp == "bingo":
            return "the game is finished."
        elif resp == "way lower":
            ng = ng + 10
        elif resp == "lower":
            ng = ng + 2
        elif resp == "upper":
            ng = ng - 2
        elif resp == "way upper":
            ng = ng - 10
    
    return "Bingo! The program's guess is "+str(ng)

guessme(me)
