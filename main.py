import os
import pymongo
import helper
import twitter
import scrapper
import watchlists

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.flhu6.mongodb.net/{DB_NAME}?retryWrites=true&w=majority")

db = client["crypto"]
raw_data_db = db["raw_data"]


if __name__ == '__main__':
    db_entires = helper.get_all_db_entries(raw_data_db)

    scrapper.update_DB(scrapper.get_coins(0,9), raw_data_db)
    watchlists.update_all_coins_watchlist(db_entires, raw_data_db)
    twitter.update_followers(db_entires, raw_data_db)