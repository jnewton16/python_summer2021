from bs4 import BeautifulSoup
import urllib.rrequest
import csv
import os
import time

#set our working directory for saving the csv file
os.chdir('/Users/Jordon/python_summer2021/HW')

#To start the loop, we'll set up a loop to get all links for speeches
#Create a list to store the endings of the url
weblist = []
#set a loop long enough to work with
for c in range(0,1000): 
    #set the web address using c so we can loop to the next page
    web_address = 'https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks?page='+str(c)
    web_page = urllib.request.urlopen(web_address)
    #setup bs4 and create a list of all items at the 'a' level
    soup = BeautifulSoup(web_page.read())
    fields = soup.find_all('a')
    #since we know that the speeches are on even numbers from 62-80, we can use this to get our text to open pages:
    for i in range(0,10):    
     #set a condition that it only grabs those by President Biden
        if fields[63+2*i].text == 'Joseph R. Biden':
            #using the attribute 'href' gives us the web url end-piece for our list
            weblist.append(fields[62+2*i].attrs['href'])
        else:
            break
    #set a condition to end our project if the last speech was not by president biden  
    if len(weblist) % 10 == 0 and fields[63].text == 'Joseph R. Biden':
        time.sleep(4)
    else:
        break

#Now that we have the list of urls, lets set up a csv
with open('hw2_jordon.csv','w') as f:
    #Get our column names and write them
    w = csv.DictWriter(f, fieldnames = ("Date","Title","Text","Citation"))
    w.writeheader()
    #use a for-loop to run through our website list
    for i in range(0,len(weblist)):
        web_address2 = 'https://presidency.ucsb.edu'+weblist[i]
        web_page2 = urllib.request.urlopen(web_address2)        
        #set up a dictionary to write into our csv
        speech = {}
        #set a separate instance of our soup read
        inner_soup = BeautifulSoup(web_page2.read())
        #set up a find_all for our date instance, which occurs as the 11th instance of 'span'
        dfield = inner_soup.find_all('span')
        #set up our title, which is the only item under 'h1'
        ttlfield = inner_soup.find_all('h1')
        #find our speech text and cite, both under 'p'
        txtfield = inner_soup.find_all('p')
        speech_text = []
        cite = []
        #use a loop to separate the speech, cite, and other unnecessary objects
        for i in range(2,len(txtfield)):
            if txtfield[i].attrs == {}:
                speech_text.append(txtfield[i].text)
            elif txtfield[i].attrs == {'class': ['ucsbapp_citation']}:
                cite.append(txtfield[i].text)
                break 
            else:
                break
        #write everything to our speech dictionary
        speech["Date"] = dfield[10].text
        speech["Title"] = ttlfield[0].text
        speech["Text"] = speech_text
        speech["Citation"] = cite        
        w.writerow(speech)
        #sleep timer
        time.sleep(4)
