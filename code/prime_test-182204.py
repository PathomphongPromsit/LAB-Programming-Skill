import math
data = int(input())
prime = 0
if data == 1 or data == 0:
        prime = 1
else:
        for x in range(2, int(math.sqrt(data)+1)):
                if (data % x == 0):
                        prime = 1
                        break
if prime == 1:
        print ("NO")
else:
        print ("YES")


            
                
