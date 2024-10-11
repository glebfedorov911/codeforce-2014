t = int(input())

def sr(l, n):
    return sum(l) / n

def c(l, sr):
    return sum([i < (sr/2) for i in l]) > len(l)//2 #несчастны - True

k = -1
for _ in range(t):
    was_true = False
    n = int(input())
    naselenie = list(map(int, input().split(" ")))
    mx = max(naselenie)
    idx = naselenie.index(mx)
    if len(naselenie) == 1 or len(naselenie) == 2:
        k = -1
    else:
        k = 0
        while True:
            if c(naselenie, sr(naselenie, len(naselenie))):
                was_true = True
                if k == 0:
                    break
                while c(naselenie, sr(naselenie, len(naselenie))):
                    naselenie[idx] -= 1
                    k -= 1
            else:
                naselenie[idx] += 5
                k += 5
            if was_true:
                k += 1
                break

    print(k)