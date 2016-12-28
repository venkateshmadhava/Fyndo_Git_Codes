import os
import os.path

mnpath = input("Enter your path: ")

for root, dirs, files in os.walk(mnpath, topdown=True):
    for drname in dirs:
 
        tempath = mnpath + drname + "/"
        gallery = ""
        #print (tempath)
        for root, dirs, files in os.walk(tempath, topdown=True):
            tmvar = 0
            count = 0
            #print (drname)

            for namess in files:
                if namess.endswith(".jpg") or namess.endswith(".JPG"):
                    count = count + 1
 #                   gallery = gallery + "http://www.pinehill.co.in/media/import/" + drname + "/" + namess

          
            for namess in files:
                if namess.endswith(".jpg") or namess.endswith(".JPG"):
                    tmvar = tmvar + 1
                    
                
                if namess.endswith(".jpg") or namess.endswith(".JPG"):

                    
                    if tmvar == count:
                        gallery = gallery + "http://www.pinehill.co.in/media/import/" + drname + "/" + namess
#                        gallery = gallery + "http://www.pinehill.co.in/media/baseimage/" + drname + "/" + namess
                        #print ("last one")
                        #print (tmvar)
 
                    else:
                        gallery = gallery + "http://www.pinehill.co.in/media/import/" + drname + "/" + namess + ","
#                        gallery = gallery + "http://www.pinehill.co.in/media/baseimage/" + drname + "/" + namess
                        #print ("general loop")
                        #print (tmvar)
                    
                        
        #print (count)
        #print (tmvar)
        print (drname + " xxxx " + gallery)
