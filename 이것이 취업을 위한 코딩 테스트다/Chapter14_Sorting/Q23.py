# 00:04 / 00:20

N = int(input())
student = [input().split() for _ in range(N)]

student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

print(*[s[0] for s in student], sep='\n')