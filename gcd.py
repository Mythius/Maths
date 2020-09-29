
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

def extended_gcd(a,b):
    g = a
    for c in b:
        g = gcd(g,c)
    return g
    
def lcm(a,b):
  return a * b / gcd(a,b)

def extended_lcm(a,b):
  g = a
  for c in b:
      g = lcm(g,c)
  return g

while True:
    try:
        args = []
        while True:
            try:
                args.append(int(input('Enter a number: ')))
            except:
                break
        print('LCM is: ',extended_lcm(args[0],args[1:]))
    except Exception as e:
        print(e)
        break


input('Click Enter to Exit')