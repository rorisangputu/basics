def greet_user (first_name, last_name): #default args positions
    print(f"Hello {first_name} {last_name}!")
    print('Welcome aboard')

greet_user(last_name="Bumz", first_name="Mike") #specifying keyword instead of default args postion
#will get an error if one keyword is not specified

#Keyword args improved readability of code when dealing with numerical values
# eg total_cost(50, 5, 0.1) is not very clear
# total_cost(total=50, shipping=5, discount=0.1) very clear 