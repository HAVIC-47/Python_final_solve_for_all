def jog_korbo(n):
    total = 0
    term = 1
    for _ in range(n):
        total += term
        term *= 3
    return total


n=int(input())
jogfol=jog_korbo(n)
print(jogfol)