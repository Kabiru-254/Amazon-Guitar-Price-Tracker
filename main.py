import requests
import smtplib
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

my_email = "testitwice@yahoo.com"
mail_server = "smtp.mail.yahoo.com"
app_password = "hegokzdhwwdfjbhd"

response = requests.get(url="https://www.amazon.com/JOYMUSIC-String-Acoustic-JG-38C-BK/dp/B07R9WPFQ1/ref=sr_1_5?crid"
                        "=3MAHNK651FKV8&keywords=guitar&qid=1664438055&qu"
                        "=eyJxc2MiOiI3LjI4IiwicXNhIjoiNi43MiIsInFzcCI6IjYuMjUifQ%3D%3D&refinements=p_72%3A1248939011"
                        "&rnid=1248937011&s=musical-instruments&sprefix=guitar%2Caps%2C356&sr=1-5", headers=headers)

response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
guitar_price_dollar = soup.find(name="span", class_="a-price-whole")
guitar_price_cents = soup.find(name="span", class_="a-price-fraction")
guitar_price_dollar = guitar_price_dollar.getText().replace(".", "")
total_price = int(f"{guitar_price_dollar}{guitar_price_cents.getText()}")


def send_email():
    with smtplib.SMTP(mail_server) as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kabiruworld@gmail.com",
            msg=f"Subject: Guitar Price alert!\n\n Hey! the guitar you were looking for is below $35. Check it out:"
                f" https://www.amazon.com/JOYMUSIC-String-Acoustic-JG-38C-BK/dp/B07R9WPFQ1/ref=sr_1_5?"
                f"crid=3MAHNK651FKV8&keywords=guitar&qid=1664438055&qu=eyJxc2MiOiI3LjI4IiwicXNhIjoiNi43MiIsInF"
                f"zcCI6IjYuMjUifQ%3D%3D&refinements=p_72%3A1248939011&rnid=1248937011&s=musical-instruments&sprefix"
                f"=guitar%2Caps%2C356&sr=1-5",
        )


if total_price < 3500:
    send_email()
    print("email sent")
