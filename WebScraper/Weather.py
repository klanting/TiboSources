import requests
from bs4 import BeautifulSoup

URL = 'https://weather.com/weather/today/l/8ca543a9a97eb2b76ebdd56bb464118a56eed1cea19fcb795f1bb55150e7258e'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

print("hours")
hour_table = soup.find('div', class_="HourlyWeatherCard--TableWrapper--1IGDr")

hours = hour_table.find_all('span', class_="Ellipsis--ellipsis--1sNTm")
for hour in hours:
    print(hour.text)

for span in hour_table.select('span[data-testid="TemperatureValue"]'):
    if span.text != "--":
        fahrenheit = int(span.text.replace("°", ""))
        celsius = round((fahrenheit - 32) * 5/9)
    else:
        celsius = "--"

    print(celsius)

for part in hour_table.select('div[data-testid="SegmentPrecipPercentage"]'):
    span = part.find('span', class_='Column--precip--2ck8J')
    chance = span.text.replace("Chance of Rain", "")
    print(chance)


print("days")
day_table = soup.find('div', class_="DailyWeatherCard--TableWrapper--3mjsg")

days = day_table.find_all('span', class_="Ellipsis--ellipsis--1sNTm")
for day in days:
    print(day.text)

for span in day_table.select('span[data-testid="TemperatureValue"]'):
    if span.text != "--":
        fahrenheit = int(span.text.replace("°", ""))
        celsius = round((fahrenheit - 32) * 5/9)
    else:
        celsius = "--"
    print(celsius)

for part in day_table.select('div[data-testid="SegmentPrecipPercentage"]'):
    span = part.find('span', class_='Column--precip--2ck8J')
    chance = span.text.replace("Chance of Rain", "")
    print(chance)
