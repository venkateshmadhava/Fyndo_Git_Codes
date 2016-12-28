import os
import os.path

mnpath = input("Enter your path: ")

for root, dirs, files in os.walk(mnpath, topdown=False):
    for drname in dirs:
 
        tempath = mnpath + "/" + drname + "/"
        gallery = ""
        print (tempath)
        for root, dirs, files in os.walk(tempath, topdown=False):
            tmvar = 0
            count = 0
            newcount = 0
            print (drname)

            for namess in files:
                if namess.startswith("IMG_"):
                    #print ("loop 1 - checking IMG_")
                    newcount = newcount + 1
                    prv = tempath + namess
                    #print (prv)
                    tempname = tempath + "AA" + str(newcount) + ".jpg"
                    os.rename(prv,tempname)
                    print ("renamed")
                elif namess.startswith("_"):
                    #print ("loop 1 - checking IMG_")
                    newcount = newcount + 1
                    prv = tempath + namess
                   # print (prv)
                    tempname = tempath + "AA" + str(newcount) + ".jpg"
                    os.rename(prv,tempname)
                    print ("renamed")


 #          for namesss in files:
#                if namesss.startswith("IMG"):
#                    count = newcount + 1
#                    prv = tempath + namesss
#                    print (prv)
#                    tempname = tempath + "IMG" + str(count) + ".jpg"
#                    os.rename(prv,tempname)
#                    print ("renamed")
                        

   #         for namess in files:
#                print ("loop 3 - replacing NEW with IMG")
#                if namess.endswith(".jpg"):
#                    if namess.startswith("NEW"):
#                        namess.replace("NEW ","")
                        
 #                       count = newcount + 1
 #                       prv = tempath + "/" + namess
#                        print (prv)
#                        tempname = tempath + "/" + "IMG" + str(count) + ".jpg"
#                        os.rename(prv,tempname)



                
                

                    
        
                    
