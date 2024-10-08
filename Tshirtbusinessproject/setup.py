"""
First create the env for the Virtual enviroment 
for the Tshirtbusinessproject 

to activate venv 
source pinterest_env/bin/activate 

to deactivate 
deactivate 

// Tools that will be used 
Zendesk for proxies use 

py3-pinterest  api for scaping pinterest 
selenium       A tool for automating web browsers.
aiohttp        An asynchronous HTTP client/server framework.
asyncio        Purpose: A library to write concurrent code using the async/await syntax.
celery         An asynchronous task queue/job queue.
redis          An in-memory data structure store used as a database, cache, and message broker.


Explanation of Each Tool's Use Case in Your Project
py3_pinterest: Automates basic Pinterest interactions like creating pins, following users, and liking content. This is the core of your automation and handles most of the Pinterest-specific logic.

Selenium: Complements py3_pinterest by handling more complex web interactions, especially those requiring a real browser, like solving CAPTCHAs or navigating JavaScript-heavy pages.

aiohttp: Enhances your scraping capabilities by allowing you to make asynchronous HTTP requests, enabling you to fetch data from multiple sources concurrently without blocking your main program flow.

asyncio: Manages asynchronous operations in your project. When combined with aiohttp, it allows you to run multiple tasks concurrently, improving efficiency and performance.

Celery: Manages task distribution and execution. It handles the execution of background tasks, schedules periodic jobs (like posting pins at regular intervals), and manages retries for failed tasks. Celery ensures your automation tasks are executed reliably and efficiently.

Redis: Acts as the backend for Celery, storing task queues and enabling task distribution. Redis can also be used for caching data, such as user agent lists, session information, or temporary data fetched from Pinterest or other sources.


example workflow 
Initialization:

**SKIP FOR NOE Configure your project settings, including Pinterest credentials and Redis connection details.
Set up logging to track the execution of your tasks.
Task Definition: ** 

** SKIP FOR NOW**Define Celery tasks in tasks.py for actions like creating pins, following users, and liking pins.
Automation Logic:**

1. Implement Pinterest interactions in pinterest_bot.py using py3_pinterest and Selenium.
Use aiohttp and asyncio in utils.py to perform asynchronous tasks like fetching data from external sources.
Task Scheduling and Execution:

2. Schedule and execute tasks using Celery, ensuring tasks are distributed across workers and executed efficiently.
3. Monitor task execution and handle retries for failed tasks.
4. Content Management:

Manage your pin data in pins.csv and rotate user agents from user_agents.txt to avoid detection.
Running the Project:

Use main.py to initialize and start the automation process, including logging in to Pinterest, performing scheduled tasks, and handling errors.


run pip freeze to check the installations 




TSHIRTBUSINESSPROJECT/
├── __init__.py
├── pinterest_bot.py
├── task_manager.py
├── proxy_manager.py
├── user_agent_manager.py
├── main.py
└── requirements.txt


"""






"""
pinterest_bot.py

Purpose: Handles interactions with Pinterest using py3_pinterest.
Key Classes/Functions:
PinterestBot: Class for Pinterest operations like logging in, creating pins, repinning, following and unfollowing process. 


This class initializes a Pinterest object, logs in, and has a method to create a pin. 
Let's expand on this by adding methods for other Pinterest operations, such as repinning content, following users, and using proxies and user agents to avoid detectio


Download a chromedriver for your project 
go to google and search how to download the chrome drive 
place it in path to run in the command line and then run chromedriver 

donaldk@donalds-MacBook-Air ~ % chromedriver --version
ChromeDriver 127.0.6533.72 (9755e24ca85aa18ffa16c743f660a3d914902775-refs/branch-heads/6533@{#1760})
donaldk@donalds-MacBook-Air ~ % 


ok now download the chromedriver manager 

Issues with Manual Management
Manual Downloads: Without webdriver_manager, you would need to manually download the correct version of ChromeDriver that matches your version of Chrome.
Updates: You’d need to update ChromeDriver whenever you update your Chrome browser.
Path Management: You’d have to ensure ChromeDriver is in your system’s PATH and executable.
What webdriver_manager Does
Automatic Downloads: It automatically downloads the correct version of the browser driver compatible with your installed browser version.
Path Management: It manages the driver path, so you don’t need to manually place the driver in your PATH.
Version Compatibility: It ensures the version compatibility between the browser and the driver.

I will intent to store credentials to avoid re-loginging eachtime 
ensure the red_root directory has the appropriate write permissionas 
py3_pinterest library typically stores session data or cookies to facilitate subsequent logins.
we will always read creds from the credroot file 

"""


"""
google.com example ok
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class BrowserBot:
    def __init__(self, proxy_list=None, user_agents=None):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.proxy_list = proxy_list or []
        self.user_agents = user_agents or []

    def go_to_google(self):
        self.driver.get("https://www.google.com")
        print("Title of the Google page is: ", self.driver.title)

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    browser_bot = BrowserBot()

    browser_bot.go_to_google()
    browser_bot.quit()"""


"""
We will no install zenrows sdk 
pip install zenrows will allow us to access proxies and rotate them into out project 
check the zenrows dashboard for api key 
Install ZenRows’ Python SDK

boards id 
Board Name: Default Board, Board ID: 939774715932751037 that i created 

"""








