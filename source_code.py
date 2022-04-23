# -*- coding: utf-8 -*-
"""
Created on Sat Apr 2 13:33:03 2022

@author: sandeepsingh
"""
from cmath import e
import imp #importing imp to access the import internals
import os
import logging
from tkinter import E
#import pytube
import urllib
import datetime
import sys
try:
    import pytube
    except ImportError as e
    print ("Getting import error as Imported module doesn't exist", e)





def download_video():
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

# Main drama will start from here.            












