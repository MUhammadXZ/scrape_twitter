import requests
from bs4 import BeautifulSoup
import time


# Function to scrape Twitter page and count stock symbol mentions
def scrape_twitter_account(url, stock_symbol):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        tweets = soup.find_all('div', class_='tweet')
        mentions = sum(1 for tweet in tweets if stock_symbol in tweet.text)
        return mentions
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return 0


# Main function to scrape multiple Twitter accounts
def scrape_twitter_accounts(accounts, stock_symbol, interval_minutes):
    try:
        while True:
            total_mentions = 0
            for account in accounts:
                mentions = scrape_twitter_account(account, stock_symbol)
                total_mentions += mentions
                print(f"{stock_symbol} was mentioned {mentions} times in {account}")
            print(f"Total mentions of {stock_symbol}: {total_mentions}")
            print(f"Waiting for {interval_minutes} minutes before the next scrape...\n")
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("Scraping interrupted by user.")


if __name__ == "__main__":
    # List of Twitter accounts to scrape
    twitter_accounts = [
        "https://twitter.com/Mr_Derivatives",
        "https://twitter.com/warrior_0719",
        "https://twitter.com/ChartingProdigy",
        "https://twitter.com/allstarcharts",
        "https://twitter.com/yuriymatso",
        "https://twitter.com/TriggerTrades",
        "https://twitter.com/AdamMancini4",
        "https://twitter.com/CordovaTrades",
        "https://twitter.com/Barchart",
        "https://twitter.com/RoyLMattox"
    ]

    # Input parameters
    stock_symbol = "$TSLA"
    interval_minutes = 15

    # Scrape Twitter accounts for mentions of stock symbol
    scrape_twitter_accounts(twitter_accounts, stock_symbol, interval_minutes)
