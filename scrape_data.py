from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service

# Initialize the WebDriver
chromedriver_path = "/home/w3e11/Downloads/chromedriver-linux64/chromedriver"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)


driver.get('https://www.alojamiento.io')  # Replace with the actual URL

# Extract data from window.ScriptData
data = driver.execute_script("""
    // Function to traverse nested object and find the required values
    function findValue(obj, key) {
        if (obj === null || obj === undefined) return '';
        if (obj.hasOwnProperty(key)) return obj[key];
        for (const prop in obj) {
            if (obj.hasOwnProperty(prop) && typeof obj[prop] === 'object') {
                const value = findValue(obj[prop], key);
                if (value !== '') return value;
            }
        }
        return '';
    }
    
    return {
        SiteURL: findValue(window.ScriptData, 'SiteUrl'),
        CampaignID: findValue(window.ScriptData.pageData, 'CampaignId'),
        SiteName: findValue(window.ScriptData, 'SiteName'),
        Browser: window.navigator.userAgent,
        CountryCode: findValue(window.ScriptData, 'CountryCode'),
        IP: findValue(window.ScriptData, 'IP')
    };
""")

# Print the extracted data (optional)
print(data)

# Create a DataFrame and save it to an Excel file
df = pd.DataFrame([data]) 
df.to_excel('scraped_data.xlsx', index=False)

# Close the driver
driver.quit()
