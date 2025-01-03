#birth_year = input('Birth year? ') #input will always be string
#age = 2025 - birth_year #minusing int from string which creates error
#print(age) # error

#Correct code

birth_year = input('Birth year? ')
age = 2025 - int(birth_year)
age = str(age) # cannot print int so you have to convert to str
print('This year you are ' + age + ' years old') 