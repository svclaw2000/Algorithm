N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort()

for i in range(1, N):
    arr[i] += arr[i-1]

print(sum(arr[1:]) if N > 1 else arr[0])