import base_wave_func as bwf
import numpy as np
import notes as n
#fréquence d'échantillonage = Nombre de sons par seconde
fe = 44100


def bandpass_filter_point(x, center_freq, fe, bandwidth=100):
    """Retourne le gain d'un filtre passe-bande appliqué à une sinusoïde à l’instant x"""
    w = 2 * np.pi * center_freq / fe
    return np.sin(w * x)


def make_vowel_func(formants, fe):
    """Crée une fonction sinusoïdale sommée des formants"""
    def vowel_func(t, f0):
        val = 0
        for formant in formants:
            val += np.sin(2 * np.pi * formant * t)
        return val / len(formants)
    return vowel_func

fe = 44100


def test():
    formants_A = [700, 1220, 2600]   
    formants_O = [400, 800, 2600]    # petit o
    formants_E = [390, 2000, 2550]
    formants_I = [270, 2290, 3010]
    formants_U = [300, 870, 2240]
    formants_Y = [310, 2300, 2900]  # [y] = "u" français

    formants_I = [ 270,2290, 2700]


    func_A = make_vowel_func(formants_A, fe)
    func_O = make_vowel_func(formants_O, fe)
    func_E = make_vowel_func(formants_E, fe)
    func_I = make_vowel_func(formants_I, fe)
    func_U = make_vowel_func(formants_U, fe)
    func_Y = make_vowel_func(formants_Y, fe)


    # Structure : [ [ [durée, freq, volume, fonction_gauche], [durée, freq, volume, fonction_droite] ], ... ]
    tab = [
        [[3, 220, 0.9, func_A]], 
        [[3, 220, 0.9, func_O]], 
        [[3, 220, 0.9, func_E]], 
        [[3, 220, 0.9, func_I]], 
        [[3, 220, 0.9, func_U]], 
        [[3, 220, 0.9, func_Y]], 
    ]
    return tab

Formant_testa = [250,500,750,1000,1250,1500,1750,2000,2250,2500,2750,3000]
Formant_teste = [150,250,350,1250]

func_testa = make_vowel_func(Formant_testa, fe)
func_teste = make_vowel_func(Formant_teste, fe)

#tab=[[[3, 220, 0.9, func_testa]],[[3, 220, 0.9, func_teste]]]


def sh(i,f) :
    return np.sin( 2 * np.pi * i * f)

do3 = 261
la3 = 440


'''
audio = bwf.write_audio( [ 
    [[1,261,0.1,sh]], 
    [[1,293,0.1,sh]], 
    [[1,329,0.1,sh]], 
    [[1,349,0.1,sh]], 
    [[1,391,0.1,sh]], 
    [[1,440,0.1,sh]], 
    [[1,493,0.1,sh]],
    [[1,523,0.1,sh]]
] ,fe)
'''

def f(tab):
    tempo = tab.pop()
    freq = tab.pop()
    return [[tempo,freq,0.1,sh]]

partition = [
    [n.do [3],0.35],
    [n.mi [3],0.25],
    [n.sol[3],0.25],
    [n.do [4],0.25],
]

tab = list(f(i) for i in partition)

#tab =  [[[1,400,0.2,sh]],[[1,400,0.2,sh]],[[1,400,0.2,sh]]]
audio = bwf.write_audio( tab , fe)
#audio = bwf.write_audio( [ [[0.1,200+10*i,0.4,sh],[0.1, 200+10*i,0.4,sh]] for i in range(0,30)] ,fe,)


bwf.write_file(audio,"Etest2",fe)

