from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import requests
import time

def check_urls_with_navigation(driver, url):
    test_results = []
    all_links_valid = True

    driver.get(url)  # Ensure we start from the given URL
    time.sleep(2)  # Allow the page to load

    # Locate all links on the page
    links = driver.find_elements(By.TAG_NAME, "a")
    link_hrefs = [link.get_attribute("href") for link in links if link.get_attribute("href")]  # Collect valid hrefs

    for link_url in link_hrefs:
        try:
            # Navigate to the link
            driver.get(link_url)
            time.sleep(2)  # Allow the page to load

            # Check the response code for the link
            response = requests.get(link_url)
            if response.status_code == 404:
                test_results.append([url, "URL Status Code Test", "Fail", f"404 error for {link_url}"])
                all_links_valid = False
            else:
                test_results.append([url, "URL Status Code Test", "Pass", f"Status Code: {response.status_code} for {link_url}"])
        except requests.exceptions.RequestException as e:
            test_results.append([url, "URL Status Code Test", "Fail", f"Request error for {link_url}: {e}"])
            all_links_valid = False
        except TimeoutException:
            test_results.append([url, "URL Status Code Test", "Fail", f"Timeout while loading {link_url}"])
            all_links_valid = False
        except StaleElementReferenceException:
            test_results.append([url, "URL Status Code Test", "Fail", f"Stale element reference for {link_url}"])
            all_links_valid = False

        # Navigate back to the original URL to continue checking other links
        driver.get(url)
        time.sleep(2)  # Allow the page to reload

    if all_links_valid:
        test_results.append([url, "URL Status Code Test", "Pass", "All URLs are valid."])

    return test_results
