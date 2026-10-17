top_left = 1
order = 10
for i in range(order):
    list=[]
    for i in range(top_left,order+1):
        list.append(i)
    for j in range(1,top_left):
        list.append(j)    
    print(" ".join(str(x) for x in list))
    #print(*list) is the same thing as line 9
    if top_left<order:
        top_left +=1
    else:
        top_left = 1