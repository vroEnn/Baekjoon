T = int(input())
for _ in range(T):
    J, N = map(int, input().split()) 
    tmp = []
    
    for i in range(N):
        r, c = map(int, input().split())
        tmp.append(r * c) 
    
    count = 0
    tmp.sort(reverse=True)
    
    for i in range(N):
        J = J - tmp[i]
        count += 1
        if J <= 0:
            break
            
    print(count)