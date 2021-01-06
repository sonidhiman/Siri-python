import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#engine.say("hiii")
#engine.say("what can i do for u")
#engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
#global command
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa','')
            print(command)
    except:
        pass
    return command

def run_alexa():
      command = take_command()
      print(command)
      if 'play' in command:
          song = command.replace('play', '')
          talk('playing'+song)
          pywhatkit.playonyt(song)
      elif 'time' in command:
          time = datetime.datetime.now().strftime('%H:%M ')
          print(time)
          talk('current time is'+ time)
      elif 'wikipedia' in command:
          person = command.replace('wikipedia', '')
          info = wikipedia.summary(person, 1 )
          print(info)
          talk(info)
      elif 'date' in command:
          talk('sorry , i have headache')
      elif 'are you single' in command:
          talk('i am in a relationship with wifi')
      elif 'joke' in command:
          print(pyjokes.get_joke())
          talk(pyjokes.get_joke())
      else:
          talk('please say the command again')


while True:
 run_alexa()
