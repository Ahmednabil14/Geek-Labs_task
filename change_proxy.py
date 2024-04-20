from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Define the change_proxy function
def change_proxy(proxy, port):
    profile = webdriver.ChromeOptions()
    profile.add_argument(f'--proxy-server=http://{proxy}:{port}')
    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service, options=profile)
    return driver

# Setup WebDriver with Proxy
proxy = 'your_proxy_server' # Replace with your proxy server
port = 'your_proxy_port' # Replace with your proxy port
driver = change_proxy(proxy, port)

# The rest of your script remains the same
