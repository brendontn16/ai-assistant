import requests
import io
import pygame
import threading


def text_to_speech(inputString):

    # Initialize Pygame Mixer
    pygame.mixer.init()

    url = "https://api.elevenlabs.io/v1/text-to-speech/wo6udizrrtpIxWGp2qJk"

    payload = {
        "voice_settings": {
            "similarity_boost": 0.5,
            "stability": 1,
            "pitch": 0.5,  # Scale from -1 to 1, where 0 is normal pitch
            "rate": 1.0,  # Normal speed is 1.0, higher is faster, lower is slower
            "volume": 1.0  # Scale from 0.0 to 1.0
        },
        "text": inputString
    }
    headers = {
        "xi-api-key": "84b9a9d9b1b54d924db53f6163fbb254",
        "Content-Type": "application/json"
    }

    def get_audio():
        response = requests.request("POST", url, json=payload, headers=headers)

        if response.ok:
            audio_file = io.BytesIO(response.content)
            audio_file.seek(0)
            sound = pygame.mixer.Sound(file=audio_file)
            sound.play()
            pygame.time.wait(int(sound.get_length() * 1000))
        else:
            print("Failed to get audio:", response.status_code)

    # Start a new thread to get the audio
    threading.Thread(target=get_audio).start()





