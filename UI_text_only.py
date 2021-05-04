from kivy.config import Config

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '200')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

class Root(BoxLayout):
    pass


class RecordButton(Button):
    output = StringProperty('')

    def record(self):
        #Blocking Audio Capture
        with m as source:
            audio = r.listen(source)

        try:
            value = r.recognize_google(audio)
            self.output = "You said \"{}\"".format(value)

        except sr.UnknownValueError:
            self.output = ("Oops! Didn't catch that")

        except sr.RequestError as e:
            self.output = ("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))


class SpeechApp(App):
    def build(self):
        # Calibrate the Microphone to Silent Levels
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(r.energy_threshold))
        return Root()


# When Executed from the command line (not imported as module), create a new App
if __name__ == '__main__':
    SpeechApp().run()
