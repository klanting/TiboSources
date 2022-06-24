import requests
from bs4 import BeautifulSoup


def fahrenheit_to_celsius(fahrenheit):
    fahrenheit = int(fahrenheit.replace("°", ""))
    celsius = round((fahrenheit - 32) * 5 / 9)
    return str(celsius) + "°"

def get_hour_weather(city_id):
    URL = f'https://weather.com/weather/hourbyhour/l/{city_id}'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    hour_list = []
    class_list = ["DaypartDetails--DayPartDetail--1up3g DaypartDetails--ctaShown--2cYCl Disclosure--themeList--25Q0H Disclosure--disableBorder--24EOy",
                  "DaypartDetails--DayPartDetail--1up3g DaypartDetails--ctaShown--2cYCl Disclosure--themeList--25Q0H"]

    hour_table = soup.find_all('details', class_=class_list)

    for hour in hour_table:
        day_name = hour.find('h3', class_='DetailsSummary--daypartName--2FBp2').text

        temperature = hour.find('span', class_='DetailsSummary--tempValue--1K4ka').text
        if temperature != "--":
            temperature = fahrenheit_to_celsius(temperature)

        rain_chance = hour.select('span[data-testid="PercentageValue"]')[0].text

        clouds = hour.find('span', class_='DetailsSummary--extendedData--365A_').text

        hour_list.append((day_name, temperature, rain_chance, clouds))

    return hour_list


def get_day_weather(city_id):
    URL = f'https://weather.com/weather/tenday/l/{city_id}'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    day_list = []

    day_table = soup.find_all('details', class_="DaypartDetails--DayPartDetail--1up3g Disclosure--themeList--25Q0H")
    for day in day_table:
        day_name = day.find('h3', class_='DetailsSummary--daypartName--2FBp2').text

        max_temperature = day.find('span', class_='DetailsSummary--highTempValue--3Oteu').text
        if max_temperature != "--":
            max_temperature = fahrenheit_to_celsius(max_temperature)

        min_temperature = day.find('span', class_='DetailsSummary--lowTempValue--3H-7I').text

        if min_temperature != "--":
            min_temperature = fahrenheit_to_celsius(min_temperature)

        rain_chance = day.select('span[data-testid="PercentageValue"]')[0].text

        clouds = day.find('span', class_='DetailsSummary--extendedData--365A_').text

        day_list.append((day_name, max_temperature, min_temperature, rain_chance, clouds))

    return day_list


a = get_hour_weather('8ca543a9a97eb2b76ebdd56bb464118a56eed1cea19fcb795f1bb55150e7258e')
d = get_day_weather('8ca543a9a97eb2b76ebdd56bb464118a56eed1cea19fcb795f1bb55150e7258e')
for s in d:
    print(s)
