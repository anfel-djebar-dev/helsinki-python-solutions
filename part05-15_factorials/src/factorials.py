def factorials(n: int) -> dict:
    d={}
    fctrl = 1
    for i in range(1,n+1):
        fctrl*=i
        d[i] = fctrl
    return d

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
