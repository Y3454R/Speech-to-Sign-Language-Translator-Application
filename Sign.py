import speech_recognition as sr

r = sr.Recognizer()
text = ''
while text !='the end':
    with sr.Microphone() as source:
        print("Speak now")
        audio = r.listen(source)
        print("recognizing...")
        try:
            text = r.recognize_google(audio)
            print('you said: {}'.format(text))
            if text =='the end':
                print('End? okay Bye Bye')
        except:
            print("Could not recognize")


