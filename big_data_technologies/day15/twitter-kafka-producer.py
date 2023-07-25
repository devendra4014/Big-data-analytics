#!/usr/bin/python3

from tweepy import StreamingClient, StreamRule
from kafka import KafkaProducer
import json
import os

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))

class TweetStream(StreamingClient):    
    def on_tweet(self, status):
        tweet = dict()
        tweet['id'] = status.id
        tweet['time'] = status.created_at
        tweet['text'] = status.text
        tweet['author'] = status.author_id
        if len(tweet['text']) > 0:
            producer.send(topic="tweets", value=tweet)
            print(tweet)

    def on_errors(self, errors):
        print(errors)

bearer_token = os.getenv('BEARER_TOKEN')
stream = TweetStream(bearer_token)
stream.add_rules([StreamRule(value='#'), StreamRule(value='lang:en')])
stream.filter()
