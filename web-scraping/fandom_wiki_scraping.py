from bs4 import BeautifulSoup
import cloudscraper
import pandas as pd

scraper = cloudscraper.create_scraper()

url = "https://fairytail.fandom.com/wiki/Fairy_Tail_(Guild)"

response = scraper.get(url)

data = []
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    headers = soup.find_all('h2')
    for header in headers:
        if 'Members' in header.get_text():
            members_header = header.get_text()

            members_table = header.find_next('table')
            
            # Go through each row in the table (skipping the header row)
            for row in members_table.find_all('tr')[1:]:
                cells = row.find_all('td')

                if len(cells) >= 4:
                    name_cell = cells[0]
                    status_cell = cells[-1]

                    link_tag = name_cell.find('a')
                    if link_tag:
                        name = link_tag.get('title')
                        link = link_tag.get('href')
                    status = status_cell.get_text(strip=True)

                    data.append({
                        "Name": name, 
                        "Status": status, 
                        "Link": link
                    })
else:
    print(response.status_code)
'''
for char in data[:5]:
    print(char)
'''        

df = pd.DataFrame(data)
df.to_csv("fairy_tail.csv", index=False)
print(df.head())