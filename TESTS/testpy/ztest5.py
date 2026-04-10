from base_wave_func import write_audio, write_file, sinusoidal



# Fréquence d'échantillonnage
fe = 44100  # standard CD

# Définir une note simple (1 seconde, sinus 440 Hz, volume 0.8)
# Forme : [[[durée_gauche, volume_gauche, fonction_gauche], [durée_droite, volume_droite, fonction_droite]]]
# On peut aussi mettre juste [[durée, volume, fonction]] pour mono (copié aux deux oreilles)

son = [
    [
        [1.0, 0.8, 440],  # gauche
        [1.0, 0.8, 440]   # droite
    ]
]

# Générer les données audio
audio = write_audio(son, fe)

# Écrire dans un fichier .wav
write_file(audio, "test_son", fe)
