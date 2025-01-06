import converters
from converters import kg_to_lbs #ctrl + space


from utils import find_max

weight = int(kg_to_lbs(47))
print(weight)

numbers = [2, 32, 17, 28, 9, 8, 65, 45]
maxNum = find_max(numbers)
print(maxNum)
print(max(numbers)) ## does the same as top

