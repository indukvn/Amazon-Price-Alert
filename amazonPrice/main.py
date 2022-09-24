from bs4 import BeautifulSoup
import requests
import smtplib

email = "your mail"
password = "your password"

URL = "https://www.amazon.in/Dell-i3-1125G4-Inspiron-5410-D560531WIN9S/dp/B097SZ1DPQ/ref=sr_1_7?keywords=touch%2Bscreen%2Blaptop&qid=1664031679&qu=eyJxc2MiOiI3LjQxIiwicXNhIjoiNy4yNCIsInFzcCI6IjIuNTkifQ%3D%3D&sprefix=touch%2Caps%2C242&sr=8-7&th=1"

response = requests.get(url=URL, headers={"Accept-Language": "your language", "User-Agent": "your data"})
data = response.text

soup = BeautifulSoup(data, "lxml")
price = soup.find(name="span", class_="a-price-whole").get_text()
print(price)

if price <= "59,000":
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg="Subject: Amazon Price Alert!\n\nThe Dell 14 (2021) Intel i3-1125G4 14'(35cm) FHD Display 2in1 Touch Screen Laptop (8GB RAM, 512Gb SSD, Win 10 + MSO, Backlit KB + FPR + Active Pen, "
            f"Silver Metal Color, Inspiron 5410, D560531WIN9S, 1.5Kg) is now available at {price} rupees/-\n\n{URL}."
    )