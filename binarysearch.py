import time
def binaryserch(indexingvalue,finding):
    startingtime=time.time()
    leftindex=0
    rightindex=len(indexingvalue)-1
    mindindex=0
   
    while leftindex<=rightindex:
       mindindex=(leftindex+rightindex)//2  #5+7  =12 // 6 
       minnumber=indexingvalue[mindindex]   #6 
       
       if minnumber==finding:
            endtime=time.time()
            print("ending time of this program "+str((endtime-startingtime)*1000) +"mil sec")
            return mindindex
       
       if minnumber<finding:
           leftindex= mindindex+1  #5
       else:
           rightindex=mindindex-1
    
    endtime=time.time()
    print("ending time of this program "+str((endtime-startingtime)*1000) +"mil sec")
    
if __name__=="__main__":
    indexingvalue=[1,3,4,6,7,98,100]
    finding=100
    index=binaryserch(indexingvalue,finding)
    print(f"this value is index of {index}")
    
    
    
    
        
        