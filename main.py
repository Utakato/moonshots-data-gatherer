import os
import pymongo
import helper
import twitter
import scrapper
import watchlists

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")


if __name__ == '__main__':
    print('Program started!')
    client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.flhu6.mongodb.net/{DB_NAME}?retryWrites=true&w=majority")
    db = client["crypto"]
    raw_data_db = db["raw_data"]
    print("Connected to DB!")

    print("Start fetching db entries!")
    db_entires = helper.get_all_db_entries(raw_data_db)
    print("Fetched all entries.")
    
    print("Proceeding to get coins")
    scrapper.update_DB(scrapper.get_coins(0,9), raw_data_db)
    print("Got all coins!")

    print("Preparing for watchlists")
    watchlists.update_all_coins_watchlist(db_entires, raw_data_db)
    print("Got all watchlists!")

    print("Moving on to twitter")
    twitter.update_followers(db_entires, raw_data_db)
    print("All done!")