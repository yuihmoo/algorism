test_range = int(input())
for i in range(test_range):
    result = ""
    X, Y = input().split()
    X = int(X)
    for j in Y:
        for k in range(X):
            result = result + j
    print(result)