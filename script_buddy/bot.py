# import tweepy
import json
import time

import gunicorn
import tweepy

from text_to_image import generate_media
import datetime


def update_index():
    "Updates samples index from which tweets are being generated"
    with open('counter.json', 'r+') as f:
        data = json.load(f)
        data['last_index'] = data['last_index'] + 1 # <--- add `id` value.
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
        
def get_start_index():
    "Gets the current index of generated samples"
    with open('counter.json', 'r') as f:
        data = json.load(f)
        index = data['last_index'] # <--- add `id` value.
        return index

with open('data/generated/samples.json','r') as f:
    scripts = json.load(f)

with open("env/auth.json", "r") as f:
    data = json.load(f)

auth = tweepy.OAuthHandler(data['api_key'], data['api_secret'])
auth.set_access_token(data['access_token'], data['access_token_secret'])

starttime = time.time()

print("Bot Online")

while True:
    index = get_start_index()
    update_index()

    try:
        generate_media(scripts[index])
        print("I get here")
        api = tweepy.API(auth)
        media =  api.media_upload('images/script_output.jpeg')
        api.update_status(status=f"{index}:{scripts[index][:100].strip()}...", media_ids=[media.media_id])
        print("Updated twitter with sample of index ", index)

    except BaseException as e:
        print('Something went wrong')
        print(e)
    print('working still')
    time.sleep(21_600 - time.time() % 21_600)
