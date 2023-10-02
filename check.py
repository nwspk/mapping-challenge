import random
from urllib.parse import urlparse

#import requests

filenames = ["a.csv", "b.csv", "c.csv"]

global_list = set()

for team in filenames:
    f = open(team)
    data = f.read().split("\n")
    data = [entry.strip('"') for entry in data]

    netlocs = set()
    twitter_links = 0
    facebook_links = 0

    for url in data:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        try:
            parsed = urlparse(url)
        except:
            continue
        if parsed.netloc == "facebook.com":
            facebook_links += 1
        if parsed.netloc == "twitter.com":
            twitter_links += 1
        netlocs.add(parsed.netloc)
        #print(parsed)

        global_list.add(parsed.netloc)

    print(team)
    print("sum:", len(netlocs))
    print("twitter_links:", twitter_links)
    print("facebook_links:", facebook_links)

    #count_get = 0
    #for url in random.sample(data, 20):
    #    if not url.startswith("http://") and not url.startswith("https://"):
    #        url = "http://" + url
    #    try:
    #        r = requests.get(url)
    #        count_get += 1
    #    except:
    #        continue

    #print("count get:", count_get)
    print()

#print()
#print("count global:", len(global_list))
#print()
