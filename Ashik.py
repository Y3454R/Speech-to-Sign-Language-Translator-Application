import cv2,os,glob
from os.path import isfile, join
from PIL import Image
import nltk

fps = 1
time = 2


def img_to_vid(pthIn, pthOut):
    frame_array=[]
    files=[f for f in os.listdir(pthIn) if isfile(join(pthIn,f))]
    for i in range (len(files)):
        filename = pthIn+files[i]
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)

        for k in range(time):
            frame_array.append(img)

    out = cv2.VideoWriter(pthOut, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()

def fetch_img(text):
    new_name_index = 0
    for letter in text:
        if letter == ' ':
            continue
        else:
            try:
                im = Image.open('C:/Users/user/PycharmProjects/videomake/ResizedImage/'+ letter + '.png')
                im.save('C:/Users/user/PycharmProjects/videomake/Final/' + str(new_name_index)+ '.png')

            except:
                im = Image.open('C:/Users/user/PycharmProjects/videomake/ResizedImage/idk.png')
                im.save('C:/Users/user/PycharmProjects/videomake/final/'+
                                str(new_name_index)+'.png')
        new_name_index += 1


def del_punc(sentence):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in sentence:
        if char not in punctuations:
            no_punct = no_punct + char
    # display the unpunctuated string
    return no_punct


def clear_Final_folder(dir):
    os.chdir(dir)
    files = glob.glob('*.png')
    for filename in files:
        os.unlink(filename)


import speech_recognition as sr
from kivy.properties import StringProperty

r = sr.Recognizer()
#dure = int(input("Set duration"))
dure = 4


def record():
    with sr.Microphone() as source:
        print("Speak now")
        audio = r.record(source, duration=dure)
        try:
            output = r.recognize_google(audio)

        except:
            output = "Could not recognize"
    return output
