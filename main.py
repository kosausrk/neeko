#====================================

#WARNING CONTAINS API KEY INSIDE OF THIS CODE. TOO LAZY TO USE .ENV IN VIRTUAL STUDIo
#MAKE SURE GITHUB REPO IS PRIVATE!!!!!

#===================================




from tkinter import *
from tkinter import filedialog
from tkinter import font
import speech_recognition as sr
import os
import requests
import json
import re
from PIL import ImageTk, Image
window = Tk()


def test():
    global actual_translated_audio
    if actual_translated_audio:
        if "hello" in actual_translated_audio:
            print("scuffed fix")

def none():
    return

global actual_translated_audio
actual_translated_audio = False
global actual_weather_text_label
actual_weather_text_label = False


# ================================================Help Page
def Help_Page():
    Help_window = Toplevel()
    canvas = Canvas(Help_window, height=700, width=800)
    canvas.pack()
    # frame for logo
    help_frame = Frame(Help_window, bg="#e9fae8", bd=5)
    help_frame.place(relx=0, rely=0, relheight=700, relwidth=800)
    help_logo_frame = Frame(Help_window, bg="#b8e6c8", bd=5)
    help_logo_frame.place(relx=0.01, rely=0.06, relheight=0.1, relwidth=0.95)
    close_help_page = Button(help_logo_frame, text="Close", command=Help_window.destroy)
    close_help_page.place(relx=0.01, rely=0.65, relheight=0.7, relwidth=0.12, anchor="w")
    help_page_logo = Label(Help_window, text="insert logo", bd=5, font=40)
    help_page_logo.place(relx=0.01, rely=0.17, relheight=0.67, relwidth=0.34)
    help_page_text = Label(Help_window, text="Command 1: Hey Neeko what is the weather in [Insert City Name] \n \nCommand 2: Hey Neeko write a note [Insert Whatever Text You Want] \n The note will be saved in a file on the repl.it or on your actual computer if you aren't using this GUI on the website ",
                           bd=5, anchor="nw", font=60, wraplength=485, justify="left")
    help_page_text.place(relx=0.36, rely=0.17, relheight=0.67, relwidth=0.6)



def get_weather(city):
    try:
        weather_api = "c9c11b4d148b67961afe2f22ba965de6"
        weather_url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': weather_api, 'q': city, 'units': 'imperial'}
        response = requests.get(weather_url, params=params)
        weather = response.json()
        weather_name = weather["name"]
        weather_desc = weather["weather"][0]["description"]
        weather_desc = weather_desc.title()
        weather_temp = weather["main"]["temp"]
        #full_weather = (weather_name, "\n", weather_desc, "\n", weather_temp, "F")
        print(weather_name, "\n", weather_desc, "\n", weather_temp, "F")
    except:
        print("Invalid CIty. You entered " + city + ". Please make sure to spell correctly ")


# =======================================Weather Page
def Weather_Page():
    Weather_window = Toplevel()
    weather_canvas = Canvas(Weather_window, height=700, width=800)
    weather_canvas.pack()
    full_weather_frame = Frame(Weather_window, bg="#a5e1f2")
    full_weather_frame.place(relx=0, rely=0, relheight=700, relwidth=800)
    # creating the frame for the search bar
    frame = Frame(Weather_window, bg='#75e1ff', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
    button_frame = Frame(Weather_window, bg="#75e1ff", bd=5)
    button_frame.place(relx=0.05505, rely=0.1, relwidth=0.112, relheight=0.1, anchor="n")
    # creating the input bar
    weather_entry = Entry(frame, font=40)
    weather_entry.place(relwidth=0.65, relheight=1)
    button = Button(frame, text="Get Weather", font=40, command=lambda: get_weather(weather_entry.get()))
    # close button
    button.place(relx=0.7, relheight=1, relwidth=0.3)
    back_button = Button(button_frame, text="Close", font=40, command=Weather_window.destroy)
    back_button.place(relx=0.01, rely=0.099, relheight=0.8, relwidth=0.845)
    # creating the frame for the bottom text
    lower_frame = Frame(Weather_window, bg='#75e1ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")
    weather_text_label = Label(lower_frame, text= "label_weather")
    weather_text_label.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)


# ==============================================Notes Page
def Notes_Page():
    def New_file():
        Notes_text.delete(1.0, END)

    def open_file():
        Notes_text.delete(1.0, END)
        notes_file = filedialog.askopenfilename(defaultextension=".*", title="Open File")
        if notes_file:
            notes_file = open(notes_file, "r")
            read_notes_file = notes_file.read()
            Notes_text.insert(END, read_notes_file)
            notes_file.close

    def save_file():
        notes_file = filedialog.asksaveasfilename(title="Save as File")
        if notes_file:
            notes_file = open(notes_file, "w")
            notes_file.write(Notes_text.get(1.0, END))
            notes_file.close

    Notes_window = Toplevel()
    notes_canvas = Canvas(Notes_window, height=700, width=800)
    notes_canvas.pack()

    full_notes_frame = Frame(Notes_window, bg="#fcf083")
    full_notes_frame.place(relx=0, rely=0, relheight=700, relwidth=800)
    main_notes_frame = Frame(Notes_window, bg='#f5e133')
    main_notes_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.9)
  
    Notes_scroll = Scrollbar(main_notes_frame)
    Notes_scroll.pack(side=RIGHT, fill=Y)
    Notes_text = Text(main_notes_frame, font=("Roboto", 16), undo=True, yscrollcommand=Notes_scroll.set)
    Notes_text.place(relx=0.02, rely=0.14, relwidth=0.95)
    Notes_scroll.config(command=Notes_text.yview)
    notes_navbar = Frame(Notes_window, bg="#f5a94c")
    notes_navbar.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
    notes_clear_button = Button(notes_navbar, text = "Clear", command = New_file)
    notes_open_button = Button(notes_navbar,text = "Open File", command = open_file)
    notes_open_button.place(relx = 0.15, rely = 0.16, 
    relwidth = 0.14, relheight = 0.65)
    notes_save_button = Button(notes_navbar, text = "Save As", command = save_file)
    notes_save_button.place(relx = 0.46, rely = 0.16, relwidth = 0.14, relheight = 0.65)
    notes_clear_button.place(relx = 0.32, rely= 0.16, relwidth = 0.11, relheight = 0.65)
    Notes_close_button = Button(notes_navbar, text="Close", command=Notes_window.destroy)
    Notes_close_button.place(relx=0.02, rely=0.16, relwidth=0.1, relheight=0.65)
