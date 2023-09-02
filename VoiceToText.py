
import os
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr

# Path to the input audio file
audio_file = "C:\\Users\\Dell\\Downloads\\aa.wav"

# Load the audio file
audio = AudioSegment.from_file(audio_file)

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Load the temporary WAV file for transcription
with sr.AudioFile(audio_file ) as source:
    audio_data = recognizer.record(source)

# Perform speech recognition
try:
    text = recognizer.recognize_google(audio_data)
    print("Transcription:")
    print(text)
except sr.UnknownValueError:
    print("Speech recognition could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")
print("here")


word_duration_ms = 2000  # Adjust as needed
chunks = [audio[i:i + word_duration_ms] for i in range(0, len(audio), word_duration_ms)]

# Initialize the starting time
current_time = 0

# Iterate through chunks and print starting times
for i, chunk in enumerate(chunks):
    # Convert the current_time to seconds
    current_time_seconds = current_time / 1000.0

    # Print starting time
    print(f"Word {i + 1} starts at {current_time_seconds} seconds")

    # Update current_time
    current_time += len(chunk)

