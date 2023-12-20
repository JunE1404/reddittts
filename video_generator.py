from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import cv2
import numpy as np
import moviepy.editor as mp
import time
def make_clip(sentence, length, index):
    images = []
    words_new = []
    words = sentence.split()
    
    for el in words:
        img = Image.new('RGBA', (600,400))
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default(20)
        draw.text((0, 0),el,(255,255,255),font=font)   
        images.append([img, (len(el) / len(sentence))*length])
        
    videodims = (600,400)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')    
    video = cv2.VideoWriter(f"{index}.mp4",fourcc, 60,videodims)
    
    for image in images:
        count = 0
        while count < image[1] * 60:
                imtemp = image[0].copy()
                video.write(cv2.cvtColor(np.array(imtemp), cv2.COLOR_RGB2BGR))
                count +=1
                
    video.release()
    time.sleep(1)
    
def add_audio(index):
    video1 = mp.VideoFileClip(f"C:/Users/julie/Programming/TTS/{index}.mp4")
    print(video1.filename)
    audio = mp.AudioFileClip(f"post/{index}.wav")
    final = video1.set_audio(audio)
    final.write_videofile("output.mp4")
    
    