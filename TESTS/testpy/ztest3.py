import process as p
import os
import pprint


test = """
Sekai de ichi-ban OHIME-SAMA
Sou iu atsukai KOKORO-ete
Yo ne?

Sono-ichi
Itsumo to chigau kami-gata ni kiga-tsuku koto
Sono-ni
Chanto kutsu made mirukoto, ii ne?
Sono-san
Watashi no hito-koto niwa mittsu no kotoba de henji suru koto
Wakattara migite ga orusu nanowo nantoka-shite!

Betsu ni wagamama nante itte nai n dakara
Kimi ni KOKORO kara omotte hoshii no KAWAII tte

Sekai de ichiban ohime-sama
Ki ga tsuite nee nee
Mataseru nante rongai yo
Watashi wo dare dato omotteru no?
Mou nanda ka amai mono ga tabetai!
Ima sugu ni yo

Oh, check one two… Ahhhhhh!
Ketten? Kawaii no machigai desho
Monku wa yurushimasen no
Ano ne? Watashi no hanashi chanto kiiteru? Chotto…
A, sore to ne? Shiroi ouma-san kimatteru desho?
Mukae ni kite
Wakattara kashizuite te wo totte “ohime-sama” tte

Betsu ni wagamama nante itte nain dakara
Demo ne sukoshi kurai shikatte kuretatte iino yo?

Sekai de watashi dake no OUJI-SAMA
Kiga tsuite hora hora
Otete ga aitemasu
Mukuchi de buaiso na OUJI-SAMA
Mou, doushite? kiga tsuite yo hayaku
Zettai kimi wa wakatte nai!… wakatte nai wa…

Ichigo no notta SHOOTOKEEKI
Kodawari tamago no torokeru PURRIN
Minna, minna gaman shimasu…
Wagamama na ko dato omowa-nai de
Watashi datte yareba-dekiru no
Ato de koukai suru wayo

Touzen desu! datte watashi wa
Sekai de ichi-ban OHIME-SAMA
Chanto mitete yone dokoka ni icchau yo?
Fui-ni dakishime-rareta kyuuni sonna e?
“HIKARERU abunai yo”sou-itte soppo muku KIMI
… kocchi noga ABUNAI wayo

"""

resultats = p.decoupage(test, 0)

resultats = p.decoupage(test, 0)

with open("sons/sortietest.txt", "w", encoding="utf-8") as f:
    for i in range(0, len(resultats), 20):
        chunk = resultats[i:i+20]
        # Mettre chaque élément entre guillemets
        chunk_quoted = [f'"{e}"' for e in chunk]
        # Joindre par des virgules
        line = ",".join(chunk_quoted)
        f.write(line + "\n")
