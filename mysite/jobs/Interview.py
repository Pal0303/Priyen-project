import cv2
import streamlit as st
import os
import speech_recognition as sr
import threading

st.title("Interview Module")

FRAME_WINDOW = st.image([])
cap = cv2.VideoCapture(0)

# Define the codec using VideoWriter_fourcc() and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Get the path to the user's Downloads folder
downloads_path = os.path.expanduser('/Users/priyen')

# Create a VideoWriter object, specifying the output file's path
out = cv2.VideoWriter(os.path.join(downloads_path, 'output.avi'), fourcc, 20.0, (640, 480))

recording = False

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Function to handle speech recognition
def recognize_speech():
    with sr.Microphone() as source:
        st.text("Recording audio for speech recognition...")
        audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
        text_file = os.path.join(downloads_path, 'transcription.txt')
        with open(text_file, 'w') as file:
            file.write(text)
        st.text(f'Transcribed text saved to: {text_file}')
    except Exception as e:
        st.text("Sorry, I did not get that")
        st.text(f"Error: {e}")

if st.button('Start/Stop Recording'):
    recording = not recording
    if recording:
        # Start a separate thread for speech recognition
        speech_thread = threading.Thread(target=recognize_speech)
        speech_thread.start()

while True:
    ret, frame = cap.read()
    if ret:
        # Write the frame into the file 'output.avi'
        if recording:
            out.write(frame)

        # Display the resulting frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        break

# Release the VideoCapture and VideoWriter objects if the recording is done
cap.release()
out.release()