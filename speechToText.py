# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak

while (1):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            print("speak now")
            audio2 = r.listen(source2)
            print("processing")
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            # Uncomment below for Hindi Font
            # MyText = r.recognize_google(audio2, language="hi-IN")
            MyText = MyText.lower()

            # writing to a text file
            # print("Did you say " + MyText)
            # print("writing to file")
            # with open('speechToText.txt', 'w', encoding='utf-16') as f:
            #     f.write(MyText)

            # Open a file with access mode 'a'
            print(MyText)
            print("writing to file")
            file_object = open('speechToText.txt', 'a', encoding='utf-16')
            # Append 'hello' at the end of file
            file_object.write(MyText+"\n")
            # Close the file
            file_object.close()
            exit()

            # SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
