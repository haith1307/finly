import requests


class APIRequest:
    def __init__(self):
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

    def get(self, link):
        return requests.get(link, headers=self.headers).json()
