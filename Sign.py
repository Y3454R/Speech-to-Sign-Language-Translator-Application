import speech_recognition as sr
from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


r = sr.Recognizer()
m = sr.Microphone()
dure = 5
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
class Root(BoxLayout):
    def about(self):
        self.ids.info.text = 'CSE 3200'

    def contact(self):
        self.ids.info.text = 'Ashikur Rahman\n' \
                             'Roll 1707090'

    def spinner_clicked(self,value):
        if value == 'Upload Recorded audio':
            self.ids.welcome.text = 'Uploading'
            self.ids.info.text = ''
        elif value == 'Enter text':
            self.ids.welcome.text = 'Entering'
            self.ids.info.text = ''
        elif value == 'Upload text':
            self.ids.welcome.text = 'Uploading text'
            self.ids.info.text = ''

    def next(self):
        wk = self.ids.spinner_id.text
        if wk == 'Options':
            self.ids.welcome.text = 'Error: Please select an option'
        elif wk == 'Upload text':
            self.ids.welcome.text = wk
        elif wk == 'Upload Recorded audio':
            self.ids.welcome.text = wk
        elif wk == 'Enter text':
            self.ids.welcome.text = wk

    def record(self):
        with m as source:

            audio = r.record(source,duration=dure)
            try:
                value = r.recognize_google(audio)
                self.ids.info.text = value
            except sr.UnknownValueError:
                self.ids.info.text = ("Oops! Didn't catch that")
            except sr.RequestError as e:
                self.ids.info.text = format(e)



class SpeechApp(App):
    def build(self):
        # Calibrate the Microphone to Silent Levels
        with m as source:
            r.adjust_for_ambient_noise(source)

        return Root()


if __name__ == '__main__':
    SpeechApp().run()





