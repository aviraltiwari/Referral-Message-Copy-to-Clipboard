from datetime import date, timedelta
from math import ceil
import pyperclip

# Copy to clipboard


def copyToClipboard(text):
    pyperclip.copy(text)


potential_referrer = input("Enter referrers name: ").capitalize()
company_name = input("Enter company name: ").capitalize()
job_url = input("Enter job url: ")
accenture_date, current_date = date(2020, 11, 5), date.today()
date_diff = current_date - accenture_date
date_diff = date_diff.days
date_year = str((int(date_diff) // 30)//12)
date_month = str(ceil(date_diff // 30) % 12)

txt = "Hello, " + potential_referrer + \
    "! \n\nHope all is well with you! \n\nI am wondering if you would feel comfortable referring me for a position at " + \
    company_name + " (" + job_url + ").\n\nI would greatly appreciate it! \n\nI have " + date_year + " year " + date_month + \
    " months of experience at Accenture and the whole experience is in Python and Javascript specifically in React.\n\n" + \
    "I've attached the resume in the chat, you can also go to https://aviraltiwari.github.io for proof of work. ☺"

copyToClipboard(txt)
print("Success! Text copied to clipboard.")
