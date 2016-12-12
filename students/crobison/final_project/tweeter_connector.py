#!/usr/bin/env python3

# Charles Robison
# Term project

import twitter
import json
import pandas as pd
import config

CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
OAUTH_TOKEN = config.OAUTH_TOKEN
OAUTH_TOKEN_SECRET = config.OAUTH_TOKEN_SECRET
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
 CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

def connection_confirmation():
    print("Confirming API connection...")
    print(twitter_api)

'''
Geo IDs for search, good resource here: 
http://www.knowbeforeyougo.co/yahooWOEIDs.cfm
'''
WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
world_trends_set = set([trend['name']
    for trend in world_trends[0]['trends']])

# print("Printing World trends:")
# print(json.dumps(world_trends, indent=1))

us_trends = twitter_api.trends.place(_id=US_WOE_ID)
us_trends_set = set([trend['name']
    for trend in us_trends[0]['trends']])

# print("Printing US trends:")
# print(json.dumps(us_trends, indent=1))

'''
Attempt to arrange objects into class
'''
# class geographies:
#     WORLD_WOE_ID = 1
#     US_WOE_ID = 23424977

#     def global_trends():
#         world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
#         world_trends_set = set([trend['name']
#             for trend in world_trends[0]['trends']])

#     def local_trends()
#         us_trends = twitter_api.trends.place(_id=US_WOE_ID)
#         us_trends_set = set([trend['name']
#             for trend in us_trends[0]['trends']])


common_trends = world_trends_set.intersection(us_trends_set)

# print('Printing common trends:')
# print(common_trends)

us_trends_json = json.dumps(us_trends, indent = 1)
# print(us_trends_json)
us_trends_data = us_trends[0]['trends']
print('Printing trend object data type: ')
type(us_trends_data)
print()
# print(us_trends_data)


data = []
names = [i['name'] for i in us_trends_data]
data.append(names)
print('Printing US trend results as list:')
print(data)
print()

names = [d['name'] for d in us_trends_data]
print('Printing US trends and tweet volume in readable format:')
for a in us_trends_data:
    print(a['name'], a['tweet_volume'])
print()

# Alternatively, creating data frame with results:
df = pd.read_json(us_trends_json)
print('printing data frame: ')
print('Printing US trends as data frame:')
print(df.head())








