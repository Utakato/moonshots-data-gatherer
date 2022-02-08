<a href="https://github.com/Utakato/moonshots">Go to Moonshot repo.</a>

main.py is run everyday on a webserver to gather data for moonshots.

It uses pymongo to connect with mongoDB, bs4 and selenium to scrape data and twitter's API to get followers count.

WIP:
-Some coins with a low marketcap and a lot of followers get their followers from another account (Doggy coin get's it's followers from snoop dog's account). Not the project's real followers.

new_entries.py is used only after I wipe the DB.

runtime.txt, requirements.txt and Procfile are all needed for the scripts to run on the webserver (heroku).