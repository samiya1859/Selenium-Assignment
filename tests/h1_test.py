from selenium.webdriver.common.by import By
import logging

def check_h1_tag(driver, url):
    try:
        h1_tag = driver.find_element(By.TAG_NAME, "h1")
        logging.info(f"H1 tag found on {url}")
        return [url, "H1 Tag Existence Test", "Pass", "H1 tag found."]
    except Exception as e:
        logging.error(f"Error finding h1 tag on {url} : {e}")
        return [url, "H1 Tag Existence Test", "Fail", "H1 tag is missing."]
