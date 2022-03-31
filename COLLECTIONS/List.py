word=[str(letter) for letter in input ("Enter word:").split()]
value=[int(num) for num in input("Enter value:").split()]
choice=int(input("1.Append \n2.Insert \n3.Extend \n4.Remove \n5.Pop \n6.Reverse \n7.Length \n8.Minimum \n9.Maximum \n10.Count \n11.Sort \n12.Index \n13.Datatype \n14.Concatenation \n15.Multiplication \nChoice:"))
if(choice==1):
	option=int(input("Select option to append:\n1.word\n2.value\nOption:"))
	if(option==1):
		a=str(input("Enter word to add in the back of the word list:"))
		word.append(a)
		print(word)
	elif(option==2):
		b=int(input("Enter value to add in the back of the values list:"))
		value.append(b)
		print(value)
	else:
		print("Invalid Input")
elif(choice==2):
	option=int(input("Select option to insert:\n1.word\n2.value\nOption:"))
	if(option==1):
		a=str(input("Enter word to be added:"))
		b=int(input("Enter position number to add the word:"))
		word.insert(b,a)
		print(word)
	elif(option==2):
		a=int(input("Enter value to be added:"))
		b=int(input("Enter position to add the value:"))
		value.insert(b,a)
		print(value)
	else:
		print("Invalid Input")
elif(choice==3):
	option=int(input("Select option to extend:\n1.word\n2.value\nOption:"))
	if(option==1):
		a=str(input("Enter word to extend in the word list:"))
		word.extend(a)
		print(word)
	elif(option==2):
		b=int(input("Enter value to extend in the the value list:"))
		value.extend(b)
		print(value)
	else:
		print("Invalid Input")
elif(choice==4):
	option=int(input("Select option to remove:\n1.word\n2.value\nOption:"))
	if(option==1):
		a=str(input("Enter word to remove in the word list:"))
		word.remove(a)
		print(word)
	elif(option==2):
		b=int(input("Enter value to remove in the the value list:"))
		value.remove(b)
		print(value)
	else:
		print("Invalid Input")
elif(choice==5):
	option=int(input("Select option to pop:\n1.word\n2.value\nOption:"))
	if(option==1):
		a=int(input("Enter position number to pop in the word list:"))
		word.pop(a)
		print(word)
	elif(option==2):
		b=int(input("Enter position number to pop in the value list:"))
		word.pop(b)
		print(value)
	else:
		print("Invalid Input")
elif(choice==6):
	word.reverse()
	print(word)
	value.reverse()
	print(value)
elif(choice==7):
	print(len(word))
	print(len(value))
elif(choice==8):
	print(min(value))
elif(choice==9):
	print(max(value))
elif(choice==10):
	option=int(input("Select option to count:\n1.word\n2.value\nOption:"))
	if(option==1):
		a=str(input("Enter word to count in the word list:"))
		print(word.count(a))
	elif(option==2):
		b=int(input("Enter value to count in the the value list:"))
		print(word.count(b))
	else:
		print("Invalid Input")
elif(choice==11):
	option=int(input("Select option to sort:\n1.word\n2.value\nOption:"))
	if(option==1):
		word.sort()
		print(word)
	elif(option==2):
		value.sort()
		print(value)
	else:
		print("Invalid Input")
elif(choice==12):
	option=int(input("Select option to index- to find the position:\n1.word\n2.value\nOption:"))
	if(option==1):
		a=str(input("Enter word to find the position in the word list:"))
		print(word.index(a))
	elif(option==2):
		b=int(input("Enter value to find the position in the the value list:"))
		print(value.index(b))
	else:
		print("Invalid Input")
elif(choice==13):
	print(type(word))
	print(type(value))
elif(choice==14):
	add=word+value
	print(add)
elif(choice==15):
	option=int(input("Select option to Multiply:\n1.word\n2.value\nOption:"))
	if(option==1):
		a=int(input("How many times you wish to display words in the name list:"))
		print(word*a)
	elif(option==2):
		b=int(input("How many times you wish to display value in the value list:"))
		print(value*b)
else:
	print("Invalid Input")
