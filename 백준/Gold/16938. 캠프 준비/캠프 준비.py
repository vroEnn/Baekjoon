import sys
import itertools

N, L, R, X = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
cnt = 0 

for i in range(1,N+1):
    com = list(itertools.combinations(A, i))
    
    for num in com:
        if L <= sum(num) <= R and abs(num[0]-num[-1]) >= X:
            cnt += 1
        
print(cnt)