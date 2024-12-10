from selenium.webdriver.common.by import By

def check_image_alt_attributes(driver, url):
    images = driver.find_elements(By.TAG_NAME, "img")
    missing_alt = False
    for image in images:
        if not image.get_attribute("alt"):
            missing_alt = True
            break
    if missing_alt:
        return [url, "Image Alt Attribute Test", "Fail", "One or more images are missing the alt attribute."]
    else:
        return [url, "Image Alt Attribute Test", "Pass", "All images have alt attributes."]
