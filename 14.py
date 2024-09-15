def infinite_recursion(n):
    print(n)
    infinite_recursion(n + 1)

infinite_recursion(0)
