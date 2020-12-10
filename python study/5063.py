V = int(input())
V_list = []
V_list = list(str(input()))

if V_list.count('A') > V_list.count('B'):
    print('A')
elif V_list.count('A') < V_list.count('B'):
    print('B')
else:
    print('Tie')