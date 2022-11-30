board = [list(map(str,input().split())) for _ in range(5)]
dx, dy = [1,0,-1,0], [0,1,0,-1]

def OOB(x,y):
    return 0 <= x < 5 and 0 <= y < 5

def dfs(x,y,word):
    word += board[x][y] # dfs 탐색하면서 문자열에 현재문자 계속 추가해주면서 word만듦
    
    if len(word) == 6: # word크기 6 되면 result 리스트에 추가 
        result.append(word)
        return 
    
    for d_x, d_y in zip(dx,dy):
        nx = x + d_x
        ny = y + d_y
        if OOB(nx,ny):
            dfs(nx,ny,word)
            
# 중복제거, 만들어지는 서로 다른 문자열 갯수 출력         
result = []
for i in range(5):
    for j in range(5):
        if board[i][j]:
            dfs(i,j,'')
            
print(len(set(result)))