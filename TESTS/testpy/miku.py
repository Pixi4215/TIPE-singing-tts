import base_wave_func as bwf
import notes as n
fe = 44100
tab = []


TheWorldIsMine = [
    [n.fa [3],0.5],
    [n.do [4],2],
    [n.fa [3],0.25],
    [n.fa [3],0.25],
    [n.mib[3],0.5],
    [n.mib[3],0.25],
    [n.fa [3],0.5],
    [n.sol[3],0.5],
    [n.lab[3],0.5],
    [n.sol[3],0.5],
    [n.fa [3],0.5],
    [n.mib[3],0.5],
    [n.do [4],1],
    [n.mib[3],0.5],
    [n.fa [3],0.5],
    [n.do [4],1],
    [n.fa [3],0.5],


    [n.mib[3],0.5],
    [n.fa [3],0.5],
    [n.fa [3],0.5],
    [n.mib[3],0.25],
    [n.fa [3],0.25],
    [n.fa [3],1],
    [n.lab[3],1],
    [n.do [4],1],
    [n.mib[4],2],
    [n.mib[3],0.25],
    [n.fa [3],0.25],
]




part_bwf = n.part_to_bwf(TheWorldIsMine)

print(part_bwf)

audio = bwf.write_audio(part_bwf,fe)
bwf.write_file(audio, "Essai_Miku5", fe)
