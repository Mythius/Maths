def lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

while True:
  num1 = int(input('Enter a number: '))
  num2 = int(input('Enter a number: '))
  print(lcm(num1,num2))