# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:48:58 2021

@author: Jordon
"""
#Import all our necessary packages and choose the directory where start_twitter is located
import os
os.chdir('C:/Users/Jordon/python_summer2021/Day6/Lecture')
import importlib
import tweepy
import time
#start twitter and set up the api
twitter = importlib.import_module('start_twitter')
api = twitter.client
#get our university's data
wupsci = api.get_user('@WUSTLPoliSci')
#set up a follower dictionary
follower_count = {}
follower_activity = {}
follower_friend = {}
#run a loop to enter data on the follower's follower count, activity, and if they are a friend
for i in range(0,wupsci.followers_count):
    user = api.get_user(wupsci.followers_ids()[i])
    def friend():
        if wupsci.id in user.followers_ids():
            return True
        else:
            return False
    try:
        follower_count[user.screen_name] = user.followers_count
    except:
        follower_count[user.screen_name] = 'Error'
    try: 
        follower_activity[user.screen_name] = user.statuses_count
    except: 
        follower_activity[user.screen_name] = 'Error'
    try:            
        follower_friend[user.screen_name] = friend()
    except:
        follower_friend[user.screen_name] = 'Error'
    print(i,' user finished')

#Find the max of each, returning a user
max(follower_activity,key=follower_activity.get)
max(follower_count,key=follower_count.get)
#make a list of followers to check for friends status
followers = list(follower_count.keys())        
followers
#make a friend list and then run a loop to populate it
friends = []
for i in followers:
    if follower_friend[i] == True:
        friends.append(i)
#Create a dictionary of user activity through a function to find the max
activity = {}
def activerange(friendlist,min,max):
    for x in friendlist:
        if follower_count[x] >= min and follower_count[x] < max:
           activity[x] = follower_activity[x]

        else:
            pass

#Run the function to find the most active in each range
activity = {}
activerange(friends,0,100)
max(activity,key = activity.get)
#the most active user among layman friends is user WUSTLDC
activity = {}
activerange(friends,100,1000)
max(activity,key = activity.get)
#The most active user among exper users is prof_nokken
activity = {}
activerange(friends,1000,1000000000000)
max(activity,key=activity.get)
#The most active user in celebrity status is user 'alucardi1

#Repeat the process for activity
popularity = {}
for x in friends:
    popularity[x] = follower_count[x]
popularity
max(popularity, key = popularity.get)
#WashUengineers is the most popular friend


#####Problem 2
#This can be solved by using a loop in a loop to get the list of friends
#of friends. Due to a limited twitter developer account, I was not
#able to finish the code in time to test everything.
friends_extended = []
follower_count_extended = {}
follower_activity_extended = {}
follower_friends_extended = {}
for i in range(0,wupsci.followers_count):
    user = api.get_user(wupsci.followers_ids()[i])
    def friend():
        if wupsci.id in user.followers_ids():
            return True
        else:
            return False
    friends_extended.append(user.screen_name)
    try:
        follower_count_extended[user.screen_name] = user.followers_count
    except:
        follower_count_extended[user.screen_name] = 'Error'
    try: 
        follower_activity_extended[user.screen_name] = user.statuses_count
    except: 
        follower_activity_extended[user.screen_name] = 'Error'
    try:            
        follower_friends_extended[user.screen_name] = friend()
    except:
        follower_friends_extended[user.screen_name] = 'Error'
    try:
        for n in range(0,user.followers_count):
            user_extended = api.get_user(user.followers_ids()[n])
            friends_extended.append(user_extended)
            try:
                follower_count_extended[user_extended.screen_name] = user_extended.followers_count
            except:
                follower_count_extended[user_extended.screen_name] = 'Error'
            try: 
                follower_activity_extended[user_extended.screen_name] = user_extended.statuses_count
            except: 
                follower_activity_extended[user_extended.screen_name] = 'Error'
            try:            
                follower_friends_extended[user_extended.screen_name] = friend()
            except:
                follower_friends_extended[user_extended.screen_name] = 'Error'                
    except:
        print('User {}\'s profile is private')        
    print(i,' user finished')
 #Using the list created, we can run the function above
 activity = {}
 activerange(friends_extended,0,100)
 max(activity,key = activity.get)

popularity_extended = {}
for x in friends:
    popularity_extended[x] = follower_count[x]
popularity_extended
max(popularity, key = popularity.get)
