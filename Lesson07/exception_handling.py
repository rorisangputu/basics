try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')


try:
    age = int(input("Age: "))
    income= 20000
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print('Age cannot zero (0)')
except ValueError:
    print('Invalid value')