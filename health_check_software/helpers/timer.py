import logging
import time
import datetime
import threading

class Timer:
    def __init__(self, print_every):
        self.log = logging.getLogger()
        self.print_every = print_every
        self.stop_event = threading.Event()
        self.time_guard_thread = threading.Thread(target=self.run, args=())


    def start(self):
        self.time_guard_thread.start()


    def stop(self):
        self.stop_event.set()
        self.time_guard_thread.join()


    def run(self):
        time_start = time.time()
        while not self.stop_event.wait(0):
            self.log.debug("Time passed: {} s".format(round(time.time()-time_start), 0))
            time.sleep(self.print_every.total_seconds())