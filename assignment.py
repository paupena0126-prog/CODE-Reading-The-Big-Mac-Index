import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'


def get_big_mac_price_by_year(year, country_code):
    df = pd.read_csv(big_mac_file)
    filtered = df[(df['date'].str[:4] == str(year)) &
                   (df['iso_a3'].str.lower() == country_code)]
    average_price = filtered['dollar_price'].mean()
    return round(float(average_price), 2)


def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    filtered = df[df['iso_a3'].str.lower() == country_code]
    average_price = filtered['dollar_price'].mean()
    return round(float(average_price), 2)


def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    filtered = df[df['date'].str[:4] == str(year)]
    cheapest = filtered.loc[filtered['dollar_price'].idxmin()]
    country = cheapest['name']
    code = cheapest['iso_a3']
    price = round(float(cheapest['dollar_price']), 2)
    return f"{country}({code}): ${price}"


def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    filtered = df[df['date'].str[:4] == str(year)]
    expensive = filtered.loc[filtered['dollar_price'].idxmax()]
    country = expensive['name']
    code = expensive['iso_a3']
    price = round(float(expensive['dollar_price']), 2)
    return f"{country}({code}): ${price}"


if __name__ == "__main__":
    print(get_the_cheapest_big_mac_price_by_year(2008))
    print(get_the_most_expensive_big_mac_price_by_year(2003))
    print(get_big_mac_price_by_year(2008, 'mys'))
    print(get_big_mac_price_by_country('usa'))
