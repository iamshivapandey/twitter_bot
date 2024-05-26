from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime



def get_data():
    try:
        i = datetime.today().date()

        print("------------------>>> Data Collection Started")

        # Setup Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Enable headless mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (required for headless mode)
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (required for headless mode)
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems (required for headless mode)
        chrome_options.add_argument("start-maximized")  # Open Browser in maximized mode
        chrome_options.add_argument("disable-infobars")  # Disable infobars
        chrome_options.add_argument("--disable-extensions")  # Disable extensions
        chrome_options.add_argument("--disable-browser-side-navigation")  # Disable browser side navigation
        chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
        chrome_options.add_argument("--window-size=1600, 400")  # Set window size
        chrome_options.add_argument("--user-agent=Your User-Agent String")  # Match user-agent string

        # Setup Chrome driver
        driver = webdriver.Chrome(options=chrome_options)


        # Open the target webpage
        driver.get('https://coinmarketcap.com/')  
        time.sleep(2)  # Adjust the sleep time as necessary


        # Take a screenshot of the entire page
        driver.save_screenshot(f'daily_ss/upper_half_{i}.png')

        driver.set_window_size(1600,1080)

        # Scroll the page to the upper part
        driver.execute_script(f"window.scrollTo(100, 500);")

        driver.save_screenshot(f'daily_ss/lower_half_{i}.png')



        driver.set_window_size(1600,1200)

        driver.get('https://coinmarketcap.com/trending-cryptocurrencies/')
        time.sleep(2)

        driver.save_screenshot(f'daily_ss/trending_cryptos_{i}.png')




        driver.set_window_size(1600,1000)

        driver.get('https://coinmarketcap.com/gainers-losers/')
        time.sleep(2)


        driver.save_screenshot(f'daily_ss/gainers_{i}.png')

        driver.execute_script(f"window.scrollTo(1400, 2000);")
        driver.save_screenshot(f'daily_ss/losers_{i}.png')


        driver.quit()

        print("------------------>>> Data Collection Completed")

        return True

    except Exception as e:
        print("------------------------>>>",e)
        return False
