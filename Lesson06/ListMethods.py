numbers = [5,2,3,2,1,7,2,5,8,4,2]

#numbers.append(20) #Append adds number to end of list
#print(numbers)

#numbers.insert(1, 4)#allows you to pic index of list where you want to add a new number
#print(numbers)

#numbers.pop(4) #removes the number at the 4th index
#print(numbers)

#numbers.sort() #Just sorts list
#print(numbers)
#numbers.reverse() 
#print(numbers)

#numbers2 = numbers.copy() #creates a copy of the list
#print(numbers.count(2)) #returns how many times the number appears in the list

##CHALLENGE - REMOVE DUPLICATES
unqiue = []
for number in numbers:
    if number not in unqiue:
        unqiue.append(number)

print(unqiue)