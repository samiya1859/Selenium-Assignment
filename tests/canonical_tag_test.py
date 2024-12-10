from selenium.webdriver.common.by import By

def check_canonical_tag(driver, url):
    try:
        driver.find_element(By.XPATH, "//link[@rel='canonical']")
        return [url, "Canonical Tag Test", "Pass", "Canonical tag is present."]
    except:
        return [url, "Canonical Tag Test", "Fail", "Canonical tag is missing."]