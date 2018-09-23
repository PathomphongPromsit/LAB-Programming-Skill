def binarySearchUp(data, key, P): 

        low = 0
        high = P
        while low <= high:

                mid = int((low+high)/2)
                if mid+1 ==P:
                        return mid
                elif data[mid] < key and key < data[mid+1]:
                        return mid
                elif data[mid] < key:
                        low = mid+1
                elif data[mid] > key:
                        high = mid-1
                elif data[mid] == key:
                        while data[mid] == key:
                                if mid+1 != P:
                                        mid = mid + 1
                                        
                                elif mid+1 == P:
                                        return (mid)
                        return (mid-1)



if __name__ == '__main__':
        Y, P = [int(i) for i in input().split()]

        data = [int(j) for j in input().split()]
        data.sort()
      
        
        countPope = 0
        Max_Pope = 0
        yStart= 0
        yStop=0
        
        for i in range (P):
                yT = (data[i]+Y)-1
                start = i
                stop = binarySearchUp(data, yT, P)
                
                countPope = (stop-start)+1
                #print("CP",countPope)
                
                if countPope>Max_Pope:
                        Max_Pope = countPope
                        yStart = data[start]
                        yStop = data[stop]




        print (Max_Pope, yStart, yStop)



