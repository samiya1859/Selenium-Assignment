
from selenium.webdriver.common.by import By

def check_meta_description(driver, url):
    try:
        meta_description = driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute("content")
        if not meta_description:
            return [url, "Meta Description Test", "Fail", "Meta description is empty."]
        
        if len(meta_description) < 50 or len(meta_description) > 160:
            return [url, "Meta Description Test", "Fail", "Meta description length is not valid."]
        else:
            return [url, "Meta Description Test", "Pass", "Meta description length is valid."]
    except Exception as e:
        return [url, "Meta Description Test", "Fail", f"Error extracting meta description: {str(e)}"]