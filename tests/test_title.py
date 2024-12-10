

def check_title_tag(driver, url):
    try:
        title = driver.title
        if len(title) > 160:
            return [url, "Title Tag Test", "Fail", "Title tag length is more than 160 characters."]
        else:
            return [url, "Title Tag Test", "Pass", "Title tag length is valid."]
    except Exception as e:
        return [url, "Title Tag Test", "Fail", f"Error extracting title: {str(e)}"]