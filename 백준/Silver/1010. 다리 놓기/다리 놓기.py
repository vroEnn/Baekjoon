import sys
from math import factorial

T = int(sys.stdin.readline())
for _ in range(T):
    N,M = map(int, sys.stdin.readline().split())
    Max = max(N,M)
    Min = min(N,M)
    # Combination 구하기
    print(factorial(Max)//(factorial(Min)*factorial(Max-Min)))
