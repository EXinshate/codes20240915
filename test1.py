while True:
    try:
        n = input("请输入一个整数: ")
        n = int(n)
        break
    except ValueError as e:
        print("�无效数字，再次输入 ...",e)
print("输入成功!")