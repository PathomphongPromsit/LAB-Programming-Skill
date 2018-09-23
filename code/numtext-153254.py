from __future__ import print_function
def split_poit(num_list):
	LN = len(num_list)
	if LN ==1:
		value = int(num_list[0])
		digit = 1
		num_to_text(int(value),digit)
	else:
		for i in range(LN-1):
			digit = LN-i
			if digit >2:
				value = num_list[i]
				num_to_text(int(value),digit)
			elif digit ==2:
				value = (int(num_list[i])*10) + int(num_list[i+1])
				num_to_text(int(value),digit)
		
	print()


def num_to_text(value,digit):
	word = ""
	if digit ==1 :  #one digit
		if value == 0:
			word ="zero"
		elif value == 1:
			word = "one"
		elif value == 2:
			word = "two"
		elif value == 3:
			word = "three"
		elif value == 4:
			word = "four"
		elif value == 5:
			word = "five"
		elif value == 6:
			word = "six"
		elif value == 7:
			word = "seven"
		elif value == 8:
			word = "eight"
		elif value == 9:
			word = "nine"

	elif digit == 2: #2digit
		digit2 = int(value/10)
		digit1 = value%10
		if value >=20:
			if digit2 ==2:
				word = "twenty"
			elif digit2 == 3:
				word = "thirty"
			elif digit2 == 4:
				word = "forty"
			elif digit2 == 5:
				word = "fifty"
			elif digit2 == 6:
				word = "sixty"
			elif digit2 == 7:
				word = "seventy"
			elif digit2 == 8:
				word = "eighty"
			elif digit2 == 9:
				word = "ninety"

			if digit1 == 1:
				word += "-one"
			elif digit1 == 2:
				word += "-two"
			elif digit1 == 3:
				word += "-three"
			elif digit1 == 4:
				word += "-four"
			elif digit1 == 5:
				word += "-five"
			elif digit1 == 6:
				word += "-six"
			elif digit1 == 7:
				word += "-seven"
			elif digit1 == 8:
				word += "-eight"
			elif digit1 == 9:
				word += "-nine"

			if digit2 == 0:
				if digit1 == 1:
					word += " one"
				elif digit1 == 2:
					word += " two"
				elif digit1 == 3:
					word += " three"
				elif digit1 == 4:
					word += " four"
				elif digit1 == 5:
					word += " five"
				elif digit1 == 6:
					word += " six"
				elif digit1 == 7:
					word += " seven"
				elif digit1 == 8:
					word += " eight"
				elif digit1 == 9:
					word += " nine"
				
		elif value <20:
			if value == 1:
				word = "one"
			elif value == 2:
				word = "two"
			elif value == 3:
				word = "three"
			elif value == 4:
				word = "four"
			elif value == 5:
				word = "five"
			elif value == 6:
				word = "six"
			elif value == 7:
				word = "seven"
			elif value == 8:
				word = "eight"
			elif value == 9:
				word = "nine"
			if value == 10:
				word = "ten"
			elif value == 11:
				word = "eleven"
			elif value == 12:
				word = "twelve"
			elif value == 13:
				word = "thirteen"
			elif value == 14:
				word = "fourteen"
			elif value == 15:
				word = "fifteen"
			elif value == 16:
				word = "sixteen"
			elif value == 17:
				word = "seventeen"
			elif value == 18:
				word = "eighteen"
			elif value == 19:
				word = "nineteen"
	
	elif digit > 2 :  # >99 
		
		if value == 1:
			word = "one"
		elif value == 2:
			word = "two"
		elif value == 3:
			word = "three"
		elif value == 4:
			word = "four"
		elif value == 5:
			word = "five"
		elif value == 6:
			word = "six"
		elif value == 7:
			word = "seven"
		elif value == 8:
			word = "eight"
		elif value == 9:
			word = "nine"
	
	if digit == 3 and value != 0:
		word += " hundred "
	elif digit == 4 and value != 0:
		word += " thousand "
	

	print(word, end='')


if __name__ == "__main__":
	n = int(input())
	for i in range(n):
		num = input()
		if num == "10000":
			word = "ten thousand"
			print(word)

		
		else:
			num_list = list(num)
			split_poit(num_list)

	
