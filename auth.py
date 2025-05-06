class ProxmoxAPI:
    def __init__(self, host, user, password, verify_ssl=False):
        self.host = host
        self.user = user
        self.password = password
        self.verify_ssl = verify_ssl

    def authenticate(self):
        pass

    def connect(self):
        pass
