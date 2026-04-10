import numpy as np
import matplotlib.pyplot as plt

# Définition de la fonction f(x)
fe = 44100



def write_with_harmonics(freqs):
    """
    fe     : fréquence d'échantillonnage
    freqs  : liste de coefficients multiplicateurs des harmoniques
             ex: [[1], [2, 3, 5]] => harmoniques de w : w, 2w, 3w, 5w
    """

    assert freqs is not None

    def func(t):
        val = 0
        for n in range(len(freqs)):
            valtemp = 0
            if freqs[n]:
                for w in freqs[n]:
                    # harmonique = coeff * (n+1) * fréquence fondamentale w
                    valtemp += np.sin(2 * np.pi * ((n+1) * w) * t)
            if len(freqs[n]) != 0:
                val += valtemp / len(freqs[n])
        return val

    return func



f = write_with_harmonics([[240],[]] )  
g=np.sin

# Domaine des x
x = np.linspace(-2, 2, 400)  # de -10 à 10 avec 400 points
y = f(x)

# Tracé
plt.figure(figsize=(6,6))
plt.plot(x, y, label="f(x)", color="blue")

# Axes
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

# Style du repère
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.title("Représentation graphique de f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.savefig("graphique.png")  # enregistre dans un fichier
