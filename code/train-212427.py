# import time

def tranfer(st,nd):
    #prev value next
    # 0    1     2
    #I_Head/ I_Tail/ II_Head/ II_Tail/ III_Head/ III_Tail
    # a       b       c        d        e         f
    #[[  ]  , [ ]], [[ ]], [ [] ]   
    #left     right  all    mid
    global index_list,head,tail

    #index start stop
    start = index_list[st-1][1]-1   
    stop = index_list[nd-1][1]-1
    #print(start,stop)

    #     head = self.head
    #     tail = self.tail
    #     #print(start.value,stop.value)

    if start == head and stop != tail: #left

        #[1][2] to [2][1]
        #self.head =stop.next  #point new head
        head = index_list[stop][2]  #point new head
        #stop.next.prev = None #set prev head = none
        index_list[index_list[stop][2]][0] = None


        #start.prev = tail
        index_list[start][0] = tail
        #tail.next = start
        index_list[tail][2] = start

        #stop.next = None
        index_list[stop][2] = None
        #self.tail = stop
        tail = stop

    elif start != head and stop != tail: # mid
        #[1][2][3] to [1][3][2]
        #prev_start = start.prev
        prev_start = index_list[start][0]
        #next_stop = stop.next
        next_stop = index_list[stop][2]

        #prev_start.next = next_stop #joint [3] to [1]
        index_list[prev_start][2] = next_stop
        #next_stop.prev = prev_start
        index_list[next_stop][0] = prev_start

        #tail.next = start
        index_list[tail][2] = start
        #start.prev = tail               #joint [2] to [3]
        index_list[start][0] = tail

        #stop.next = None                #tail close [2]
        index_list[stop][2] = None
        #self.tail = stop
        tail = stop



if __name__ == "__main__":
    
    bogey, operand = [int(i) for i in input().split()]
    
    index_list = []
    
    for i in range(1,bogey+1):  #buit train  {prev,value,next}
        if i == 1:
            index_list.append([None,i,i])
        elif i == (bogey):
            index_list.append([i-2,i,None])
        else:
            index_list.append([i-2,i,i])
    #print(index_list)

    head = 0
    tail = bogey-1
    
    for j in range(operand):
      start, stop = [int(l) for l in input().split()] 
      # if j == operand-1:
      #   t0 = time.time()
      tranfer(start,stop)
    

    current = head
    #print("CUR",current)
    #print("GGWP")
    while current != None:
        #print("GG")
        a = index_list[current][1]
        print (int(a))
        current = index_list[current][2]
    # print(time.time() - t0)