t = int(input()) # набор количества данных
result = []

def count_odds(a, b):
    return (b + 1) // 2 - (a // 2)

for i in range(t):
    n, k = list(map(int, input().split(" ")))
    
    odd_count = count_odds(n-k+1, n)

    if odd_count % 2 == 0:
        print("YES")
    else:
        print("NO")