import cv2,os,glob, shutil
from os.path import isfile, join
from PIL import Image
import nltk, datetime
import speech_recognition as sr

fps = 1
time = 2


def img_to_vid(pthIn, pthOut):
    frame_array=[]
    files=[f for f in os.listdir(pthIn) if isfile(join(pthIn,f))]
    for i in range (len(files)):
        filename = pthIn+files[i]
        img = cv2.imread(filename)

        for k in range(time):
            frame_array.append(img)
                                                          # 125x205 is dimension of resized img
    out = cv2.VideoWriter(pthOut, cv2.VideoWriter_fourcc(*'mp4v'), fps, (281,363) )
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()


def fetch_img(text):
    new_name_index = 0
    for word in text:
        try:
            im = Image.open('C:/Users/user/PycharmProjects/videomake/ResizedImage/'+ word + '.png')
            im.save('C:/Users/user/PycharmProjects/videomake/Final/' + str(new_name_index)+ '.png')
            new_name_index += 1
        except:
            for letter in word.lower():
                try:
                    im = Image.open('C:/Users/user/PycharmProjects/videomake/ResizedImage/'+ letter + '.png')
                    im.save('C:/Users/user/PycharmProjects/videomake/Final/' + str(new_name_index)+ '.png')
                    new_name_index += 1 #important  (same new_name_index replaces image)
                except:
                    im = Image.open('C:/Users/user/PycharmProjects/videomake/ResizedImage/idk.png')
                    im.save('C:/Users/user/PycharmProjects/videomake/final/'+ str(new_name_index)+'.png')
                    new_name_index += 1  #important (same new_name_index replaces image)
    
        

def del_punc(tokens):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for member in tokens:
        if member in punctuations:
            tokens.remove(member)
    # display the unpunctuated string
    print('tok', tokens)
    return tokens

def tokenize(voice_text):
    tokens = nltk.word_tokenize(voice_text)
    not_necessary = ['is', 'the', 'in', 'of', 'at', 'after', 'am', 'before', 'for', 'a', 'an']
    for element in tokens:
        if element in not_necessary:
            tokens.remove(element)
    print(tokens)
    return tokens


def clear_Final_folder(dir):
    os.chdir(dir)
    files = glob.glob('*.png')
    for filename in files:
        os.unlink(filename)

def audio_to_text(dir):
    r = sr.Recognizer()
    with sr.AudioFile(dir) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = 'null'
    return text


def text_to_text(dir):
    text_file = open(dir, 'r')
    text = ''
    lines = text_file.readlines()
    for i in lines:
        text += i + ' '
    return text

def Backup_history(source, dest):
    current_time = datetime.datetime.now()
    shutil.copy(source, dest)
    #unique filename generator fnm
    fnm = str(current_time.hour) + '_' + str(current_time.minute) + '_'+ str(current_time.second) + '_' + str(current_time.year) + '_' + str(current_time.month)
    os.rename(dest+'/vid_ex.mp4', dest+fnm+'.mp4')

import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
        
def Update_Database(url):
    dest = 'C:/Users/user/PycharmProjects/videomake/ResizedImage'
    shutil.copy(url, dest)

    #unique filename generator fnm
    #os.rename(dest+'/vid_ex.mp4', dest+fnm+'.mp4')
