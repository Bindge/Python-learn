numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

incorrect_index = None
sum = 0
i = 0
while i < len(numbers):
    if numbers[i] == None:
        incorrect_index = i
    else:
        sum = sum + numbers[i]
    i += 1
numbers[incorrect_index] = sum/len(numbers)
print(f'Измененный список: {numbers}')


