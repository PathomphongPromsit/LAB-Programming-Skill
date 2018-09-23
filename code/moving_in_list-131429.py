

def A(st,nd):
	global head, tail, index_list

	start = index_list[st-1][1]-1   
	stop = index_list[nd-1][1]-1

	if index_list[start][2] != stop:

		#pop
		if start == head:
			index_list[index_list[start][2]][0] = None  #set None to head
			head = index_list[start][2]					#point new head
		elif start == tail:
			index_list[index_list[start][0]][2] = None  #set None to tail
			tail = index_list[start][0]					#point new tail
		else:
			start_preve = index_list[start][0]
			start_next = index_list[start][2]


			index_list[start_preve][2] = start_next		#start.preve.next = start.next
			index_list[start_next][0] = start_preve		#start.next.prev = start.prev

		# print("ST STO HE TA",start,stop,head,tail)

		#insert
		if stop == head:
			index_list[stop][0] = start		#stop prev = start
			index_list[start][2] = stop		#start next = stop
			index_list[start][0] = None		#new head = None
			head = start					#pointer to new head
		else:
			index_list[start][0] = index_list[stop][0]  # start.prev = stop.prev
			index_list[stop][0] = start 				#stop.prev = start
			index_list[index_list[start][0]][2] = start #start.prev.next = start
			index_list[start][2] = stop					#start.next = stop

def B(st,nd):
	global head, tail, index_list
	
	start = index_list[st-1][1]-1   
	stop = index_list[nd-1][1]-1

	if index_list[stop][2] != start:
		#pop
		if start == head:
			index_list[index_list[start][2]][0] = None  #set None to head
			head = index_list[start][2]					#point new head
		elif start == tail:
			index_list[index_list[start][0]][2] = None  #set None to tail
			tail = index_list[start][0]					#point new tail
		else:
			start_preve = index_list[start][0]
			start_next = index_list[start][2]


			index_list[start_preve][2] = start_next		#start.preve.next = start.next
			index_list[start_next][0] = start_preve		#start.next.prev = start.prev
		# print("ST STO HE TA",start,stop,head,tail)

		#insert
		if stop == tail:
			index_list[stop][2] = start 	#stop.next = start
			index_list[start][0] = stop		#start.prev = stop
			index_list[start][2] = None		#new tail = None
			tail = start 					#pointer to new tail
		else:
			index_list[start][2] = index_list[stop][2]  # start.next = stop.next
			index_list[stop][2] = start 				#stop.next = start
			index_list[index_list[start][2]][0] = start	#start.next.prev = start
			index_list[start][0] = stop					#start.prev = stop

#######################################################################################
if __name__ == "__main__":
	bogey, operand = [int(i) for i in input().split()]
	
	index_list=[]

	for i in range(1,bogey+1):  #buit train  {prev,value,next}
		if i == 1:
			index_list.append([None,i,i])
		elif i == (bogey):
			index_list.append([i-2,i,None])
		else:
			index_list.append([i-2,i,i])
	head = 0
	tail = bogey-1
	pop_index = 0
	for j in range(operand):
		O, start, stop = [k for k in input().split()] 
		#print (start,stop)
		start = int(start)
		stop = int(stop)
		
		if O == "A":
			A(start,stop)
			
		else:
			B(start,stop)

	current = head
	while current != None:

		a = index_list[current][1]
		print (int(a))
		current = index_list[current][2]

