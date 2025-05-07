import requests


class ProxmoxAPI:
    def __init__(self, host, user, password, verify_ssl=False):
        self.host = host
        self.user = user
        self.password = password
        self.verify_ssl = verify_ssl
        self.ticket = None
        self.csrf_token = None

    def authenticate(self):
        url = f"https://{self.host}:8006/api2/json/access/ticket"
        print(url)
        data = {"username": self.user, "password": self.password}
        resp = requests.post(url, data=data, verify=self.verify_ssl)

        if resp.status_code != 200:
            raise Exception(f"Auth failed: {resp.text}")
        res = resp.json()["data"]
        self.ticket = res["ticket"]
        self.csrf_token = res["CSRFPreventionToken"]
        return self.ticket, self.csrf_token

    def connect(self):
        if not self.ticket:
            self.authenticate()
        return self.ticket is not None
