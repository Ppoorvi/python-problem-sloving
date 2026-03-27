#example1
math =50
chem = 50
phy = 50
english = 60
print(id(math))
print(id(chem))
print(id(phy))
print(id(english))


#example2
print(2+2)#4
print("2"+"2")#22
val1 = input("Enter first valve:")#2
val2 =input("Enter second value:")#2
print(val1+val2)#22


print(2+2)#4
print("2"+"2")#22
val1 = int(input("Enter first valve:"))#2
val2 =int(input("Enter second value:"))#2
print(val1+val2)#4


#example3
#int used to convert in integer

print(int(3.14))
#print(int(10+5j))
print(int(True)) #=1
print(int(False)) #=0
#print(int("4.22"))
print(int("4"))
print(int("vasu"))

#example4
#bool() is used to convert

print(bool(0))  #False
print(bool(15))  #True
print(bool(3.14))  #True
print(bool(0.0))  #False
print(bool(1+2j))  #True
print(bool(0+0j))  #False
print(bool(-1))  #True
print(bool(False))  #False
print(bool(True))  #True
print(bool(""))  


#example5
#decision making statement (conditional statement)

n=int(input("Enter any single digit :"))#5
if n>0:
  print("positive number")
if n<0:
  print("negative number")
if n==0:
  print("Zero")



#example6
#WAP to accept five number in 5 differnt variables and check max number and print

n1 = int(input("Enter value of n1:")) #
n2 = int(input("Enter value of n2:")) #
n3 = int(input("Enter value of n3:")) #
n4 = int(input("Enter value of n4:")) #
n5 = int(input("Enter value of n5:")) #

if n1>n2 and n1>n3 and n1>n4 and n1>n5:
  print("N1 is max value")
if n2>n1 and n2>n3 and n2>n4 and n2>n5:
  print("N2 is max value")
if n3>n1 and n3>n2 and n3>n4 and n3>n5:
  print("N3 is max value")
if n4>n1 and n4>n2 and n4>n3 and n4>n5:
  print("N4 is max value")
if n5>n1 and n5>n2 and n5>n3 and n5>n4:
  print("N5 is max value")


#example7
#WAP to accept three paper marks and calculate total percentage and if percentage is greater than or equal to the 

math = int(input("Enter marks of maths:"))
chem = int(input("Enter marks of chem:"))
phy = int(input("Enter marks of phy:"))
total = phy + chem + math
percentage = total/3.0
print("Total =",total)



#example8
#WAP to calculate simple interst
principle amount = 100000
roi              = 10
time             = 1

si = pa*roi*time/100
print("Simple interst =",si)


#example9


#WAP to enter height of user in feet and convert it onto inch and centimeter

height =float(input("Enter height in feet"))
inch = height*12
cm = inch *2.54
print("Inch",inch)
print("centimeter",cm)

#example10
#WAP to take centigrade temperature and convert it into Fahrenheit temperature










