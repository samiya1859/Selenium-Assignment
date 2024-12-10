from utils.webdriver_setup import setup_driver
from tests.h1_test import check_h1_tag
from tests.h1toh6_sequence_test import check_html_tag_sequence
from tests.image_alt_test import check_image_alt_attributes
from tests.url_status_check import check_urls_with_navigation
from tests.currency_filter_test import check_currency_filter
from tests.meta_description_test import check_meta_description
from tests.test_title import check_title_tag
from tests.og_test import check_open_graph_tags
from tests.canonical_tag_test import check_canonical_tag
from utils.result_saver import save_results

def run_tests():
    driver = setup_driver()
    url = "https://www.alojamiento.io/"
    driver.get(url)
    driver.implicitly_wait(4)

    test_results = []
    test_results.append(check_h1_tag(driver, url))
    test_results.append(check_html_tag_sequence(driver, url))
    test_results.append(check_image_alt_attributes(driver, url))
    test_results.append(check_currency_filter(driver, url))
    test_results.extend(check_urls_with_navigation(driver, url))
    test_results.append(check_meta_description(driver,url))
    test_results.append(check_title_tag(driver, url))
    test_results.append(check_open_graph_tags(driver, url))
    test_results.append(check_canonical_tag(driver, url))


    save_results(test_results)

    driver.quit()

if __name__ == "__main__":
    run_tests()
