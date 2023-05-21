import email
import imaplib

# Connect to the mail server
mail = imaplib.IMAP4_SSL("imap.gmail.com")

# Login to your account
mail.login('your-email@gmail.com', 'your-password')

# Select the mailbox you want to delete in
# If you want SPAM, use "INBOX.SPAM"
mail.select("inbox")

# Create a response code and list of email ids
resp, items = mail.uid('search', None, "ALL")
items = items[0].split()

# Iterate over each email
for emailid in items[::-1]:
    resp, data = mail.uid(
        'fetch', emailid, "(BODY[HEADER.FIELDS (SUBJECT FROM)])")
    raw_email = data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)

    # Get subject and sender
    subject = str(email.header.make_header(
        email.header.decode_header(email_message['Subject'])))
    sender = str(email.header.make_header(
        email.header.decode_header(email_message['From'])))

    # If sender is a spam sender, move the email to the trash
    if sender == "spam-email@spam.com":
        result = mail.uid('STORE', emailid, '+FLAGS', '(\Deleted)')
        mail.expunge()

# Close the connection to the mail server
mail.close()
mail.logout()
