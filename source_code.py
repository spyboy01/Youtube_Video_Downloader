# -*- coding: utf-8 -*-
"""
Created on Sat Apr 2 13:33:03 2022

@author: sandeepsingh

This is a weekend project which was completed in two day's. The main motive behind this project was to learn/implement python dependecy free library pytube.
"""
from cmath import e
import imp #importing imp to access the import internals
import os
import logging
from secrets import choice
from tkinter import E
#import pytube
import urllib
import datetime
import sys
try:
    import pytube
    except ImportError as e
    print ("Getting import error as Imported module doesn't exist", e)





def download_video(): #function to download single video
    URL= input("Enter The YouTube Video Link")
    try:
        video_link=YouTube(URL)
        print("Video Title is:",video_link.title)
        val=input("Do you want to download ? Y/N \n")
        if(val=='Y'): #if the user input is yes
            #video_link=video_link.streams.first()
            video_link=video_link.streams.get_highest_resolution()
            video_link.download()
            print("Dowanloading started", video_link.title)
            #directory path to download videos
            video_link.download("C:\learning\Pythin_practice\Download")
            print ("video downloaded succesfully")
            return 0

        else:
            return 0
    except:
        print("error occur while downloading the video")
        for i in range(5):
            time.sleep(2)
            print("System will retry after 2 second")


def download_play_list():
    URL= input("Enter The YouTube Video PlayList Link")
    try:
        video_link=YouTube(URL)
        #find the playlist 
        play_list=video(video_link)
        folder=play_list.title
        parent_folder="C:\learning\Pythin_practice\Download"
        path=os.path.join(parent_folder,folder) # to concatenates path components
        os.mkdir(path)
        count =0
        for i in range play_list.videos_link:
            count=count+1 #find how many videos are present in a playlist
            video_link=YouTube(URL)
            #video_link=video_link.streams.first()
            video_link=video_link.streams.get_highest_resolution()
            print("Downloading .. ", count," : ",  YouTube(URL).title)
            video_link.download(path) #download at changed location
            print ("video downloaded succesfully")
            print ("\n")
        return 0
    except:
        print("error occur while downloading the video")
        for i in range(5):
            time.sleep(2)
            print("System will retry after 2 second")       






# Main drama will start from here.
make_choice = int (input('''press: 1 For single Video

Press: 2 for PlayList '''))
print("\n")
if make_choice==1:
    download_video()
elif make_choice==2:
    download_play_list()
else:
    exit        















