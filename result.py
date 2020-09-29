from sys import argv
from os import system,name
from time import sleep

script,filename=argv

def clear():
	print("loading......")
	sleep(2)
	if name=='nt':
		_ =system('cls')
	else:
		_=system('clear')


i=True
def class_l10(file,name1,Class,roll):
	maths=eval(input("Enter Marks of maths:  "))
	while maths>100 or maths=='':
		print("Marks cannot be greater than 100.Please input correct marks.")
		maths=eval(input("Enter Marks of maths:  "))
		pass
	science=eval(input("Enter Marks of science:  "))
	while science>100 or science=='':
		print("Marks cannot be greater than 100.Please input correct marks.")
		science=eval(input("Enter Marks of science:  "))
		pass
	Sscience=eval(input("Enter Marks of So.science:  "))
	while Sscience>100 or Sscience=='':
		print("Marks cannot be greater than 100.Please input correct marks.")
		Sscience=eval(input("Enter Marks of So.science:  "))
		pass
	sanskrit=eval(input("Enter Marks of sanskrit:  "))
	while sanskrit>100 or sanskrit=='':
		print("Marks cannot be greater than 100.Please input correct marks.")
		sanskrit=eval(input("Enter Marks of sanskrit:  "))
		pass
	hindi=eval(input("Enter Marks of hindi:  "))
	while hindi>100 or hindi=='':
		print("Marks cannot be greater than 100.Please input correct marks.")
		hindi=eval(input("Enter Marks of hindi:  "))
	english=eval(input("Enter Marks of english:  "))
	while english>100 or english=='':
		print("Marks cannot be greater than 100.Please input correct marks.")
		english=eval(input("Enter Marks of english:  "))
		pass
	
	total=maths+sanskrit+science+Sscience+hindi+english
	percent=total/6
	line1="Name     : %s \n"%name1
	line2="Class    : %d 'th \n"%Class
	line3="Roll No. : %d \n"%roll
	line4=("  __________________________________________________ \n" )
	line5= ("|                                                  |\n")
	line6= ("|	Science     : %d/100	                        \n"%science)
	line7= ("|	So.Science  : %d/100					        \n"%Sscience)
	line8= ("|	Maths       : %d/100					        \n"%maths)
	line9= ("|	Hindi       : %d/100				            \n"%hindi)
	line10=("|	English     : %d/100	                        \n"%english)
	line11=("|	Sanskrit    : %d/100			                \n"%sanskrit)
	line12=("|	Total	    : %d/600  Percent : %d    		  \n"%(total,percent))
	line13=("|__________________________________________________|\n")                                                              
	
	a=open(file,'w')
	a.truncate()
	a.write(line1)
	a.write(line2)
	a.write(line3)
	a.write(line4)
	a.write(line5)
	a.write(line6)
	a.write(line7)
	a.write(line8)
	a.write(line9)
	a.write(line10)
	a.write(line11)
	a.write(line12)
	a.write(line13)
	a.close()
	pass

i=True
while i:
	name1=input("Student name: ")
	Class=eval(input("Class: "))
	roll=eval(input("Roll no. : "))
	if Class<=10:

		class_l10(filename,name1,Class,roll)
	
	ok=True
	while ok:
		q=input("For correction press Y  and press q for quit: ")
		if q=='Y' or q=='y':
			i=True
			ok=False
			clear()
		elif q=='q' or q=='Q':
			i=False
			ok=False
		else :
			print ("Enter corre choice: ")
			ok=True

