#!/usr/bin/python3
"""script that scraping twitter accounts"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime


# Setup WebDriver
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)


def get_tweets(url, ticker, time_interval):
    """
    Scrapes tweets from a given Twitter account URL and counts how many times
    a specified ticker symbol is mentioned within a certain time interval.

    Parameters:
    - url: The URL of the Twitter account to scrape.
    - ticker: The ticker symbol to search for in the tweets.
    - time_interval: The time interval in minutes to consider for the tweets.

    Returns:
    - count: The number of times the ticker symbol is mentioned in
      the tweets from the specified Twitter account within
      the given time interval.
    """
    count = 0
    driver.get(url)
    time.sleep(15)  # Adjust this value based on your internet speed

    tweets = driver.find_elements(By.XPATH, '//div[@data-testid="tweetText"]')
    time_element = driver.find_elements(By.XPATH, '//time[@datetime]')

    for i in range(len(tweets)):
        tweet_content = tweets[i].text
        tweet_time = time_element[i]
        if ticker in tweet_content:
            tweet_datetime = tweet_time.get_attribute('datetime')
            tweet_strptime = datetime.strptime(
                tweet_datetime, '%Y-%m-%dT%H:%M:%S.%fZ')
            time_difference = datetime.now() - tweet_strptime
            if time_difference.total_seconds() / 60 > time_interval:
                break
            count += 1
    return (count)


if __name__ == "__main__":
    count = 0
    ticker = "$SPX"
    time_interval = 15
    urls = ['https://twitter.com/Mr_Derivatives',
            'https://twitter.com/warrior_0719',
            'https://twitter.com/ChartingProdigy',
            'https://twitter.com/allstarcharts',
            'https://twitter.com/yuriymatso',
            'https://twitter.com/TriggerTrades',
            'https://twitter.com/AdamMancini4',
            'https://twitter.com/CordovaTrades',
            'https://twitter.com/Barchart',
            'https://twitter.com/RoyLMattox']
    while True:
        for url in urls:
            count += get_tweets(url, ticker, time_interval)
        print("{} was mentioned {} times in the last {} minutes.".format(
            ticker, count, time_interval))
        time.sleep(time_interval * 60)

# Close the driver after all URLs have been processed
driver.quit()
