tobase = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

def numToBase(i,base=10):
	if base > 16:
		raise Exception('Error: Base 16 is the Maximum allowed base\n')
	if i < 0 or base < 0:
		raise Exception('Error: No Negative Numbers permitted\n')
	d = 0
	m = 0
	result = ""
	while True:
		d = i // base # Integer Division
		m = i % base # Modulus
		result = tobase[m] + result # The modulus gets appended to beginning of Result
		i = d #
		if i == 0:
			break
	return result

while True:
	try:
		num = int(input('Enter num: '))
		# base = int(input('Enter base: '))
		try:
			print('Result in base 2: '+numToBase(num,2))
			print('Result in base 8: '+numToBase(num,8))
			print('Result in base 16: '+numToBase(num,16))
			# print('Result: '+numToBase(num,base))
			print()
		except Exception as e:
			print(e)
	except Exception as e:
		break

input('Click Enter to Exit')