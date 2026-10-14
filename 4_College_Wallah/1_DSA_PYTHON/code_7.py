def func(i):
    if i==5:
        return
    func(i+1)
    print(i, end=" ")
func(1)