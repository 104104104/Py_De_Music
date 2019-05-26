from py_de_music import *

a = createWave("mi", 0.5)
b = createWave("do", 0.375)
c = createWave("so", 0.125)

music = a+a+a+b+c+a+b+c+a

save_wave(music, "Darth_Vader.wav")
