def find_max(numbers):
    maxNum = numbers[0]
    for number in numbers:
        if number > maxNum:
            maxNum = number
    return maxNum

