input_T = int(input())

def solve(N):
    if N == 1 :
        return 1
    elif N == 2 :
        return 2
    elif N == 3 :
        return 4
    else:
        return solve(N-1) + solve(N-2) + solve(N-3)

for i in range(input_T) :
    N = int(input())
    print(solve(N))
    