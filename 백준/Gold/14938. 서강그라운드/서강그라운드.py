import sys
input = sys.stdin.readline

INF = int(1e9)
n, m, r = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

item = list(map(int, input().split()))



# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(r):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# result를 빈 리스트로 하고 최대값 출력도 가능
for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if graph[i][j] <= m :
            tmp += item[j-1] 
            # item의 인자가 n개인데, j가 1부터 들어가서 j-1번째 인자부터 더해야함
    if tmp > result:
        result = tmp
        # result.append(tmp)

print((result))
# print(max(result))
        