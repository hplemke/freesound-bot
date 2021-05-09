# freesound-bot
A Twitter bot that posts descriptions of sounds from freesound.org.

## Usage
You'll need to install this bot's dependencies using `pip` before you can run it:
```
pip install -r requirements.txt
```

In order to get this bot to do anything, you'll need to acquire API credentials for Twitter and Freesound,
and place them in your environment:
```
export TWITTER_CONSUMER_KEY="your Twitter consumer key"
export TWITTER_CONSUMER_SECRET="your Twitter consumer secret"
export TWITTER_ACCESS_TOKEN="your Twitter access token"
export TWITTER_ACCESS_TOKEN_SECRET="your Twitter access token secret"
export FREESOUND_CLIENT_SECRET="your Freesound secret"
```
To get your values, you'll need to create an account on both Twitter and Freesound, and complete
their developer applications for API keys. There are instructions on how to do this with Twitter
here (and other places too): https://realpython.com/twitter-bot-python-tweepy/

You can apply for Freesound access credentials here: https://freesound.org/apiv2/apply/

Once this has been done, the bot can simply be invoked with `python freesound_bot.py`.
