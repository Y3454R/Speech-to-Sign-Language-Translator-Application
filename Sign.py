from tkinter import Entry, Label, Tk
from tkinter import filedialog, Button
import speech_recognition as sr
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import Ashik


r = sr.Recognizer()
m = sr.Microphone()


#vid = Video(source = 'C:/Users/user/PycharmProjects/videomake/Output/vid_ex.mp4')

ent_txt = TextInput( hint_text = 'Type your speech',size_hint = (1, 0.4))

directory = 'C:/Users/user/PycharmProjects/videomake'
pthIn = directory +'/Final/'
pthOut = directory + '/Output/vid_ex.mp4'

    

class Root(BoxLayout):
    

    def about(self):
        self.ids.vid.source = directory+'/Output/Contact.mp4'
        self.ids.vid.color = 'white'
        self.ids.vid.state = 'play'
        

    def contact(self):
        self.ids.info.text = 'Mail us:\n' \
                             'rahman1707090@stud.kuet.ac.bd'

    def refresh(self):
        try:
            self.ids.vid.state = 'stop'
        except:
            pass
        self.ids.vid.color = 'black'
        self.remove_widget(ent_txt)
        self.ids.welcome.text = 'Welcome to Sign Language'
        self.ids.info.text = ''
        self.ids.spinner_id.text = 'Options'
        self.ids.play.background_color = 'blue'
        
        try:
            self.add_widget(self.ids.play)
        except:
            pass


    def spinner_clicked(self,value):
        self.ids.play.background_color = 'blue'

        if value == 'Recorded audio':
            self.ids.welcome.text = 'Uploading Audio'
            self.ids.info.text = ''
            '''self.remove_widget(ent_txt)
            self.remove_widget(rec_txt)
            self.add_widget(rec_audio)'''

            self.next(value)


        elif value == 'Enter text':
            self.ids.welcome.text = 'Entering'
            self.ids.info.text = ''
            self.add_widget(ent_txt)
            

        elif value == 'Upload text':
            
            self.ids.welcome.text = 'Uploading text'
            self.ids.info.text = ''
            '''self.remove_widget(rec_audio)
            self.remove_widget(ent_txt)
            self.add_widget(rec_txt)'''
            self.next(value)

        elif value == 'Add image':
            
            root = Tk()
            root.geometry("500x150")
            root.configure(background='skyblue')
            Label(root, text='Please choose image with dimension 281x363', font=(15)).pack()
            
            root.filename = filedialog.askopenfilename(initialdir="D:/" , title="Select file", filetypes=(("png", "*.png"),("All files", "*.*")))

            Label(root, text='You selected: '+root.filename,  font=(12)).pack()
            Button(root, text='Add in', font=(12), padx=20, command=root.destroy).pack()
            
            Ashik.Update_Database(root.filename)
            self.ids.welcome.text = 'Successfully added new image'
            root.mainloop()
               

    def help(self):
        self.ids.info.text = 'Manual here'


    def next(self,wk):
        from tkinter import filedialog, Button
        

        root = Tk()
        root.geometry("300x150")
        root.configure(background='skyblue')
        
        if wk == 'Options':
            self.ids.welcome.text = 'Error: Please select an option'

        elif wk == 'Upload text':

            root.filename = filedialog.askopenfilename(initialdir="D:/" , title="Select file", filetypes=(("Text for Sign", "*.txt"), ("All files", "*.*")))
            url= root.filename
            root.title("Select Text file")
            Label(root, text='Selected: '+url, font=(16)).pack()
            Button(root, text='Convert', font=(12), padx=20, pady=15, command=root.destroy).pack()
            
            root.mainloop()

            voice_text = Ashik.text_to_text(url) 
            if voice_text == '':
                self.ids.welcome.text = 'Empty file!'
            else:
                text = Ashik.del_punc(Ashik.tokenize(voice_text))
                # print(text)  important
                if text == '':
                    self.ids.welcome.text = 'Sorry! Unexpressable in Sign Language'
                else:
                    self.ids.info.text = voice_text
                    Ashik.fetch_img(text)
                    Ashik.img_to_vid(pthIn, pthOut)
                    Ashik.clear_Final_folder(pthIn)
                    self.ids.welcome.text = 'Converted your text file!'
                    
        elif wk == 'Recorded audio':
            root.filename = filedialog.askopenfilename(initialdir="D:/" , title="Select file", filetypes=(("Audio for Sign", "*.wav"), ("All files", "*.*")))

            url= root.filename
            root.title("Select Audio file")
            Label(root, text='Selected: '+url, font=(16)).pack()
            Button(root, text='Convert', font=(12), padx=20, pady=15, command=root.destroy).pack()
            root.mainloop()

            voice_text = Ashik.audio_to_text(url)
            if voice_text == 'null':
                self.ids.info.text = 'Ops! couldn\'t recognize audio'
            else:
                text = Ashik.del_punc(Ashik.tokenize(voice_text))
                if text == '':
                    self.ids.welcome.text = 'Sorry! Unexpressable in Sign Language'
                else:
                    self.ids.info.text = voice_text
                    Ashik.fetch_img(text)
                    Ashik.img_to_vid(pthIn, pthOut)
                    Ashik.clear_Final_folder(pthIn)
                    self.ids.welcome.text = 'Converted your audio file!'

            


    def record(self):
        voice_text = 'null'
        dure = 3

        if self.ids.duration.text == '5s':
            dure = 5
        elif self.ids.duration.text == '7s':
            dure = 7
        elif self.ids.duration.text == '10s':
            dure = 10

        with m as source:
            audio = r.record(source,duration=dure)
            try:
                voice_text = r.recognize_google(audio)

            except sr.UnknownValueError:
                self.ids.info.text = ("Oops! Couldn't catch that")
            except sr.RequestError as e:
                self.ids.info.text = format(e)

        if voice_text == 'null':
            self.ids.info.text = "Oops! Couldn't catch that"
        else:
            self.ids.info.text = voice_text
            text = Ashik.del_punc(Ashik.tokenize(voice_text))
            Ashik.fetch_img(text)
            Ashik.img_to_vid(pthIn, pthOut)
            print(text)

        Ashik.clear_Final_folder(pthIn)
        print("done")

        try:
            self.add_widget(self.ids.play)
        except:
            pass


    def play(self):

        if self.ids.spinner_id.text == 'Enter text':
            text = Ashik.del_punc(Ashik.tokenize(ent_txt.text))
            print('text', text)
            if len(text)==0:
                self.ids.welcome.text = 'Sorry! Unexpressable in Sign Language!'
            else:
                Ashik.fetch_img(text)
                Ashik.img_to_vid(pthIn, pthOut)
                Ashik.clear_Final_folder(pthIn)
                self.ids.info.text = ent_txt.text
                self.remove_widget(ent_txt)
                self.ids.welcome.text = 'Converted your text!'
                try:
                    self.ids.vid.source = 'C:/Users/user/PycharmProjects/videomake/Output/vid_ex.mp4'
                    self.ids.vid.color = 'white'
                    self.ids.vid.state = 'play'
                except:
                    self.ids.welcome.text = 'Error occured'
        else:
            try:
                self.ids.vid.source = 'C:/Users/user/PycharmProjects/videomake/Output/vid_ex.mp4'
                self.ids.vid.color = 'white'
                self.ids.vid.state = 'play'
            except:
                self.ids.welcome.text = 'You haven\'t converted anything to show! '
         #important
        

    def save(self):
        
        root = Tk()
        root.geometry("300x150")
        root.configure(background='skyblue')
        root.filename = filedialog.askdirectory(initialdir="D:/" , title="Select file")

        Ashik.Backup_history(pthOut, root.filename)
        self.ids.welcome.text = 'Saved!'
        Label(root, text='Saved Successfully', pady = 20, padx=10,font=(16)).pack()
        Button(root, text='Close', font=(12), padx=20, pady=15, command=root.destroy).pack()
        root.mainloop()

class SpeechApp(App):
    def build(self):
        # Calibrate the Microphone to Silent Levels

        with m as source:
            r.adjust_for_ambient_noise(source)

        return Root()


if __name__ == '__main__':
    SpeechApp().run()



