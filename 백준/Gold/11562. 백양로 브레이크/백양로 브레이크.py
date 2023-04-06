n, m = map(int,input().split())

INF = 1e9
road = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j:
            road[i][j] = INF

# 일방향이면 미리 도로 건설해놓고 배열에 넣어놓자.
for _ in range(m):
    u, v, b = map(int,input().split())
    if b == 0:
        road[u-1][v-1] = 0
        road[v-1][u-1] = 1      # 통행하려면 도로 건설해야함
    elif b== 1:
        road[u-1][v-1] = 0
        road[v-1][u-1] = 0

# 최단 거리 업데이트 해놓기.
for t in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if road[i][j] > road[i][t] + road[t][j]:
                road[i][j] = road[i][t] + road[t][j]

# 해당 도로의 비용을 출력하기만 하면 됨.
k = int(input())
for _ in range(k):
    s, e= map(int,input().split())
    print(road[s-1][e-1])