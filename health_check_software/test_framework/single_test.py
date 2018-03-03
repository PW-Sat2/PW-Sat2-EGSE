import logging
import time

class SingleTest(object):
    def __init__(self, name=None, description=None, **kwargs):
        self.name = name
        self.description = description
        self.result = None
        self.log = logging.getLogger(name)
        self.obc = None
        self.lock = None
        self.timestamp = None
        self.kwargs = kwargs
        self.data = None

        self.name = name
        self.description = description
        self.default_name = None
        self.default_description = None

        self.set_default_title_description()
        self.override_title_desc()


    def set_default_title_description(self):
        pass


    def override_title_desc(self):
        if self.name == None:
            self.name = self.default_name

        if self.description == None:
            self.description = self.default_description


    def test_script(self):
        pass


    def run(self, obc, lock):
        self.obc = obc
        self.lock = lock
        with self.lock:
            self.timestamp = time.time()
            self.log.debug("Test started")
            self.test_script()
            self.log.debug("Test finished")