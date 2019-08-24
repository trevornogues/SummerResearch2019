def loop(L):
    for i in range(len(L)):
        if L[i] == i:
            i += 1
        print(i)

test = [1,1,1,2,4,4,4]

loop(test)