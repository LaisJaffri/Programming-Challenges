A = [0,0,1,1]
B = [0,1,0,1]


print(f"A B | {"AND": <5} {"OR": <5} {"XOR": <5}")
for i in range(len(A)):
    print(f"{A[i]} {B[i]} | {(A[i] and B[i]): <5} {(A[i] or B[i]): <5} {(A[i] ^ B[i]): <5}")