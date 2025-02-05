# Stock News Alert System

This Python script tracks the stock price of a specified company and sends SMS alerts when there is a significant change in the stock price. If the price fluctuates by more than 5% between two consecutive days, it fetches the latest news articles related to the company and sends them via SMS using Twilio.

## Features
- Fetches daily stock prices using the Alpha Vantage API.
- Calculates the percentage change between consecutive days.
- Retrieves the top 3 news articles related to the company when significant price changes occur.
- Sends SMS notifications with stock movement details and news headlines.

## Prerequisites
- Python 3.x
- Twilio Account (for SMS functionality)
- API Keys for:
  - [Alpha Vantage](https://www.alphavantage.co/)
  - [News API](https://newsapi.org/)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-news-alert.git
   cd stock-news-alert
   ```
2. Install the required Python packages:
   ```bash
   pip install requests twilio
   ```

## Configuration
1. Replace the placeholders in the script with your API keys and Twilio credentials:
   ```python
   STOCK = "APPLE"
   COMPANY_NAME = "Apple"
   NEWS_API_KEY = "YOUR-API-KEY"
   ALPHAVANTAGE_API_KEY = "YOUR-API-KEY"
   account_sid = 'YOUR-ACC-SID'
   auth_token = "YOUR-AUTH-TOKEN"
   ```
2. Set your phone number in the `to` parameter of the `client.messages.create` method.

## Usage
Run the script:
```bash
python stock_alert.py
```

The script will:
- Fetch the closing prices for the last two days.
- Calculate the percentage change.
- If the change exceeds 5%, retrieve the latest news articles.
- Send an SMS with the stock change and news details.

## Example SMS Format
```
APPLE: 🔺2%
Headline: Apple unveils new product lineup.
Brief: Apple has launched its latest series of devices at an exclusive event.
For further details visit https://example.com
```

## License
This project is licensed under the MIT License.

## Acknowledgments
- [Alpha Vantage](https://www.alphavantage.co/)
- [News API](https://newsapi.org/)
- [Twilio](https://www.twilio.com/)

## Contact
For any queries, reach out at [your-email@example.com].

