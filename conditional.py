'''este programa te permite aplicar operaciones basicas de matematicas 
this script let you apply basic math operations as :
add, mult, subs and div.
el usuario debe igresar dos numeros 
the user must press two numbers 
2, the user must pres and optio from menu 
3, the fuction must apply the operation 
'''

import os 

def calc(x,y,z):
    if  z == 1 :
        Ans = x + y 
    elif  z == 2 :
        Ans  =x - y 
    elif  z == 3 :
        Ans  = x * y 
    elif  z == 4 :
        Ans = x / y 

    return Ans 


os.system("clear")
n1 = int (input("frist number:"))
n2 = int (input("secont number:"))
print("### menu ###")

print("[1]. add ")
print("[2]. div ")
print("[3]. div ")
print("[4]. div ")
opt = int (input("press an option"))

print ("the answer is", calc(n1,n2,opt))
 



