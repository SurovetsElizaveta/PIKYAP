from time import time, sleep
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, type, val, traceback):
        go_time = time() - self.start_time
        print(f"\ntime: {go_time}")


@contextmanager
def cm_timer2():
    start_time = time()
    try:
        yield
    finally:
        go_time = time() - start_time
        print(f"time: {go_time}")


# with cm_timer_1():
#     sleep(5.5)
#
# with cm_timer2():
#     sleep(5.5)
