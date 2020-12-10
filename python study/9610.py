N = int(input())
XY_list = []
i = 0
for i in range(N):
    x, y = map(int,(input().split()))
    if x>0 and y>0:
        XY_list.append('Q1')
    elif x==0 or y==0:
        XY_list.append('AXIS')
    elif x<0 and y>0:
        XY_list.append('Q2')
    elif x<0 and y<0:
        XY_list.append('Q3')
    elif x>0 and y<0:
        XY_list.append('Q4')
    i += 1

print('Q1:', XY_list.count('Q1'))
print('Q2:', XY_list.count('Q2'))
print('Q3:', XY_list.count('Q3'))
print('Q4:', XY_list.count('Q4'))
print('AXIS:', XY_list.count('AXIS'))
