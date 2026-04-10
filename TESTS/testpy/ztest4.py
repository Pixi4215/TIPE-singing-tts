import base_wave_func as bwf
import numpy as np
import notes as n
#fréquence d'échantillonage = Nombre de sons par seconde
fe = 44100

params_Z = [
    (4, [1]),
    *[
        (16 * j, [125 * i for i in range(1, 5)])
        for j in range(1, 30)
    ]
]

print(params_Z)




print(params_Z)

#audio = bwf.write_audio( [[[3,1,n.do[4]]]] , fe)
#print(audio)
#bwf.write_file(audio,"test_post",fe)

