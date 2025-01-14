import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Choose a voice (try a male voice with a deeper tone)
for voice in voices:
    if "male" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Adjust the pitch and speed for a "Santa Claus" effect
engine.setProperty('rate', 130)  # Slightly slower
engine.setProperty('volume', 1.0)  # Full volume

# Add some jolly Santa-like words
santa_words = "Ho ho ho! Merry Christmas to all, and to all a good night!"

# Speak the Santa-like phrase
engine.say(santa_words)
engine.runAndWait()
