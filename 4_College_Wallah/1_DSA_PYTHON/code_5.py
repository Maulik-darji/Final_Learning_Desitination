def func(i):
    if i == 5:
        return
    print(i, end=" ")
    func(i+1)

func(0)
