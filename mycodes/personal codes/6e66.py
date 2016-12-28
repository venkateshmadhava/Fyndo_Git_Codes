import os
import random

board = ["-","-","-","-","-","-","-","-","-"]

u1 = ["0","0","0","0","0","0","0","0","0"]
u2 = ["0","0","0","0","0","0","0","0","0"]

print ("this is our board: " + '\n')
print (str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
print (str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
print (str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))

u1nm = input ("Enter user one name: ")
u2nm = input ("Enter user two name: ")
u1t = "1"
u2t = "0"

print ("The position legent is here:")
print ("0" + " | " + "1" + " | " + "2")
print ("3" + " | " + "4" + " | " + "5")
print ("6" + " | " + "7" + " | " + "8")

for i in range(9):
    if u1t == "1":
        turnu1 = input(u1nm + "'s turn:")
        turnu1 = int(turnu1)
        for j in range(30):
            if board[turnu1] == "X" or board[turnu1] == "O":
                turnu1 = input ("Position filled - enter again: ")
                turnu1 = int(turnu1)
                j=0
                
        u1[turnu1] = "1"
        board[turnu1] = "X"
        if u1[0] == "1" and u1[1] == "1" and u1[2] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u1[3] == "1" and u1[4] == "1" and u1[5] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u1[6] == "1" and u1[7] == "1" and u1[8] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u1[0] == "1" and u1[3] == "1" and u1[6] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u1[1] == "1" and u1[4] == "1" and u1[7] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u1[2] == "1" and u1[5] == "1" and u1[8] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u1[0] == "1" and u1[4] == "1" and u1[8] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u1[2] == "1" and u1[4] == "1" and u1[6] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        u1t = "0"
        u2t = "1"
            
    else:
        turnu2 = input(u2nm + "'s turn:")
        turnu2  = int(turnu2)
        for j in range(30):
            if board[turnu2] == "X" or board[turnu2] == "O":
                turnu2 = input ("Position filled - enter again: ")
                turnu2 = int(turnu2)
                j=0
                
        u2[turnu2] = "1"
        board[turnu2] = "O"
        if u2[0] == "1" and u2[1] == "1" and u2[2] == "1":
            print ("Game over: " + u2nm + " wins!")
            break          
        elif u2[3] == "1" and u2[4] == "1" and u2[5] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u2[6] == "1" and u2[7] == "1" and u2[8] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u2[0] == "1" and u2[3] == "1" and u2[6] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u2[1] == "1" and u2[4] == "1" and u2[7] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u2[2] == "1" and u2[5] == "1" and u2[8] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u2[0] == "1" and u2[4] == "1" and u2[8] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        elif u2[2] == "1" and u2[4] == "1" and u2[6] == "1":
            print ("Game over: " + u2nm + " wins!")
            break
        
        u2t = "0"
        u1t = "1"
        
    print (str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print (str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print (str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]) + '\n')


    print ("The position legent is here:")
    print ("0" + " | " + "1" + " | " + "2")
    print ("3" + " | " + "4" + " | " + "5")
    print ("6" + " | " + "7" + " | " + "8")

    

    

    


    
        
        
