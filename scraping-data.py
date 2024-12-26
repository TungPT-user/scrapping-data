from bs4 import BeautifulSoup 
import requests 
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_Vietnamese_subdivisions_by_GDP"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# print(soup)

# soup.find("table", class_ = "wikitable sortable")

table = soup.find_all("table")[2]
print(table)


titles = table.find_all("th")
city_titles = [title.text.strip() for title in titles]
print(city_titles)

df = pd.DataFrame(columns = city_titles)


columns_data = table.find_all("tr")
for row in columns_data [1:]:
    row_data = row.find_all("td")
    invidual_data = [data.text.strip() for data in row_data]
    print(invidual_data)

    length = len(df)
    df.loc[length] = invidual_data

    df.to_csv("C:\\Users\\ptung\Desktop\\nhật ký Python-data\\scrapping-data\\city-gdp.csv" )