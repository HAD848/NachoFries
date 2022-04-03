# Nacho Fries Twitter Bot
    
Twitter bot written in Python using Tweepy and BeautifulSoup. Checks the Taco Bell website for changes in the status of the Nacho Fries' Avaliability, and updates a twitter account with that ***vital*** information.

###### Setup

In order to use this program, a number of steps have to be done. 
* Firstly one must sign up for a Twitter Developer Account and recieve escalated privelages, storing keys and tokens in a safe location.
* Set `Config.ini` to contain keys, tokens, and the twitter handle of your developer account.
* (Optional) Set up a cron job or scheduled task to run your program daily.
* You're all set! Just make sure there's any tweet on your timeline, and run the program.

###### Troubleshooting

If you're encountering any errors, make sure the following are all correct:
* Keys and Tokens are properly set in `Config.ini`
* Your Tokens are set to `Read and Write` access on Twitter
* There's at least one tweet on your timeline
* The name set in `Config.ini` is the one beginning with an `@`, not the screen name. IE `@NachoFries2`
* Your Twitter Developer Account has escalated privelages. This requires submitting an application to Twitter to get your app verified by them.
