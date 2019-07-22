N, M = input().split()
N = int(N)
M = int(M)
A =  list(map(int,input().split()))
B =  list(map(int,input().split()))
pairs = N+M-1
l = []
val = 0

for i in range(N):
    for j in range(M):
        c = A[i]+B[j]
        if(val >= pairs):
            break
        if(c not in l and val < pairs):
            l.append(c)
            print(i, j)
            val = val+1
    

