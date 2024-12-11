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
4. Download the appropriate ChromeDriver version and place it in the chromedriver folder.
   
## Usage
1. Make sure all dependencies are installed and ChromeDriver is set up correctly.
   Example:

```markdown
Copy code
### Prerequisites
- Python 3.12.3 or later
- Google Chrome and matching [ChromeDriver](https://chromedriver.chromium.org/downloads)
- Selenium, Pandas, Requests (install via `pip install -r requirements.txt`)
```
3. Run the main.py file to execute all tests:

```bash
python main.py
```
3. The test results will be saved in the following files:

   - test_results.csv: CSV format with test results.
   - test_results.xlsx: Excel format with test results, organized into multiple sheets for 
    each test case.
4. 
## Test Cases

The project performs the following tests:

1. H1 Tag Existence Test: Checks whether the page contains an h1 tag.
2. HTML Tag Sequence Test: Verifies the sequence of HTML tags (h1 to h6).
3. Image Alt Attribute Test: Ensures all images have valid alt attributes.
4. URL Status Code Test: Checks if all links return valid HTTP status codes (200 OK, etc.).
5. Currency Filter Test: Verifies the functionality of the currency filter on the page.
6. Meta Description Test: Ensures the page includes a <meta> tag with a description attribute.
7. Title Tag Test: Checks if the page has a <title> tag and ensures it is not empty.
8. Open Graph (OG) Tags Test: Validates the presence of Open Graph tags, such as og:title, 
  og:description, and og:image.
9. Canonical Tag Test: Verifies the presence of the <link rel="canonical"> tag to prevent 
  duplicate content issues.

## Contributing

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make changes and commit them (git commit -am 'Add new feature').
4. Push to your forked branch (git push origin feature-branch).
5. Create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

```markdown

### Explanation of Sections:
1. **Project Title**: The name and description of your project.
2. **Features**: The core features of your project.
3. **Requirements**: The dependencies required for the project, such as Python, Selenium, and other libraries.
4. **Installation**: Instructions to set up the project on a local machine.
5. **Usage**: How to run the tests and where the results are stored.
6. **Test Cases**: Describes the test cases that the script performs.
7. **Contributing**: Instructions for contributing to the project.
8. **License**: This section is optional, but if you are using a specific license (like MIT), you should include it.

You can adjust this template to fit the specific needs and structure of your project!
```
