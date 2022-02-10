import threading
import time


def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    print('Done Sleeping...')


def main():
    threads = []
    for _ in range(100):
        t = threading.Thread(target=do_something, args=[2])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} seconds')
