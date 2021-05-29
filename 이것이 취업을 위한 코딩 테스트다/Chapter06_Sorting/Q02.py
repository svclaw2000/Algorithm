# 00:02 / 00:20
N = int(input())
student = []
for _ in range(N):
    inp = input().split()
    student.append((int(inp[1]), inp[0]))

student.sort()

print(*[s[1] for s in student])