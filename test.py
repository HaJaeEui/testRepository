import sys
sys.stdin = open("input.txt", "r")
n,m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

print(n, m)
print(arr)