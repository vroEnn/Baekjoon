import sys
input = sys.stdin.readline

while True:
    S = input()
    li = []
    
    if S[0] == '.':
        break
    
    for i in S:
        if i == '[' or i == '(':
            li.append(i)
        elif i == ']':
            if len(li) > 0 and li[-1] == '[':
                li.pop()
            else:
                li.append(']')
                break
        elif i == ')':
            if len(li) > 0 and li[-1] == '(':
                li.pop()
            else:
                li.append(')')
                break
                
    if len(li) == 0:
        print('yes')
    else:
        print('no')