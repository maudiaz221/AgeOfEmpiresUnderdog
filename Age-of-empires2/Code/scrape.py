import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import json


def generateDF():
    
    # URL of the website to scrape
    url = 'https://aoe-elo.com/api?request=tournaments'

    # Make a test request
    response = requests.get(url)

    response = response.json()

    data = {'id':[], 'tournament':[], 'tier':[], 'url':[], 'prizepool':[]}
    
    for key in response:
        data['id'].append(key['id'])
        data['tournament'].append(key['name'])
        data['url'].append(key['url'])
    
    prizepool, tiers = getlinks(data['url'])
    
    data['prizepool'] = prizepool
    data['tier'] = tiers
    
    


    # CSV file path
    csv_file = 'data.csv'

    # Writing dictionary to CSV
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

    with open('data.json', 'w') as f:
        json.dump(data, f)
    
    df = pd.DataFrame(data)
    
    
       

    return df





# def getlinks(urls):
    
#     prizepool = []
#     tiers = []
    
#     for link in urls:
#         response = requests.get(link)

#         soup = BeautifulSoup(response.content, 'html.parser')
#         money = soup.find_all('p',class_='text-center m-0 font-170')
#         prizepool.append(money[0].text)

#         tournaments = []
#         # Find all <a> tags with class 'link'
#         links = soup.find_all('a')

        
#         for link in links:
#             if 'liquipedia' in link.text:
#                 tournaments.append(link)
#                 link = tournaments[0]['href']
#                 soup = BeautifulSoup(requests.get(link).content, 'html.parser')
#                 tier = soup.find_all('div', class_="infobox-cell-2 infobox-description", string='Liquipedia Tier:')
#                 tier = tier[0].find_next('div').text
#                 tiers.append(tier)
                
#             else:
#                 tiers.append('NaN')
#                 break
            
#     return prizepool, tiers

def getlinks(urls):
    none = 0
    prizepool = []
    tiers = []
    i = 0
    for link in urls:
        print(tiers)
        try:
            response = requests.get(link)
            response.raise_for_status()  # Raise an exception for non-200 status codes

            soup = BeautifulSoup(response.content, 'html.parser')
            money = soup.find_all('p', class_='text-center m-0 font-170')
            prizepool.append(money[0].text)

            # Find all <a> tags with class 'link'
            lin = soup.find('a', string='liquipedia.net')
            if lin:
                liq = lin['href']
                response = requests.get(liq)
                soup = BeautifulSoup(response.content, 'html.parser')
                tier = soup.find_all('div', class_="infobox-cell-2 infobox-description", string='Liquipedia Tier:')
                if tier:
                    tier = tier[0].find_next('div').text
                    print(tier)
                    tiers.append(tier)
                else:
                    tiers.append('NaN')
            else:
                tiers.append('NaN')

        except requests.exceptions.RequestException as e:
            print(f"Error occurred while fetching data from {link}: {e}")
            prizepool.append('NaN')  # Append NaN for prizepool
            tiers.append('NaN')  # Append NaN for tiers
        
        print(f"Processed {i+1} out of {lin} of out of {link}")
        if lin is None:
            none += 1
        i += 1
    
    print(none)
        

    return prizepool, tiers


    

if __name__ == "__main__":
    df = generateDF()
    df.to_csv('scrap.csv', index=False)
    
