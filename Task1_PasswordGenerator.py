import random, time
print("\n\n    ******   Welcome to Password Generator   ******     \n\n")
print("\n      Never again worry for a strong password!\n")
print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀             ⢀⡄⠀
 ⠀⠹⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⠏⠀⠀
⠀⠀⠀⠙⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⠋⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⣿⡉⠻⣷⣤⡀⠀⠀⢀⣴⣾⠟⢉⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣦⡈⠻⣿⣦⣀⠻⠟⢁⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡈⠻⣿⣷⣄⠙⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⣀⠙⢿⣿⣦⡈⠻⣿⣷⣄⠀⠀⠀⠀⢀⣄⠀⠀⠀⠀
⠀⠀⠀⠘⢿⣷⡄⠀⣠⣾⣿⠗⠀⠙⢿⣿⣦⡈⠻⣿⣷⣄⠀⢠⣾⡿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣾⣿⠟⢁⣴⣿⡷⠀⠙⢿⣿⣦⡈⠻⣿⣷⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣿⣿⣶⣿⡿⠋⠀⠀⠀⠀⠙⢿⣿⣶⣿⣿⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⠟⠉⠙⢿⣷⣄⡀⠀⠀⢀⣠⣾⡿⠋⠉⠻⣿⣆⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣾⠋⠀⠀⠀⠀⠀⠙⢿⡿⠂⠐⢿⡿⠋⠀⠀⠀⠀⠀⠙⣷⣦⡀⠀⠀
⠀⠸⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⠇⠀
""")
cr = int(input("\n\nEnter the number of characters you need in your password : "))
n = int(input("\nEnter the number of numbers you need in your password : "))
a = int(input("\nEnter the number of alphabets you need in your password : "))

car = []
num = []
alp = []

for i in range(33, 48):
    car.append(chr(i))

for i in range(60, 65):
    car.append(chr(i))

for i in range(94, 97):
    car.append(chr(i))

for i in range(123, 127):
    car.append(chr(i))

for i in range(65, 91):
    alp.append(chr(i))

for i in range(97, 123):
    alp.append(chr(i))

for i in range(48, 58):
    num.append(chr(i))


t = int(input( '\nEnter the number of passwords that you need(one or more than one): \n' ))
    

print(f"Your {t} passwords are : \n")    

while t != 0:
   passw = []
   ps = ""
   for i in range(0, cr):
      ind = random.randint(0, len(car)-1)
      passw.append(car[ind])
   for i in range(0, a):
      ind = random.randint( 0, len(alp)-1 )
      passw.append(alp[ind])
   for i in range(0, n):
      ind = random.randint(0, len(num)-1)
      passw.append(num[ind])


   for i in range( 0, len(passw) ):
      ind = random.randint( 0, len(passw)-1 )
      if i == 0:
         ps = passw[i] 
      else:
         ps = ps + passw[i]

   print(ps)    
   print("\n")  

   t = t-1                