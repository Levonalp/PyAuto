import requests
import smtplib
import time
from email.message import EmailMessage

# Set the cryptocurrency symbol (e.g., 'bitcoin')
crypto_symbol = 'bitcoin'

# Set price thresholds
price_threshold_high = 60000
price_threshold_low = 40000

# Set the interval between price checks (in seconds)
interval = 60 * 60  # Check every hour

# Configure email settings
email_sender = 'youremail@example.com'
email_password = 'your_email_password'
email_recipient = 'recipientemail@example.com'
email_subject = f'{crypto_symbol.capitalize()} Price Alert'


def get_crypto_price(symbol):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
    response = requests.get(url)
    response_json = response.json()
    return response_json[symbol]['usd']

# Configure email settings


def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_recipient

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(email_sender, email_password)
    server.send_message(msg)
    server.quit()


while True:
    try:
        current_price = get_crypto_price(crypto_symbol)
        print(f'Current {crypto_symbol} price: ${current_price}')

        if current_price > price_threshold_high:
            email_body = f'{crypto_symbol.capitalize()} price is now above ${price_threshold_high}. Current price: ${current_price}'
            send_email(email_subject, email_body)
            print('Email sent!')

        if current_price < price_threshold_low:
            email_body = f'{crypto_symbol.capitalize()} price is now below ${price_threshold_low}. Current price: ${current_price}'
            send_email(email_subject, email_body)
            print('Email sent!')

        time.sleep(interval)
    except Exception as e:
        print(f'Error: {e}')
        time.sleep(interval)
