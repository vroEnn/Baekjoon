import sys
input = sys.stdin.readline
A=[]
for _ in range(int(input())):
    a = input().rstrip()
    if a not in A:
        A.append(a)
A.sort()
A.sort(key=len)
for i in A:
    print(i)