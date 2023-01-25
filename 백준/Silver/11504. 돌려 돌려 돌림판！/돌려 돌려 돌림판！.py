import sys

# 테스트케이스 T , 돌림판등분 N , XY길이 M, X,Y 
T = int(sys.stdin.readline())

# T개수만큼 반복, new_clrcle 리스트 새로작성(가능한 모든 경우를 담음)
for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    X = int(''.join(sys.stdin.readline().split()))
    Y = int(''.join(sys.stdin.readline().split()))
    circle = list(sys.stdin.readline().split())
    new_circle = circle + circle[:M-1]
    cnt = 0
    temp = 0
# M개씩 자른부분을 temp로 입력하고 조건만족시 cnt세줌
    for i in range(N):
        temp = int(''.join(new_circle[i:i+M]))
        if X <= temp <= Y:
            cnt +=1
    print(cnt)