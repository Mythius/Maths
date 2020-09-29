def gcd(a,b):
    if a == 0:
		print(a)
		return b
	return gcd(b%a,a)

def extended_gcd(a,b):
	g = a
	for c in b:
		try:
			g = gcd(g,c)
		except Exception as e:
			print(e)
	return g

while True:
	try:
		args = []
		while True:
			try:
				args.append(int(input('Enter a number: ')))
			except:
				break
		print('GCD is: ',extended_gcd(args[0],args[1:]))
	except Exception as e:
		print(e)
		break

input('Click Enter to Exit')