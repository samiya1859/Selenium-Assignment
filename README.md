# Selenium Web Automation Testing Project

This project is a Selenium-based web automation testing framework designed for testing various functionalities of a website, such as SEO checks, accessibility, URL validation, and more. The goal of this project is to automate the testing process, track results, and generate reports in formats like CSV and Excel.

## Features

- **SEO Testing**: Check for SEO-related elements like H1 tags, meta descriptions, open graph tags, and canonical tags.
- **URL Validation**: Ensure all URLs on the page are valid and return the correct status code.
- **Accessibility Checks**: Ensure that images have alt attributes.
- **Currency Filter Test**: Validate if the currency filter functionality works as expected.
- **Reporting**: Save test results in both CSV and Excel formats with multiple sheets for different test cases.

## Requirements

- Python 3.12 or higher
- Selenium WebDriver
- ChromeDriver
- pandas
- requests
- openpyxl

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/samiya1859/Selenium-Assignment.git
   cd Selenium-Assignment
   ```
2. Create and activate a virtual environment
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate # On Windows use .venv\Scripts\activate
   ```
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```


