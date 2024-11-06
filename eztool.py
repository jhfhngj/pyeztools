import time
class wtools:
    def wu(cond):
        while not cond:
            time.sleep(1)
    def wait(tim):
        time.sleep(tim)