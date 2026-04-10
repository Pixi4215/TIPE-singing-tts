import TTS.base_wave_func as bwf
import numpy as np
import PROCESS.text_process as p
fre = 44100


# fonctions pour simplfier l'écriture

def o(i):
    if i >= 4 :
        return 2
    if i < 100 or i == 0:
        return 4
    if i == 100 :
        return 1
    else :
        return 0
def e(i):
    if i == 5 or i == 19 :
        return 3
    if i == 3 or i == 4 or i == 15 or i == 18 :
        return 4
    return 0

# paramètres des formants


def gaussian_formant(f_center, bandwidth, harmonics_fund=130, n_harm=30, base_amp=3):
    """
    Génère des partiels avec amplitude pondérée par une gaussienne
    centrée sur f_center, de largeur bandwidth.
    """
    partials = []
    for i in range(1, n_harm + 1):
        freq = i * harmonics_fund
        # Poids gaussien : fort près du formant, faible loin
        amp = base_amp * np.exp(-((freq - f_center)**2) / (2 * bandwidth**2))
        if amp > 0.05:  # seuil pour ne pas additionner du bruit
            partials.append((amp, [freq]))
    return partials




params_A = [
    *[
    (30-(i/2), [105*i]) for i in range(10)
    ]
]
params_O = [
    *[
        (o(i) ,[125*i + o(100*i)])for i in range(1,6) 
    ],

]


params_E = [
    *[
        (e(i), [132*i]) for i in range(20)
    ]
]

params_I = [
    ( 3, [1, 160,310,2070]),
    (0.5, [480] + [2030 + 190*i for i in range(9)])
]

params_U = []

params_Y = []

# créations des fonctions sonores liées au formants

def write_mltp_harmo(freq):
    """
    freq : liste de tuples (k, freqs)
        - k : facteur de pondération (amplitude)
        - freqs : liste de fréquences (en Hz)
    Retourne une fonction f(t) = somme pondérée de sinusoïdes.
    """
    def func(t):
        val = 0
        count = 0
        for k, freqs_list in freq:
            for w in freqs_list:
                count += 1
                # Somme pondérée des sinusoïdes
                val += k * np.sin(2 * np.pi * w * t)
        if count != 0:
            val /= count  # normalisation
        return val

    return func

fa = write_mltp_harmo( params_A ) #done
fo = write_mltp_harmo( params_O ) #done
fe = write_mltp_harmo( params_E ) #en cours
fi = write_mltp_harmo( params_I ) #done
fu = write_mltp_harmo( params_U )
fy = write_mltp_harmo( params_Y )


def voyeller(fil,pas):
    '''
    permet de transformer un string de voyelle en sons
    
    :param fil: string de caractères
    :param pas: durée arbitraire de l'unité dans le tableau émincé
    '''

    def formant(chr):
        match chr:
            case '-':
                return lambda x : 0
            case 'a' :
                return fa
            case 'o' : 
                return fo
            case 'i' :
                return fi
            case 'e' :
                return fe
            case _ : 
                print( "caractère incorrect passsé : ",chr)
                return lambda x : 2/0

    u = p.emincer(p.decouper(fil,2))
    print("bb", u)
    tab  = []
    for vnb in u :
        v,nb = vnb 
        tab = tab + [[[pas*nb,1,formant(v)]]]
    return tab



params_E2 = []



#tab = voyeller("o-i-i-a-i-a-o-i-i-i-a-o-i",0.2)
















# Formants du e
F1_e, F2_e, F3_e = 450, 2200, 2900

c_params_E = (
    gaussian_formant(F1_e,120)
  + gaussian_formant(F2_e,200)
  + gaussian_formant(F3_e,250)
)

c_params_A = (
    gaussian_formant(800,  150, base_amp=4)  
  + gaussian_formant(1200, 200, base_amp=2)  
  + gaussian_formant(2700, 300, base_amp=1)  
)

c_params_O = (
    gaussian_formant(500, 100, base_amp=4)
  + gaussian_formant(800, 120, base_amp=2)
  + gaussian_formant(2500, 300, base_amp=0.5)
)

c_params_I = (
    gaussian_formant(270,  80,  base_amp=3)
  + gaussian_formant(2300, 180, base_amp=3)  
  + gaussian_formant(3000, 250, base_amp=1)
)

fac = write_mltp_harmo( c_params_A ) 
foc = write_mltp_harmo( c_params_O ) 
fec = write_mltp_harmo( c_params_E ) 
fic = write_mltp_harmo( c_params_I ) 


tab = [[[2,1,fac]],[[2,1,foc]],[[2,1,fec]],[[2,1,fic]]]


audio = bwf.write_audio(tab, fre)
bwf.write_file(audio, "voyelles/caoei", fre)
