num_1, num_2, num_3 = map(int,input().split())
list_1 = [num_1, num_2, num_3]
list_1.remove(max(list_1))
print(max(list_1))