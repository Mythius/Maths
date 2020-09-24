def gcd(a,b):  
    if a == 0 : 
        return b  
    return gcd(b%a,a)

while True:
	try:
		n1 = int(input('Enter a number: '))
		n2 = int(input('Enter a number: '))
		print('GCD is: ',gcd(n1,n2))
	except Exception as e:
		print(e)
		break

input('Click Enter to Exit')