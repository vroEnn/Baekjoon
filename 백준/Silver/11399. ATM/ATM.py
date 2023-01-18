N = int(input())
m = list(map(int,input().split()))

result = 0
m.sort()
    
for i in range(N):
    result += m[i] * (N-i)

print(result)