def gen(n):
    for i in range(n):
        yield i ** 2


if __name__ == '__main__':
    l = gen(10000)
    for i in l:
        print(i)
