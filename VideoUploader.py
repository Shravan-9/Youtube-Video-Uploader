"""
Description: This program will automate the process of uploading a video on YouTube 
using APIs and specific tags. You will be able to set the title, description, and privacy status.
"""

import os
import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

tags = [
        "Insane", "rocket", "league", "crazy", "save", "goal", "goalie", "soccer",
        "cars", "youtube", "shorts", "plat", "gold", "game", "recommended", "overtime",
        "clutch", "xbox", "ps4", "current", "season", "8", "ariel", "spin", "reverse",
        "pinch", "delay", "beat", "drop", "outrageous", "class", "saving", "sidemen",
        "gaming", "gameplay", "clips", "fyp", "viral", "movie", "music", "boost",
        "comeback", "clutch", "Platinum", "gold", "diamond", "flick", "musty", "turtle",
        "wall", "air", "dribble", "edits", "tricks", "tutorial", "rage", "tuff",
        "movement", "world", "cup", "tournament"
    ]

# Load credentials from the JSON file
credentials = None
if os.path.exists('credentials.json'):
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes=['https://www.googleapis.com/auth/youtube.upload'])
    credentials = flow.run_local_server()

# Use the credentials to build the YouTube Data API service client
if credentials is not None:
    youtube = build('youtube', 'v3', credentials=credentials)

# Function to upload video to YouTube
def upload_video_to_youtube(video_path, title, description, tags=None):
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "categoryId": "22",
                "title": title,
                "description": description,
                "tags": tags if tags else []
            },
            "status": {
                "privacyStatus": "public",   # Set video privacy to "public"
                "selfDeclaredMadeForKids": False  # Set "not made for kids"
            }
        },
        media_body=video_path
    )
    response = request.execute()
    return response


def gui_upload_video():
    video_path = input_video_path.get()
    title = input_title.get()
    description = input_description.get()
    
    if os.path.isfile(video_path):
        # Call the upload_video_to_youtube function with user-provided details and fixed settings
        response = upload_video_to_youtube(video_path, title, description, tags=tags)
        upload_completed_label.config(text="Video uploaded successfully. Video ID: " + response["id"])
    else:
        upload_completed_label.config(text="Please enter a valid video path")


def on_upload_button_click():

    video_path = input_video_path.get()
    title = input_title.get()
    description = input_description.get()
    
    if os.path.isfile(video_path):
        gui_upload_video()  # Call the gui_upload_video function
        upload_completed_label.config(text="Your Upload Has Been Completed")
    else:
        upload_completed_label.config(text="Please select a valid video file")



# Create a simple GUI
root = tk.Tk()
root.title("YouTube Video Uploader")
root.configure(background='lightblue1')

# Creates the title
title_label = tk.Label(root, text="YouTube Video Uploader", font=("Inter", 36))
title_label.configure(background="lightblue1")
title_label.pack(pady=50)

# Creates the Labels
label_video_path = tk.Label(root, text="Video Path:", font=("Inter", 16), fg="black")
label_video_path.configure(background="lightblue1")
label_video_path.place(x=80, y=220)

label_title = tk.Label(root, text="Video Title:", font=("Inter", 16), fg="black")
label_title.configure(background="lightblue1")
label_title.place(x=80, y=320)

label_description = tk.Label(root, text="Video Description:", font=("Inter", 16), fg="black")
label_description.configure(background="lightblue1")
label_description.place(x=80, y=420)

upload_completed_label = tk.Label(root, text="", font=("Inter", 16), fg="black")
upload_completed_label.configure(background="lightblue1")
upload_completed_label.place(x=80, y=620)

# Creates the Entries 
input_video_path = tk.Entry(root, width=38, font=("Inter", 18), fg="black")
input_video_path.configure(background="thistle")
input_video_path.place(x=200, y=240)

input_title = tk.Entry(root, width=38, font=("Inter", 18), fg="black")
input_title.configure(background="thistle")
input_title.place(x=200, y=340)

input_description = tk.Entry(root, width=38, font=("Inter", 18), fg="black")
input_description.configure(background="thistle")
input_description.place(x=200, y=460)

# Create upload Button 
upload_button = tk.Button(root, text="Upload Video", command= on_upload_button_click, font=("Inter", 18), bg="blue", fg="white")
upload_button.pack(pady=20)
upload_button.place(x=1200,y=650)

root.mainloop()



