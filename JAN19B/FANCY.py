T = int(input())

for i in range(T):
    String = input()
    S = String.split()
    l = len(S)
    
    for i in range(l):
        if(S[i] == 'not'):
            print("Real Fancy")
            break
    else:
        print("regularly fancy")
        