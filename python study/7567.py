dish_list = list(str(input()))
result = 0

for i in range(len(dish_list)):
    if i == 0:
        result += 10
    elif dish_list[i] == dish_list[i-1]:
        result += 5
    else:
        result += 10
        
print(result)