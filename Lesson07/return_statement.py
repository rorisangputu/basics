def calc_cost(total, discount):
    calc = total * discount
    price = total - calc / 100 
    return price

prod_total = input("Total: ")
sale_discount = input("Discount %: ")
discounted_price = calc_cost(int(prod_total),int(sale_discount))
print(discounted_price)
