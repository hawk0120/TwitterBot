#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

Consumer_Key = '****'
Consumer_Secret = '****'
Access_Token =  '****'
Access_Secret = '****'
auth = tweepy.OAuthHandler( Consumer_Key, Consumer_Secret )
auth.set_access_token( Access_Token, Access_Secret )
api = tweepy.API( auth )

filename = open(argfile,'r')
f = filename.readlines()

#Opens and closes file

for line in f:
	try:
		api.update_status( status = line + " #BellLetsTalk" )
		time.sleep(10) #Tweet every 10 seconds
	except: tweepy.error.TweepError
	time.sleep(2)
	continue
f = filename.readlines()
api.update_status( status = line + " #BellLetsTalk")
filename.close()
