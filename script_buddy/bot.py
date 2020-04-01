# import tweepy
import json
import tweepy
from utils import update_index, get_start_index
from text_to_image import generate_media

with open('data/generated/samples.json') as f:
    scripts = json.load(f)

index = get_start_index()
index = 1342



generate_media(scripts[index])

with open("env/auth.json","r") as f:
    data = json.load(f)

auth = tweepy.OAuthHandler(data['api_key'], data['api_secret'])
auth.set_access_token(data['access_token'], data['access_token_secret'])

api = tweepy.API(auth)

api.update_with_media('images/script_output.jpeg',f"{index}:{scripts[index][:100]}...")




