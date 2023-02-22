import sys
input = sys.stdin.readline

n = int(input())
drink = list(map(int, input().split()))

drink.sort(reverse=True)
ans = drink[0]

for i in range(1,n):
    ans += drink[i]/2

print(ans)