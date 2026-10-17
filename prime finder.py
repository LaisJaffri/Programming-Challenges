number = 20
prime = []
print("TEST")
for i in range(1,number+1):
    for j in range(1,i+1):
            if j!=1 and i!=j and i%j==0:
                break
            if i==j:
                 prime.append(i)
                 break
prime.remove(1)
print(prime)