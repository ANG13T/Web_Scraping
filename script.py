from bs4 import BeautifulSoup
import re
import csv

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

icecream_file = open('icecream_data.csv', 'w')
csv_writer = csv.writer(icecream_file)
csv_writer.writerow(['Name', 'Price', 'Rating'])

icecreamNamesTag = soup.find_all(attrs={"class": "name"})
icecreamPricesTag = soup.find_all(attrs={"class": "price"})
icecreamRatingsTag = soup.find_all(attrs={"class": "rating"})

icecreamNames = []
icecreamPrice = []
icecreamRating = []

for name in icecreamNamesTag:
    icecreamNames.append(name.text)

for price in icecreamPricesTag:
    priceText = re.search('\d.\d+', price.text).group(0)
    icecreamPrice.append(float(priceText))

for rating in icecreamRatingsTag:
    ratingText = re.search('\d+', rating.text).group(0)
    icecreamRating.append(int(ratingText))


for x in range(len(icecreamNames)):
    csv_writer.writerow([icecreamNames[x], icecreamPrice[x], icecreamRating[x]])

icecream_file.close()