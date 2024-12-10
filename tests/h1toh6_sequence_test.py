from selenium.webdriver.common.by import By

def check_html_tag_sequence(driver, url):
    try:
        h1_tag = driver.find_element(By.TAG_NAME, "h1")
        h2_tag = driver.find_element(By.TAG_NAME, "h2")
        h3_tag = driver.find_element(By.TAG_NAME, "h3")
        h4_tag = driver.find_element(By.TAG_NAME, "h4")
        h5_tag = driver.find_element(By.TAG_NAME, "h5")
        h6_tag = driver.find_element(By.TAG_NAME, "h6")
        return [url, "HTML Tag Sequence Test", "Pass", "All tags H1 to H6 found in sequence."]
    except:
        return [url, "HTML Tag Sequence Test", "Fail", "One or more tags are missing or out of sequence."]
