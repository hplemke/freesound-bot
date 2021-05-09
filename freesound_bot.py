import os
import requests
import random
import tweepy

MAX_SOUND_ID = 570715

consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
freesound_client_secret = os.getenv('FREESOUND_CLIENT_SECRET')

# get a random sound
random.seed()
sound_id = random.randint(0, MAX_SOUND_ID)
response = requests.get(f'https://freesound.org/apiv2/sounds/{str(sound_id)}/?token={freesound_client_secret}')
# raise an error if there was an error response code
response.raise_for_status()
tweet = response.json()['description'][0:280]

# post the sound description to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.update_status(tweet)
