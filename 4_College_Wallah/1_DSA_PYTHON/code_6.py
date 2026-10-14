def func2(x,n):
    if x == n:
        return
    print(n, end=" ")
    func2(x, n-1)
func2(0, 6)