from multiprocessing import Pool
import time


def get_value(value):
    i = 0
    while i < 3:
        time.sleep(1)
        print(value, i)
        i += 1


if __name__ == '__main__':
    values = ['value{}'.format(str(i)) for i in range(0, 5)]
    pool = Pool(processes=4)
    pool.map(get_value, values)
