from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

L = [arr[0]]

for i in range(1, n):
    if L[-1] < arr[i]:
        L.append(arr[i])
  
    else:
        idx = bisect_left(L, arr[i])
        L[idx] = arr[i]
    
print(len(L))