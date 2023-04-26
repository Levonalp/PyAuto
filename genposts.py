import random
import datetime

# Define brand keywords and templates
keywords = ["innovation", "sustainability",
            "quality", "design", "customer satisfaction"]
templates = [
    "Discover the power of {keyword} with our latest products!",
    "Experience {keyword} like never before with our brand!",
    "Our commitment to {keyword} sets us apart from the competition.",
    "Unlock the secret to {keyword} with our cutting-edge solutions!",
    "We're proud to be a leader in {keyword} - find out why our customers love us!",
]

# Generate a social media post


def generate_post():
    keyword = random.choice(keywords)
    template = random.choice(templates)
    post = template.format(keyword=keyword)
    return post

# Schedule social media posts


def schedule_posts(days, frequency):
    today = datetime.date.today()
    for day in range(days):
        post_date = today + datetime.timedelta(days=day)
        for _ in range(frequency):
            post = generate_post()
            print(f"[{post_date}] - {post}")


# Customize the number of days and post frequency per day
days = 30
frequency = 2

# Run the scheduler
schedule_posts(days, frequency)
