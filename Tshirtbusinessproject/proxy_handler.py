import os
from zenrows import ZenRowsClient

class ProxyHandler:
    def __init__(self, proxy_list=None):
        self.zenrows_api_key = os.getenv('ZENROWS_API_KEY')
        self.proxy_list = proxy_list or []
        self.zenrows_client = ZenRowsClient(self.zenrows_api_key)

    def get_scraper_api_response(self, url, user_agent, data=None, files=None, method="GET"):
        headers = {
            'User-Agent': user_agent
        }
        if method == "POST":
            if files:
                response = self.zenrows_client.post(url, headers=headers, data=data, files=files)
            else:
                response = self.zenrows_client.post(url, headers=headers, data=data)
        else:
            response = self.zenrows_client.get(url, headers=headers)
        return response
