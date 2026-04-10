import numpy as np
import matplotlib.pyplot as plt


def interpoler(c):
    lx,ly = c
    assert(len(lx)==len(ly))
    def p(x):
        res = 0
        for i in range(0,len(lx)):
            li = 1
            for j in range(0,len(lx)):
                if j != i :
                    li = li * ( ( x - lx[j]) / (lx[i] - lx[j]) )
            res += (li * ly[i])
        return res
    return p


f = interpoler(([1,-1,3],[1,1,2]))

# Domaine des x
x = np.linspace(-5, 5, 40000)  
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

plt.savefig("graphes/raphique2.png")  # enregistre dans un fichier
