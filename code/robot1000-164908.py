control = input()
#up = "N"
#down = "S"
#left = "W"
#right = "E"
#y = control.count('N')-control.count('S')
#x = control.count('E')-control.count('W')
#print("(%d,%d)" % (x, y))

x = 0
y = 0
for i in range(0,len(control)):
	#print (control[i])
	if control[i] == "N" :
		y += 1
	elif control[i] ==  "S" :
		y -= 1
	elif control[i] == "E" :
		x += 1
	elif control[i] == "W" :
		x -= 1
	elif control[i] == "Z" :
                x = 0
                y = 0
		# if x == 0 and y == 0 :
  #                       x = 0
  #                       y = 0                        
  #               elif x == 0 :
  #                       if y > 0:
  #                               y -= 1
  #                       elif y < 0:
  #                               y += 1
  #               elif y == 0:
  #                       if x > 0:
  #                               x -= 1
  #                       elif x < 0:
  #                               x +=1
  #               elif x > 0 and y > 0:
  #                       x -=1
  #                       y -=1
  #               elif x > 0 and y < 0:
  #                       x -=1
  #                       y +=1
  #               elif x < 0 and y > 0:
  #                       x +=1
  #                       y-=1
  #               elif x < 0 and y < 0:
  #                       x+=1
  #                       y+=1


		

print("%d %d" % (x, y))
