import time
import requests
from bs4 import BeautifulSoup as bs
import re

def get_watchlist_count(url):
    with requests.Session() as s:
        r = s.get(url)
        if r.status_code != 200:
            print(r)
        soup = bs(r.content, "html.parser")
        test = soup.find_all("div", attrs={'class' : "namePill"})
        return int("".join(re.findall("[0-9]+", test[2].text)))


def update_db_watchlist(id, watchlist, db): 
    query = { '_id' : id } 
    update = {'$set': { 'watchlist': watchlist } }
    db.update_one(query, update)


def update_all_coins_watchlist(db_entries, db):    
    i = 0
    for entry in db_entries:
        id = entry["_id"]
        link = entry["link"]
        
        try:
            watchlist = get_watchlist_count(link)
        except:
            print("I'm tired")
            time.sleep(70)
            watchlist = get_watchlist_count(link)
            # log error? / warning 
        
        update_db_watchlist(id, watchlist, db)
        # print(f"{entry['name']}'s watchlist has been updated!") ----- switch with log? Log: date // hh //mm //ss start : i coin has been updated.
        i+= 1
        time.sleep(0.5)  
