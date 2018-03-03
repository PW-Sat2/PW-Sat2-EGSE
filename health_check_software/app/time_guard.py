import logging
import time
import datetime
import threading

class TimeGuard(object):
    def __init__(self, obc, lock):
        self.stop_event = threading.Event()
        self.log = logging.getLogger('TIME GUARD')
        self.lock = lock
        self.obc = obc

    def stop(self):
        self.stop_event.set()

    def run(self):
        while not self.stop_event.wait(0):
            with self.lock:
                obc_time = self.obc.current_time()
                if obc_time > datetime.timedelta(minutes=2):
                    self.log.error("OBC Time {}".format(obc_time))

                obc_response = self.obc.jump_to_time(0)
                obc_time_next = self.obc.current_time()

                debug_response = 'OBC answer: {}, OBC indication {}'.format(obc_response, obc_time_next)

                if obc_response == 'OK' and obc_time_next < datetime.timedelta(seconds=10):
                    if obc_time > datetime.timedelta(minutes=2):
                        self.log.error('Time set correctly')
                        self.log.error(debug_response)
                    else:
                        self.log.info('Time set correctly')
                        self.log.debug(debug_response)
                else:
                    self.log.error('Time set not correctly')
                    self.log.error(debug_response)
            time.sleep(1)
        return