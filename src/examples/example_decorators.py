def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        f(*args, **kwargs)
        print("Ended")

    return wrapper


@func
def func2(text):
    print(text)


if __name__ == '__main__':
    func2("Mario World")
