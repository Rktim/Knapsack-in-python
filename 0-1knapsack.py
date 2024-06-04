def knapsack(it,c):
    it.sort(key=lambda it: it[0]/it[1],reverse=True)
    
    t=0
    
    for i in it:
        if c==0:
            break
        f=min(c/i[1],1)
        t+= f * i[0]
        c-=f*i[1]
    return t

items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
max_value = knapsack(items, capacity)
print("Maximum value that can be obtained:", max_value)
