t = int(input()) #количество наборов чисел
result = []
for _ in range(t):
    n, k = list(map(int, input().split(" "))) #количество людей / монеты при которых забираются
    data = list(map(int, input().split(" "))) #список монет с индексом людей
    robin_monet = 0
    cnt = 0
    for i in data:
        if i >= k:
            robin_monet += i
        if i == 0 and robin_monet > 0:
            robin_monet -= 1    
            cnt += 1
    result.append(cnt)

for i in result:
    print(i)