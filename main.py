import numpy as np
from scipy.io.wavfile import write
from playsound import playsound

duration = 2

# B major chord
frequencies = [246.94, 311.13, 369.99]

t = np.linspace(0, duration, duration * 44100, False)

wave = sum(np.sin(2 * np.pi * f * t) for f in frequencies)

# Write to output/sound.wav file
write('output/sound.wav', 44100, wave)

# Play the sound
playsound('output/sound.wav')