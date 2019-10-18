class Subject:

    def request(self):
        print("subject is handling request.")


class Proxy(Subject):
    def __init__(self, subject):
        self.subject = subject

    def request(self):
        if self.check_access():
            self.subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request")