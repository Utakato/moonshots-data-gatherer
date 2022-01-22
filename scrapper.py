import helper
from bs4 import BeautifulSoup as bs

def create_entry(row, base_url):
    rank = int(row.find("p").text)
    symbol = row.find("p", attrs={'class': "coin-item-symbol"}).text
    name = row.find("p", attrs={'class': "iworPT"}).text
    tds = row.find_all("td")
    link = base_url + tds[3].find("a", attrs={'class': "cmc-link"}).attrs['href']



    stringprice = tds[3].find("span").text[1:]
    if stringprice.__contains__("..."):
        price = "Too many 0's" #maybe find a way to see the actual number.
    else: 
        price = float(stringprice.replace(",", "")) 


    marketCap = int(tds[6].find("span", attrs={'class': "ieFnWP"}).text[1:].replace(",", ""))

    return {
        'rank': rank,
        'name': name,
        'symbol': symbol,
        'price': price,
        'market_cap': marketCap,
        'link': link, 
    }


def get_coins(startPage, endPage):
    url = "https://coinmarketcap.com"
    current_page = startPage
    coins= []
    i = 0
    while True:
        with helper.init_driver(f"{url}/?page={i}") as driver:            
            helper.scroll_to_bottom(driver)

            soup = bs(driver.page_source, "html.parser")
            table = soup.table
            rows = table.find_all("tr")
            rows.pop(0) 

            for row in rows:
                new_entry = create_entry(row, url)
                coins.append(new_entry)
            
            print(f'Finished page {current_page}')
            
            if current_page == endPage: 
                break
            else:
                current_page += 1
            i += 1
    print("Coins received")
    return coins


def update_DB(coins_list, db): 
    print("Update initialized! Should take about 7.5 minutes.")
    for coin in coins_list:
        db.replace_one({"name": coin['name']}, coin)
    print("Updated 900 coins!")
