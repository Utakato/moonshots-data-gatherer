import os
import pymongo
import helper
import scrapper

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")


if __name__ == '__main__':
    print('Program started!')
    client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.flhu6.mongodb.net/{DB_NAME}?retryWrites=true&w=majority")

    db = client["crypto"]
    raw_data_db = db["raw_data"]
    print("Connected to DB!")

    print("Initializing initial_entries.py")
    scrapper.create_initial_entries(scrapper.get_coins(0,9),raw_data_db)