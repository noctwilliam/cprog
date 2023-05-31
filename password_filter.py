"""
Solutions devised by meself hihi
"""
import re
def password_filter(passwrd):
	acceptable = False
	# special_char = ['!','@','#','$','%','^','&','*','(',')','_','+','{','}','|',':','"','<','>','?','/','[',']',';',"'",',','.','~','`','\\','-','=']
	vowels = ['a','e','i','o','u']
	for i in passwrd:
		# Contain at least one vowel
		if i in vowels:
			acceptable = True
			break
	# Check whether contains numeric or not
	for i in passwrd:
		if i.isnumeric():
			acceptable = True
			break
		else:
			acceptable = False
	# Check whether contains at least one uppercase or not
	for i in passwrd:
		if i.isupper() or i.islower():
			acceptable = True
			break
	# Cannot contain three consecutive vowels
	if re.search(r'[aeiou]{3}',passwrd):
		acceptable = False
		# print(acceptable)
	# Cannot contain three consecutive consonants
	if re.search(r'[^aeiou]{3}',passwrd):
		acceptable = False
		# print(acceptable)
	if re.search(r'[ee]', passwrd) == False or re.search(r'[oo]',passwrd) == False:
		acceptable = False
		# print(acceptable)
	# print(acceptable)
	return acceptable

password_output = []
amt = int(input("Enter how many lines of password to be entered: "))
i = 0
while i < amt:
	passwrd = input("Enter password: ")
	if len(passwrd) < 1 or len(passwrd) > 20:
		print("Password must be between 1 and 20 characters")
		break
	if password_filter(passwrd):
		password_output.append(f"{passwrd} is acceptable")
	else:
		password_output.append(f"{passwrd} is unacceptable")
	i += 1

for i in password_output:
    print(i)