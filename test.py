from math import ceil
# print('Hello world')
def getChange(M, p):
    denominations = [0.01,0.05, 0.1,0.25,0.5,1]
    change = M-p
    ret = [0]*6
    for i in range(len(denominations)-1, -1,-1):
        ret[i] = int(change / denominations[i])
        # print(change * (change // denominations[i]))
        change = round(change-denominations[i]*(change // denominations[i]), 2)

    print(ret)
    # return ret
getChange(5, 0.99)
getChange(3.14, 1.99) # should return [0,1,1,0,0,1]
getChange(4, 3.14) # should return [1,0,1,1,1,0]
getChange(0.45, 0.34) # should return [1,0,1,0,0,0]
