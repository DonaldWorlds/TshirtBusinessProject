import os
import random
import time
from dotenv import load_dotenv
from proxy_handler import ProxyHandler
from user_agent_handler import UserAgentHandler

def test_proxy_rotation():
    load_dotenv()
    print("Loading environment variables...")

    zenrows_api_key = os.getenv('ZENROWS_API_KEY')
    if not zenrows_api_key:
        print("ZENROWS_API_KEY not found in environment variables.")
        return

    print(f"ZENROWS_API_KEY found: {zenrows_api_key}")

    proxy_handler = ProxyHandler()
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78"
    ]


    user_agent_handler = UserAgentHandler(user_agents)

    test_urls = [
        "http://ident.me",
        "https://httpbin.org/ip"
    ]

    successful_requests = 0
    max_retries = 3

    for i in range(5):  # Test with 5 requests for demonstration
        url = random.choice(test_urls)
        user_agent = user_agent_handler.get_random_user_agent()
        for attempt in range(max_retries):
            try:
                response = proxy_handler.get_scraper_api_response(url, user_agent)
                if response:
                    print(f"Using Scraper API URL: {url} with User-Agent: {user_agent}")
                    print(f"Response from {url}: {response.text}")
                    successful_requests += 1
                    break
            except Exception as e:
                print(f"Failed to connect to {url} using Scraper API: {e}")
                print(f"Retrying {url} (attempt {attempt + 1}) with User-Agent: {user_agent}")
                time.sleep(2)  # Short delay before retrying

    print(f"Successful requests: {successful_requests}")

if __name__ == "__main__":
    test_proxy_rotation()
