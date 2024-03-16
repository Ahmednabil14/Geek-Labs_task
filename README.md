# Twitter Ticker Scraper

This project is a Python script designed to scrape tweets from specified Twitter accounts and count how many times a specified ticker symbol is mentioned within a certain time interval. It uses Selenium WebDriver for browser automation and ChromeDriver for interacting with Twitter's web interface.

## Prerequisites

- Python 3
- Selenium WebDriver
- ChromeDriver
- webdriver_manager

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install Selenium WebDriver and webdriver_manager
3. Download and install ChromeDriver.

## Usage

1. Clone this repository or download the script.
2. Open the script in a text editor and modify the `urls` list with the Twitter account URLs you want to scrape.
3. Set the `ticker` variable to the ticker symbol you're interested in.
4. Set the `time_interval` variable to the time interval in minutes you want to consider for the tweets.
5. Run the script:
6. The script will print out how many times the specified ticker symbol was mentioned in the tweets from the specified Twitter accounts within the given time interval.

## Note

Before running the script, you must log in to Twitter with a valid account, otherwise script will give you unexpected outputs.
