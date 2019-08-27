#developer juan argoti 
#randon 1  exercise 
import os 
from random import randint, uniform, random
## this fuction generate integer numbers 
def Z():
    ansZ = randint (0,100)
    return ansZ
##fucntion generate float numbers 

def R():
    ansR = uniform (0,100)
    return ansR
## main
os.system("clear")

print ("the integer random number is :",Z())

r= R()

print ("the float random numnber is ",r)