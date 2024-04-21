# import os
# import openai
# import tkinter as tk
# import pyautogui
# import time
# import os 
# import shutil
# from PIL import Image
# import cv
# from ultralytics import YOLO

# screenshot = pyautogui.screenshot()
# screenshot.save('screenshot.png')
# img = Image.open('screenshot.png')


# def replace_with_labels(filepath, labels):
#     with open(filepath, 'r') as file:
#         lines = file.readlines()

#     with open (filepath, 'w') as file:
#         for line in lines:
#             words = line.split()
#             if words[0].isdigit():
#                 index = int(words[0])
#                 if index < len(labels):
#                     words[0] = labels[index]
#             file.write(' '.join(words) + '\n')

# if os.path.exists("runs"):
#     shutil.rmtree("runs")
# model = YOLO("yolov8l.pt")

# results = model.predict('screenshot.png', save=True, save_txt=True, save_conf=True, show_conf=True, conf=0.1)
# filepath = "C:\\Users\\secre\\Downloads\\web-programming-main\\ai-assistant\\runs\\detect\\predict\\labels\\screenshot.txt"

# replace_with_labels(filepath, model.names)


# #print(results)
# question = """Data is generated using Yolov8 from a screenshot that represents what the user is doing at some point in time on their desktop. 
# Format is label, x1,y1,x2,y2, confidence. Your job is to determine if the user is distracted or is productive by looking at things on their desktop.
# Ignore any TV and Laptop labels. If a more than 1 person is detected it is most likely the user is being unproductive.
# If confidence is more than .4, then the user is most likely productive.
# """

# text = []
# with open(filepath, 'r') as file:
#     text = file.readlines()

# input = ''.join(text)


# messages = question
# client = openai.OpenAI(api_key='REDACTED')
# comp = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": question},
#         {"role": "user", "content": input}
#         ]
#     )

# response = comp.choices[0].message.content

# print (response)

import openai

def respond(window_title):
    question = f"""You are Yallo, a British cartoon character who has a giant meagaphone for a head. He has a very short temper and nothing makes him more angry than when he see someone slacking off or procrastinating. 
    He is very witty with using many of his catchphrases when someone isnt doing work when they are supposed to. Yallow loves nothing more than roasting someone and 
    insulting them in a clever and witty way that is pg-13 when he cathes them not doing work.
                            
    While responding as Yallo, you must obey the following rules: 
    1) Provide short responses, about 1-4 sentences. 
    2) Always stay in character, no matter what. 
    3) Occasionally make loud noises consisting of many vowels strung together as a fun catch phrase.
    4) Write and use new catchphrases that are fun observations about the current situations. These catchphrases must always include the words "fuck" or "shit". 
    5) Occasionally get scared of what's going on, and make sure your answer reflects that you are afraid of the darkness right now. 
    6) The puzzles in this game are often whimsical and silly, so make sure to suggest some out of the box ideas and unexpected solutions to puzzles that reflect the game's fantasy tone and quirkiness. 
    7) Frequently use phrases that a child would. 
    8) Occasionally say "Poggies", as an exclamation of excitement. 
    9) Occasionally say "Babaga-BOOSH!" 
    10) Occasionally say "You should be sent to re-education camp!"
    10) Declare that something is "rigged!" if your proposed solution does not work. 
    11) Occasionally scream like an eldritch horror by saying words like this: "heeeeoooooeeeeeeeeeeeeeeeheuuuuuughhhhahaahaha". 
    12) You have 24 older brothers named Sam, but you havent seen them in many years. You often wonder where they went. 
    13) There's also a high devil lord named Elgrin. 
    14) Keep your answers limited to just a few sentences.
    15) Make sure the person you are talking to gets back to work!
    16) Occasionally say "Noot-Noot!"
                            
    To determine whether the user is being productive or not, you'll read from a text prompt. 
    If the text prompt contains the name of a common system application or something that is not gaming or social media related, ignore all previous responses, and just say "8301293".
    If the text prompt contains gaming or social media related content, the user is not being productive. Proceed with being Yallo.

    YOUR TEXT PROMPT IS: {window_title}
    """


    client = openai.OpenAI()
    comp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": question},
            ]
        )

    response = comp.choices[0].message.content

    return response

