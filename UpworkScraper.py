
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import random

# Initialize the undetected Chrome driver
driver = uc.Chrome()

# Lists to store scraped data
Names = []
Link_to_Profiles = []
Job_Success = []
Hourly = []
Amounts = []

# Function to detect CAPTCHA
def detect_captcha(driver):
    try:
        captcha_element = driver.find_element(By.XPATH, "//input[@aria-label='CAPTCHA']")
        if captcha_element.is_displayed():
            return True
    except Exception:
        return False

# Simulating human-like behavior with random delays
def random_sleep(min_time=1, max_time=3):
    time.sleep(random.uniform(min_time, max_time))

# Scraping through multiple pages
for i in range(1,85): 
    # Adjust the range as needed for more pages
    driver.get(f'https://www.upwork.com/nx/search/talent/?adaptive_skill_uid=1031626776454348800&nbs=2&q=sales%20copywriter&rate=0-10&page={i}')
    
    
    # Wait for the main content to be present
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h5.name.m-0"))
    )

    # Random delay to simulate human browsing
    random_sleep()

    # Check for CAPTCHA
    if detect_captcha(driver):
        print("CAPTCHA detected! Solve it manually and press Enter to continue...")
        input("Press Enter after solving the CAPTCHA manually...")

    # Continue scraping after CAPTCHA resolution
    try:
        # Scrape names and profile URLs
        names = driver.find_elements(By.CSS_SELECTOR, "h5.name.m-0 a.profile-link")
        hourly_elements = driver.find_elements(By.CSS_SELECTOR, "div.details-item.text-base strong span[data-test='rate-per-hour']")
        job_success_elements = driver.find_elements(By.CSS_SELECTOR, "div.jss-progress-circle")
        amount_earned_elements = driver.find_elements(By.CSS_SELECTOR, "strong.air3-popper-trigger")

        for index in range(len(names)):
            name = names[index].text if names[index] else None
            profile_link = names[index].get_attribute('href') if names[index] else None
            hourly_rate_text = hourly_elements[index].text if hourly_elements[index] else None
            
            # Clean and parse the hourly rate
            hourly_rate = float(hourly_rate_text.replace('$', '').replace('/hr', '').strip()) if hourly_rate_text else None
            
            # Scrape only if name, profile link, and hourly rate are present, and hourly rate is less than $20
            if name and profile_link and hourly_rate and hourly_rate < 10:
                Names.append(name)
                Link_to_Profiles.append(profile_link)
                Hourly.append(hourly_rate_text)
                
                # Append Job Success or None if missing
                if index < len(job_success_elements):
                    Job_Success.append(job_success_elements[index].text)
                else:
                    Job_Success.append(None)
                
                # Append Amount Earned or None if missing
                if index < len(amount_earned_elements):
                    Amounts.append(amount_earned_elements[index].text)
                else:
                    Amounts.append(None)

    except Exception as e:
        print(f"Error on page {i}: {e}")

    # Random delay between page loads
    random_sleep()

# Create a DataFrame and save to Excel
df = pd.DataFrame({
    'Name': Names,
    'Profile Link': Link_to_Profiles,
    'Hourly Rate': Hourly,
    'Job Success': Job_Success,
    'Amount Earned': Amounts
})

# Save the DataFrame to an Excel file
df.to_excel('upwork_profile_2.xlsx', index=False)

# Close the WebDriver
driver.quit()
#https://www.upwork.com/nx/search/talent/?adaptive_skill_uid=1031626776454348800&nbs=2&q=sales%20copywriter&rate=0-10&page=2
