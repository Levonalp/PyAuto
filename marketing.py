import smtplib


# function to send email
def send_email(subject, body, to_email, from_email, from_email_password):
    message = f"Subject: {subject}\n\n{body}"
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, from_email_password)
            server.sendmail(from_email, to_email, message)
            print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)


# variables to pass to send_email function
subject = "Newsletter: Real Estate Market Update"
body = "Hello! Here's the latest news on the real estate market..."
to_email = "recipient@example.com"
from_email = "your_email@example.com"
from_email_password = "your_email_password"
# a function call to send_email
send_email(subject, body, to_email, from_email, from_email_password)
