from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# === CONFIGURATION ===
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
START_URL = os.getenv("START_URL")
PAPER_ID = os.getenv("PAPER_ID")

# === Telegram Config ===
BOT_TOKEN = os.getenv("BOT_TOKEN") 
CHAT_IDS = os.getenv("CHAT_IDS")

def send_telegram(msg):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    for chat_id in CHAT_IDS:
        data = {'chat_id': chat_id, 'text': msg}
        try:
            requests.post(url, data=data)
        except Exception as e:
            print(f"❌ Failed to send to {chat_id}: {e}")


# === Setup Chrome Options ===
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

last_status = "Decision pending"

print("🚀 Starting monitor loop...")

while True:
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Step 1: Visit start page
        driver.get(START_URL)
        time.sleep(4)

        # Step 2: Find *first* "Log in" <a> tag
        login_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'Log in')]")
        if not login_links:
            raise Exception("No login links found.")
        login_links[0].click()
        time.sleep(4)

        # Step 3: Fill in login form
        driver.find_element(By.NAME, "LoginId").send_keys(USERNAME)
        driver.find_element(By.NAME, "Password").send_keys(PASSWORD)
        driver.find_element(By.NAME, "Submit").click()
        time.sleep(2)
        print("Login attempt complete. Current URL:", driver.current_url)

        # Step 4: Enter workspace
        enter_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, \"LoginAs_Proposer_105\")]"))
        )
        enter_link.click()
        print("Entered workspace.")
        time.sleep(5)

        # Step 5: Check submission status
        row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//td[text()='{PAPER_ID}']/parent::tr"))
        )
        status_text = row.find_elements(By.TAG_NAME, "td")[6].text.strip()
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f"[{timestamp}] Paper status:", status_text)

        if status_text != last_status:
            msg = f"📢 [{timestamp}]\nStatus changed! Update: {status_text}"
            send_telegram(msg)
            print("✅ Alert sent.")
            break

    except Exception as e:
        print("⚠️ Error during check:", e)

    finally:
        driver.quit()

    print("Sleeping 5 minutes before next check...\n")
    time.sleep(300)  # Sleep 5 minutes
