from functools import partial
import multiprocessing
from multiprocessing.pool import Pool
from time import time, sleep

class NoDaemonProcess(multiprocessing.Process):
    def _get_daemon(self):
        return False
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)
 
class NoDaemonProcessPool(Pool):
    Process = NoDaemonProcess


class Klazz(object):
    def start(self):
        """docstring for start"""
        t0 = time()
        for x in range(6):
            self.sequential_transform()
        print('Sequential took {} seconds.'.format(time()-t0))
        
        no_daemon_pool = NoDaemonProcessPool(3)
        t0 = time()
        multi = []
        for x in range(9):
            multi.append(no_daemon_pool.apply_async(self.parallel_transform))
        r = [i.get() for i in multi]
        
        print('Parallel took {} seconds.'.format(time()-t0))

    def parallel_transform(self):
        """docstring for transform"""
        print('transform called!')
        pool = Pool(3)
        ts = time()
        multiple_results = []
        multiple_results.append(pool.apply_async(self._m1, args = ('a')))
        multiple_results.append(pool.apply_async(self._m2, args = ('a')))
        multiple_results.append(pool.apply_async(self._m3, args = ('a')))
        retval = [res.get() for res in multiple_results] # wait until all are done
        print('Took {} - returned: {}'.format(time() - ts, retval))
        
    def sequential_transform(self):
        """docstring for transform"""
        ts = time()
        self._m1('a')
        self._m2('a')
        self._m3('a')
        print('Took {}'.format(time() - ts))

    def _m1(self, a):
        """docstring for m1"""
        print("m1 working.. with arg {}".format(a))
        sleep(5)
        return 'm1'

    def _m2(self, a):
        """docstring for m1"""
        print("m2 working.. with arg {}".format(a))
        sleep(5)
        return 'm2'

    def _m3(self, a):
        """docstring for m1"""
        print("m3 working.. with arg {}".format(a))
        sleep(5)
        return 'm3'


# def do_something_lengthy():
#     print("I am working...")
#     sleep(5)
#     return "done"
#
# def run_parallel():
#     print("************ running in parallel ************")
#     pool = Pool(2)
#     ts = time()
#     multiple_results = [pool.apply_async(do_something_lengthy, ()) for i in range(2)]
#     retval = [res.get() for res in multiple_results] # wait until all are done
#     print('Took {} secs - returned: {}'.format(time() - ts, retval))
#
# def run_sequential():
#     print("************ running sequentially ************")
#     ts = time()
#     for _ in range(2):
#         do_something_lengthy()
#     print('Took {}s'.format(time() - ts))


if __name__ == '__main__':
    # run_sequential()
    # run_parallel()
    k = Klazz()
    k.start()