from threading import Thread


class MyThread(Thread):

    def __init__(self, scrypt):
        self.scrypt = scrypt
        Thread.__init__(self)

    def run(self):
        self.scrypt()


