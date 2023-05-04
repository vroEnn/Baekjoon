import sys
input = sys.stdin.readline


n,m = map(int,input().split())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(int(input())):
    i,j,x,y = map(int,input().split())
    sum = 0
    
    for p in range(i-1,x):
        for q in range(j-1,y):
            sum += arr[p][q]
            
    print(sum)