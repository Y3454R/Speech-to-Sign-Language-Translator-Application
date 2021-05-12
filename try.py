'''import glob
from PIL import Image

imageNames = glob.glob(r"C:\ Users\ user\PycharmProjects\videomake\images\*.png")
new_width  = 125
new_height = 205
count=0

for i in imageNames:
	img = Image.open(i)
	img = img.resize((new_width, new_height), Image.ANTIALIAS)

	img.save(r"C:\ Users\ user\PycharmProjects\videomake\ResizedImage\\"+str(count)+".png")
	count+=1
	print("Images Resized " +str(count)+"/"+str(len(imageNames)),end='\r')

def clear_Final_folder(dir):
    os.chdir(dir)
    files = glob.glob('*.png')
    for filename in files:
        os.unlink(filename)


def fetch_img():
    new_name_index = 0
    for letter in text:
        im = Image.open('C:/Users/user/PycharmProjects/videomake/ResizedImage/'+ letter + '.png')
        im.save('C:/Users/user/PycharmProjects/videomake/Final/' + str(new_name_index) + '.png')
        new_name_index += 1  '''


import nltk
nltk.download('averaged_perceptron_tagger')
sentence = """Today morning, Arthur felt very good."""

# tokene into words
tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)
# print tokens
#Loop through the tagged tweets

print(tags)