#===============================================To-Do Page
def Todo_page():
  Todo_window = Toplevel()
  todo_canvas = Canvas(Todo_window, height=700, width=800)
  todo_canvas.pack()
  random_label = Label(Todo_window, text = "Working")
  random_label.pack()




#==============================================main page
canvas = Canvas(window, height=700, width=800)
canvas.pack()
# full window frame
full_main_frame = Frame(window, bg="#ff7369")
full_main_frame.place(relx=0, rely=0, relheight=700, relwidth=800)
# frame with all the buttons in main window
main_frame = Frame(window, bg="#eb5938", bd=10)
main_frame.place(relx=0.63, rely=0.25, relwidth=0.7, relheight=0.5, anchor="n")
# frame for the file/chat box
chat_frame = Frame(window, bg="#eb5938", bd=10)
chat_frame.place(relx=0, rely=0.25, relheight=0.5, relwidth=0.27)

chat_label = Label(chat_frame, text="Insert File Name", bg="white", bd=10, wraplength=143, justify="left", anchor="nw")
chat_label.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.85, anchor="w")


def open_file():
    File_dialog = filedialog.askopenfilename(initialdir="/downlaods", title="Select a file")
    # checking if something in file exists if so it will procced
    if File_dialog:
        try:
            recongize = sr.Recognizer()
            audio_file = sr.AudioFile(File_dialog)
            with audio_file as source:
                audio = recongize.record(source)
                translated_audio = recongize.recognize_google(audio)
                chat_label.config(text="Neeko thinks you said: " + translated_audio)
                chat_label.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.85, anchor="w")
            if translated_audio:
                global actual_translated_audio
                actual_translated_audio = translated_audio
        except ValueError:
            print(" Only Compatabile files: PCM, WAV,AIFF/AIFF, Native FLACK. \n Most perferred is WAV")
        except AssertionError:
            print("Please enter a file")
        except:
            print("Something else went wrong, make sure to send only allowed file types or send a different file")


def audio_response():
    global actual_translated_audio
    if "weather" in actual_translated_audio:
      if actual_translated_audio:
          weather_pattern = re.compile("in(.*)$")
          weather_city_name = weather_pattern.search(actual_translated_audio).group(1)
          # audio_weather = get_weather(weather_city_name)
          chat_label.config(text=get_weather(weather_city_name))
    if "note" in actual_translated_audio:
        notes_audio = filedialog.asksaveasfilename(title="Save as File")
        if notes_audio:
            notes_pattern = re.compile("note(.*)$")
            finding_audio_note = notes_pattern.search(actual_translated_audio).group(1)
            notes_audio = open(notes_audio, "w")
            notes_audio.write(finding_audio_note)
            notes_audio.close



give_up = Button(chat_frame, text="✓", command=audio_response)
give_up.place(relx=0.689, rely=0.9, relheight=0.09, relwidth=0.2)
# upload file button
# chat_label = Label(chat_frame, text="translated_audio", bg="white", bd=10, wraplength=143, justify="left", anchor="nw")
# chat_label.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.85, anchor="w")
Upload_file = Button(chat_frame, text="Upload File", command=open_file)
Upload_file.place(relx=0.1, rely=0.896, relheight=0.11, relwidth=0.45)
# Bar at the top/ for logo
logo_frame = Frame(window, bg="#eb5938", bd=10)
logo_frame.place(relx=0.49, rely=0.140, relwidth=0.969, relheight=0.1, anchor="n")
helpButton = Button(logo_frame, text="Help", command=Help_Page)
helpButton.place(relx=0.02, rely=0.35, relheight=0.7, relwidth=0.135)
logo = Label(logo_frame, text="logo", bg="#6aeb72", bd=10)
logo.place(relx=0.9, rely=0, relheight=1.15, relwidth=0.089)
Notes_button = Button(main_frame, text="Notes", font=40, command=Notes_Page)
Notes_button.place(relx=0.265, rely=0.05, relheight=0.19, relwidth=0.2)
To_do_button = Button(main_frame, text = "To Do", font = 40, command = Todo_page)
To_do_button.place(relx = 0.52,rely = 0.05, relheight = 0.19, relwidth = 0.2)

Weather_button = Button(main_frame, text="Weather", font=40, command=Weather_Page)
Weather_button.place(relx=0.01, rely=0.05, relheight=0.19, relwidth=0.2)

window.mainloop()
