import os
import openai
import tkinter as tk
import pyautogui
import time
import cv2
import os 
import shutil
from PIL import Image
from ultralytics import YOLO

screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')
img = Image.open('screenshot.png')


def replace_with_labels(filepath, labels):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    with open (filepath, 'w') as file:
        for line in lines:
            words = line.split()
            if words[0].isdigit():
                index = int(words[0])
                if index < len(labels):
                    words[0] = labels[index]
            file.write(' '.join(words) + '\n')

if os.path.exists("runs"):
    shutil.rmtree("runs")
model = YOLO("yolov8l.pt")

results = model.predict('screenshot.png', save=True, save_txt=True, save_conf=True, show_conf=True, conf=0.1)
filepath = "C:\\Users\\secre\\Downloads\\web-programming-main\\ai-assistant\\runs\\detect\\predict\\labels\\screenshot.txt"

replace_with_labels(filepath, model.names)


#print(results)
question = """Data is generated using Yolov8 from a screenshot that represents what the user is doing at some point in time on their desktop. 
Format is label, x1,y1,x2,y2, confidence. Your job is to determine if the user is distracted or is productive by looking at things on their desktop.
Ignore any TV and Laptop labels. If a more than 1 person is detected it is most likely the user is being unproductive.
If confidence is more than .4, then the user is most likely productive.
"""

text = []
with open(filepath, 'r') as file:
    text = file.readlines()

input = ''.join(text)


messages = question
client = openai.OpenAI(api_key='sk-proj-LdpxTD770LiS6VFKp2YNT3BlbkFJOspFgqjTxMqruBv1Axl3')
comp = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": question},
        {"role": "user", "content": input}
        ]
    )

response = comp.choices[0].message.content

print (response)
