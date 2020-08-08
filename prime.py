def f(N):
    P = []
    for n in range(2, N):
        q = 1
        for p in P:
            q = n % p
            if q == 0:
                break

        if q:
            P.append(n)
    return P

if __name__ == '__main__':
    P = f(20)
    print(P)
