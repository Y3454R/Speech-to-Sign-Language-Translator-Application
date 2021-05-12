import nltk
import Ashik

voice_text= Ashik.record()
tokens =[]


def tokenize(voice_text):
    tokens = nltk.word_tokenize(voice_text.lower())
    not_necessary = ['is', 'the', 'in', 'of', 'at', 'after']
    for element in tokens:
        if element in not_necessary:
            tokens.remove(element)
    text = ''
    for element in tokens:
        text = text + element
    return text


'''def photo_to_vid():
    frameSize = (125, 205)

    out = cv2.VideoWriter('C:/Users/user/PycharmProjects/videomake/Output/ex_vid.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'), 1, frameSize)

    for filename in glob.glob('C:/Users/user/PycharmProjects/videomake/Final/*.png'):
        img = cv2.imread(filename)
        out.write(img)

    out.release()'''

directory = 'C:/Users/user/PycharmProjects/videomake'
pthIn = directory +'/Final/'
pthOut = directory + '/Output/vid_ex.mp4'

print(voice_text)

text = Ashik.del_punc(tokenize(voice_text))
Ashik.fetch_img(text)
Ashik.img_to_vid(pthIn,pthOut)

Ashik.clear_Final_folder(pthIn)
print("done")
