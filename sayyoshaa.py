import wave

audio = wave.open("converted.wav", "rb")
channels = audio.getnchannels()
sample_width = audio.getsampwidth()
frequency = audio.getframerate()
num_of_frames = audio.getnframes()

print("Channels:", channels)
print("Sample:", sample_width, "Bytes")
print("Frequency:", frequency)
print("Number:", num_of_frames)

samples = audio.readframes(num_of_frames)
print(len(samples))
