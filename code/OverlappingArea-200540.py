x_i, y_i, w_i, h_i = [int(i) for i in input().split()]
x_ii, y_ii, w_ii, h_ii = [int(i) for i in input().split()]

left  = (x_i-x_ii)
right = (x_ii+w_ii)-(x_i+w_i)

under  = (y_i-y_ii)
on = (y_ii+h_ii)-(y_i+h_i)

x_i_L = x_i
x_i_R = x_i+w_i
x_ii_L = x_ii
x_ii_R = x_ii+w_ii
y_i_U = y_i-h_i
y_i_O = y_i
y_ii_U = y_ii-h_ii
y_ii_O = y_ii



#print(left,right,under,on)
if ((x_i_L <= x_ii_L) and (x_i_R <= x_ii_L)) or ((x_ii_R <= x_i_L) and (x_ii_R <= x_i_R)):
	print("0")
elif ((y_i_O <= y_ii_U) and (y_i_U <= y_ii_U)) or ((y_ii_O <= y_i_U) and (y_ii_O <= y_i_O)):
	print("0")
else:
#x
	if left <= 0 and right <= 0: #in
		x =  w_ii
	elif left <= 0 and right > 0: #right
		x = w_i-abs(left)
	elif  left > 0 and right <=0: #left
		x = w_i - abs(right)
	elif left > 0 and right > 0: #wide
		x= w_i
	#y 
	if under <= 0 and on <= 0: #in
		y =  h_ii
	elif under <= 0 and on > 0: #on
		y = h_i-abs(under)
	elif  under > 0 and on <=0: #under
		y = h_i - abs(on)
	elif under > 0 and on > 0: #wide
		y = h_i
	#print(x,y)
	print(x*y)