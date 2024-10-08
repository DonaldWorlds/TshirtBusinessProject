import os
import csv
import time
import queue
import threading
import json
from dotenv import load_dotenv
from py3pin.Pinterest import Pinterest
from user_agent_handler import UserAgentHandler
from proxy_handler import ProxyHandler

# Load environment variables
load_dotenv()

class PinterestBot:
    def __init__(self, proxy_handler, user_agent_handler):
        self.proxy_handler = proxy_handler
        self.user_agent_handler = user_agent_handler
        
        # Initialize Pinterest instance with credentials
        email = os.getenv('EMAIL')
        password = os.getenv('PASSWORD')
        username = os.getenv('USERNAME')
        cred_root = os.getenv('CRED_ROOT')

        if not all([email, password, username, cred_root]):
            raise ValueError("Missing credentials or CRED_ROOT path. Please check your .env file.")

        self.pinterest = Pinterest(
            email=email,
            password=password,
            username=username,
            cred_root=cred_root
        )
        
        self.loaded_boards = set()
        self.queue = queue.Queue()
        self.lock = threading.Lock()

    def login(self):
        # Perform login using the Pinterest instance
        try:
            self.pinterest.login()
            print("Successfully logged in to Pinterest.")
        except Exception as e:
            print(f"Failed to log in: {str(e)}")


    """def login(self):
        user_agent = self.user_agent_handler.get_random_user_agent()
        url = 'https://www.pinterest.com/login/'
        
        # Use the proxy handler to make the login request
        response = self.proxy_handler.get_scraper_api_response(url, user_agent)
        
        if response and response.status_code == 200:
            # Perform login using the Pinterest instance
            self.pinterest.login()
            print("Successfully logged in to Pinterest.")
        else:
            print(f"Failed to load login page: {response.status_code if response else 'No response'}")"""


    def upload_pins_from_csv(self, csv_file_path):
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for index, row in enumerate(reader, start=1):
                board_id = row['board_id']
                image_path = os.path.join('images', row['image_path'])
                description = row['description']
                title = row['title']
                link = row['link']

                try:
                    response = self.pinterest.upload_pin(
                        board_id=board_id,
                        image_file=image_path,
                        description=description,
                        title=title,
                        section_id=None,
                        link=link
                    )
                    
                    response_data = json.loads(response.content)
                    print(f"Response for line {index}: {response_data}")

                    if "resource_response" in response_data:
                        print(f"Successfully pinned {image_path} to board {board_id}")
                    else:
                        print(f"Failed to pin {image_path}: {response_data}")
                    
                    time.sleep(600)  # 600 seconds = 10 minutes

                except Exception as e:
                    print(f"Error uploading pin {image_path} on line {index}: {e}")

                print(f"Processed line {index} from {csv_file_path}")

if __name__ == "__main__":
    user_agent_handler = UserAgentHandler()
    proxy_handler = ProxyHandler()
    pinterest_bot = PinterestBot(proxy_handler, user_agent_handler)
    
    pinterest_bot.login()
    pinterest_bot.upload_pins_from_csv('pins.csv')
