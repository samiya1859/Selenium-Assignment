
from selenium.webdriver.common.by import By


def check_open_graph_tags(driver, url):
    og_tags = ["og:title", "og:image", "og:description", "og:url"]
    missing_tags = []
    
    for og_tag in og_tags:
        try:
            driver.find_element(By.XPATH, f"//meta[@property='{og_tag}']")
        except:
            missing_tags.append(og_tag)
    
    if not missing_tags:
        return [url, "Open Graph Tags Test", "Pass", "All required Open Graph tags are present."]
    else:
        return [url, "Open Graph Tags Test", "Fail", f"Missing Open Graph tags: {', '.join(missing_tags)}"]