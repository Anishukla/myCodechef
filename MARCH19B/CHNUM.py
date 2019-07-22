T = int(input())
for i in range(T):
    N = int(input())
    A =  list(map(int,input().split()))
    m = 0
    a = 0
    for i in range(N):
        if(A[i] >= 0):
            m = m+1
        else:
            a = a+1
            
    if(a>=1):
        print(m, a)
        
    if(a==0):
        print(m, m)

    