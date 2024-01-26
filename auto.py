import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set your email credentials
email = "your_email@example.com"
password = "your_password"

# Set the recipient email address (for testing purposes, you can use your own email)
recipient_email = "recipient_email@example.com"

# Download the web page using requests
url = "https://example.com"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract specific information using BeautifulSoup (modify as needed)
info = soup.find("div", {"class": "some_class"}).get_text()

# Compose the email message
subject = "Extracted Information"
body = f"Here's the extracted information from {url}:\n\n{info}"

msg = MIMEMultipart()
msg["From"] = email
msg["To"] = recipient_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Send the email using your email account credentials
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email, password)
        server.sendmail(email, recipient_email, msg.as_string())
    print(f"Email sent to {recipient_email}")
except Exception as e:
    print(f"Error occurred: {e}")

