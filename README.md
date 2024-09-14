# Upwork Profile Scraper

This Python script scrapes Upwork profile details including **name**, **profile URL**, **hourly rate**, **total earnings**, and **job success rate**. It uses **Selenium** to automate the extraction process from multiple pages and allows filtering of profiles based on certain criteria.

## Features

- Scrapes the following data from Upwork profiles:
  - **Name**
  - **Profile URL**
  - **Hourly Rate**
  - **Total Earnings**
  - **Job Success Rate**
- Automatically handles pagination to traverse multiple pages.
- Option to filter profiles where specific fields (e.g., total earnings or job success rate) are missing.
- Filter profiles based on hourly rate.

## Prerequisites

To run this script, you need:
- **Python 3.x**
- **Selenium** installed:
  ```bash
  pip install selenium
  ```

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/upwork-profile-scraper.git
   cd upwork-profile-scraper
   ```



3. Run the script:
   ```bash
   python scrape_upwork_profiles.py
   ```

## Filter Profiles

The script allows filtering profiles based on specific conditions. For example, you can filter to only include profiles with:
- Hourly rate less than $20.
- Profiles where the job success rate and total earnings are missing are stored as None.

## Output

The script generates a CSV file containing the following columns:

| Name       | Profile URL                                 | Hourly Rate | Total Earnings | Job Success Rate |
|------------|---------------------------------------------|-------------|----------------|------------------|
| John Doe   | https://www.upwork.com/freelancers/johndoe  | $15/hr      | None           | None             |
| Jane Smith | https://www.upwork.com/freelancers/janesmith| $18/hr      | $5000          | 95%              |

## Customization

Modify the filtering conditions by updating the parameters in the `scrape_upwork_profiles.py` script, such as setting a different maximum hourly rate or filtering other fields.

## Known Issues

- **Upwork Captchas**: Upwork may present captchas during scraping. It's recommended to add delays between requests or limit the scraping frequency to avoid detection.


## License

[MIT License](LICENSE)

## Disclaimer

This tool is for educational purposes only. The user is responsible for any consequences of using this scraper. Ensure you comply with Upwork's Terms of Service and use the tool responsibly.
