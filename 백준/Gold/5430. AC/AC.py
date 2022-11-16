case = int(input())

for i in range(case):
    funList = list(input())
    cntR = 0 # R 갯수 확인
    N = int(input())
    numList  = input()
    
    if N == 0: # 안에 있는게 없으면 바로 []로 리턴 
        numList = []
    elif N == 1:# 안에 있는게 하나일 경우 
        numList = [numList[1:-1]]
    else:
        numList = list(map(int, numList[1:-1].split(',')))
        
    if funList.count('D') > len(numList):
        print('error')
        continue
            
    for j in funList:
        if len(numList) == 0:
            break
            
        if j == 'R':
            if cntR == 0: # 0 혹은 짝수일 때 
                cntR = 1
            else:
                cntR = 0
        elif j == 'D':
            if cntR == 0: # 0 혹은 짝수일 때 
                del numList[0]
            else:
                del numList[-1]
                
    if len(numList) == 0:
        print('[]')
    else:
        if cntR == 0: # 0 혹은 짝수일 때 
            print('[' + ','.join(map(str, numList)) + ']')
        else:
            numList.reverse()
            print('[' + ','.join(map(str, numList)) + ']')
                
                