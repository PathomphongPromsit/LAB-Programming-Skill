from __future__ import print_function
def num_to_roman_split(data):
	LD = len(data)
	for i in range(LD):
		digit = LD - i
		num_to_roman(int(data[i]),digit)

def num_to_roman(value,digit):
	global ggwp

	if digit == 4:
		ggwp.extend('M'*value)
	elif digit == 3:
		
		if value == 1:
			ggwp.extend('C')
		elif value == 2:
			ggwp.extend('CC')
		elif value == 3:
			ggwp.extend('CCC')
		elif value == 4:
			ggwp.extend('CD')
		elif value == 5:
			ggwp.extend('D')
		elif value == 6:
			ggwp.extend('DC')
		elif value == 7:
			ggwp.extend('DCC')
		elif value == 8:
			ggwp.extend('DCCC')
		elif value == 9:
			ggwp.extend('CM')

	elif digit == 2:
		
		if value == 1:
			ggwp.extend('X')
		elif value == 2:
			ggwp.extend('XX')
		elif value == 3:
			ggwp.extend('XXX')
		elif value == 4:
			ggwp.extend('XL')
		elif value == 5:
			ggwp.extend('L')
		elif value == 6:
			ggwp.extend('LX')
		elif value == 7:
			ggwp.extend('LXX')
		elif value == 8:
			ggwp.extend('LXXX')
		elif value == 9:
			ggwp.extend('XC')
		
	elif digit == 1:
		
		if value == 1:
			ggwp.extend('I')
		elif value == 2:
			ggwp.extend('II')
		elif value == 3:
			ggwp.extend('III')
		elif value == 4:
			ggwp.extend('IV')
		elif value == 5:
			ggwp.extend('V')
		elif value == 6:
			ggwp.extend('VI')
		elif value == 7:
			ggwp.extend('VII')
		elif value == 8:
			ggwp.extend('VIII')
		elif value == 9:
			ggwp.extend('IX')
	
	


if __name__ == "__main__":
	ggwp=[]
	data = input()
	num_to_roman_split(data)
	for i in range(len(ggwp)):
		print(ggwp[i], end='')

