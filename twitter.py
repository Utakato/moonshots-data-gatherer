import requests
import os

API_BEARER_TOKEN = os.environ.get("API_BEARER_TOKEN")
search_url = 'https://api.twitter.com/1.1/users/search.json?'  



def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {API_BEARER_TOKEN}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def update_followers(db_entries, db):
    for entry in db_entries:
        id = entry["_id"]
        name = entry["name"].replace(" ", "")
        query_params = {'q' : name}

        json_response = connect_to_endpoint(search_url, query_params)
        print(json_response)

        try:
            followers = json_response[0]['followers_count']
            link = json_response[0]['url']
        except: 
            followers = 0
            link = "No response from api"
            print(f'Something went wrong while trying to retrieve {name} information.')
        
        db_query = {'_id': id}
        db_update = {'$set': {'twitter_followers': followers, 'twitter_link': link}}

        db.update_one(db_query, db_update)
        print(f'{name} updated!')
