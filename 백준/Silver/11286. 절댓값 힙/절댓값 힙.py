import sys
input = sys.stdin.readline
from heapq import heappop, heappush


h = []

for i in range(int(input())):
    x = int(input())
    
    if x !=0:
        heappush(h, (abs(x),x))

    else:
        print(heappop(h)[1] if h else 0) 