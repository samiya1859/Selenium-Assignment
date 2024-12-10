import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_currency_filter(driver, url):
    result = []

    try:
        footer = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "footer"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", footer)
        time.sleep(2)

        dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "js-currency-sort-footer"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        time.sleep(2)

        dropdown.click()

        currency_items = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#js-currency-sort-footer .select-ul li"))
        )

        if len(currency_items) == 0:
            result = [url, "Currency Filter Test", "Fail", "No currency items found in the dropdown."]
            return result

        currency_item_to_click = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(currency_items[1])
        )
        currency_item_to_click.click()
        time.sleep(3)

        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".price-info.js-price-value"))
        )
        price_text = price_element.text

        if "€" in price_text:
            result = [url, "Currency Filter Test", "Pass", "Currency successfully changed to EUR."]
        elif "$" in price_text:
            result = [url, "Currency Filter Test", "Pass", "Currency successfully changed to USD."]
        else:
            result = [url, "Currency Filter Test", "Fail", "Currency did not change correctly."]
    
    except Exception as e:
        result = [url, "Currency Filter Test", "Fail", f"Error while interacting with currency filter: {str(e)}"]

    return result
