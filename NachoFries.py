import requests
import tweepy
from bs4 import BeautifulSoup
from configparser import ConfigParser

#Loads Config.ini
config = ConfigParser()
config.read('Config.ini')

#Pulls variables from Config.ini
key = config.get('Keys','key')
key_secret = config.get('Keys', 'key_secret')
token = config.get('Tokens', 'token')
token_secret = config.get('Tokens', 'token_secret')
user_name = config.get('User', 'user_name')


#Sets up Twitter OAuth and API
auth = tweepy.OAuth1UserHandler(key, key_secret, token, token_secret)

auth.client = tweepy.API(auth)


#Functions to obtain source code parse
def get_src(url):
    agent= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"}
    source=requests.get(url, headers=agent)
    return source

def get_data(source):
    soup = BeautifulSoup(source.content, 'html.parser')
    #print(soup.prettify) #Debug
    s = soup.find('p', string='Nacho Fries are back at THE BELL® and back where they belong—with you.')
    return s

s = get_data(get_src('http://tacobell.com/nacho-fries'))


#Reads latest tweet on timeline
user = auth.client.get_user(screen_name=user_name)
tweet = auth.client.user_timeline(user_id = user.id_str, count = 1)[0]
#print(tweet.text) #Debug


#Checks if Nacho Fries exist, then checks if the status has changed from last tweet. If changed, sends update tweet.
if(s!=None):
    #Success
    if(tweet.text!="The Taco Bell Nacho Fries have now returned!"):
        auth.client.update_status("The Taco Bell Nacho Fries have now returned!")
else:
    #Fail
    if(tweet.text!="The Taco Bell Nacho Fries have left the menu!"):
        auth.client.update_status("The Taco Bell Nacho Fries have left the menu!")
