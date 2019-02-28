a, b, c = map(int, input().split())
n = max(a, max(b, c))
k = min(a, min(b, c))
print(n - k)
