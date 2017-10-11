from functools import partial
from multiprocessing.pool import Pool
from time import time, sleep


def do_something_lengthy():
    print("I am working...")
    sleep(5)
    return "done"

def run_parallel():
    print("************ running in parallel ************")
    pool = Pool(2)
    ts = time()
    multiple_results = [pool.apply_async(do_something_lengthy, ()) for i in range(2)]
    [res.get() for res in multiple_results] # wait until all are done
    print('Took {}s'.format(time() - ts))

def run_sequential():
    print("************ running sequentially ************")
    ts = time()
    for _ in range(2):
        do_something_lengthy()
    print('Took {}s'.format(time() - ts))


if __name__ == '__main__':
    run_sequential()
    run_parallel()