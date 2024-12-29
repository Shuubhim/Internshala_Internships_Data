# Internship Data Scraper

This repository contains a Python script designed to scrape internship listings from **Internshala**. It extracts key details such as roles, company names, stipends, durations, and locations, and organizes them into a structured dataset for further analysis.

## Features
- Utilizes **Requests** and **BeautifulSoup** for web scraping.
- Extracts data such as:
  - Internship roles
  - Company names
  - Stipends offered
  - Duration of internships
  - Locations of internships
- Outputs the scraped data into a **pandas DataFrame** for easy processing and analysis.

## Dependencies
- `pandas`
- `numpy`
- `requests`
- `beautifulsoup4`

## How to Use
1. Clone the repository.
2. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script to fetch internship details and generate a DataFrame.

## Notes
- The script is configured to scrape internship data from multiple pages of Internshala.
- Error handling is implemented to manage missing data gracefully.

## Future Improvements
- Save the scraped data into a CSV file for portability.
- Add functionality to scrape additional details like application deadlines and required skills.
- Enhance efficiency by implementing asynchronous requests.
