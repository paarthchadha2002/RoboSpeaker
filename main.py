# import os
#
# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker, this project was created by Paarth")
#     while True:
#         x = input("Enter what you want me to speak: ")
#         if x == "qan":
#             os.system('pronounce "bye bye friend"')
#             break
#         command = f'pronounce "{x}"'
#         os.system(command)

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker, this project was created by Paarth")
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "qan":
            speak("Bye bye friend, program terminated...")
            break
        speak(x)

