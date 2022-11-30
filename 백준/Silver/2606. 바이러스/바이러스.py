import sys
input=sys.stdin.readline

n=int(input())
node=int(input())
network=[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
cnt=-1

for _ in range(node):
    a,b=map(int,input().split())
    network[a].append(b)
    network[b].append(a)

def dfs(num):
    
    ## 방문처리
    visited[num]=True

    ## 감염된 갯수 증가
    global cnt
    cnt+=1
    
    ## 연결된 그래프 확인하기
    for net in network[num]:
        if (not visited[net]):
            dfs(net)

dfs(1)
print(cnt)