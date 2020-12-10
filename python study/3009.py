X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())
X3, Y3 = map(int, input().split())

list_X = [X1, X2, X3]
list_Y = [Y1, Y2, Y3]
list_X.sort()
list_Y.sort()

if list_X.count(list_X[0]) == 2:
    list_X.append(list_X[-1])
else:
    list_X.append(list_X[0])

if list_Y.count(list_Y[0]) == 2:
    list_Y.append(list_Y[-1])
else:
    list_Y.append(list_Y[0])

print(list_X[3], list_Y[3])