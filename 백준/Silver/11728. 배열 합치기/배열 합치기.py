N,M= map(int, input().split())
arr_N = list(map(int, input().split()))
arr_M = list(map(int, input().split()))
arr = sorted(arr_N + arr_M)
print(*arr)