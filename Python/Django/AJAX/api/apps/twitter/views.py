from django.shortcuts import render, redirect
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#Use your keys
consumer_key = 'hYp6fWqkN7UBHTpZjLalEBBk3'
consumer_secret = '14WxaukmBY4upENxYHHJcmY21ula3aCMJjm1ozr0SopNOwcCoL'
access_token = '821588289157107712-EMqI3jMd4ZVgnPDXqZWlVl0OE1EuH3B'
access_secret = 'u0QMEPNsMZC2ntyLh4uFEVWdfFHDXpsHuPvxhAfAVpSs9'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
# Create your views here.
def index(request):
    return render(request, 'twitter/home.html')

def tweets(request):
    print '********inputted name **********'
    print request.POST['name']
    try:
        tweets = api.user_timeline(request.POST['name'])
        print type(tweets)
    except tweepy.TweepError:
        pass
    return redirect('/')
